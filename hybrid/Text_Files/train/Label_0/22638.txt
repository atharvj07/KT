#include <bits/stdc++.h>
using namespace std;
const int inf = 987654321;
const long long int INF = 123456789987654321;
int N, M, Xn;
struct Frog {
  int x, t, id;
};
vector<Frog> frog;
struct Mosq {
  int p, b;
};
vector<Mosq> mosq;
struct BIT {
  vector<pair<long long int, long long int> > tree;
  void init() {
    tree = vector<pair<long long int, long long int> >(
        4 * Xn, pair<long long int, long long int>(-1, -1));
  }
  void udt(int idx, pair<long long int, long long int> val, int l, int r,
           int n) {
    if (idx < l || r < idx) return;
    if (l == r) {
      tree[n] = val;
      return;
    }
    int m = (l + r) >> 1;
    udt(idx, val, l, m, 2 * n);
    udt(idx, val, m + 1, r, 2 * n + 1);
    tree[n] = max(tree[2 * n], tree[2 * n + 1]);
  }
  void add(int idx, pair<long long int, long long int> val, int l, int r,
           int n) {
    if (idx < l || r < idx) return;
    if (l == r) {
      tree[n].first += val.first;
      tree[n].second += val.second;
      return;
    }
    int m = (l + r) >> 1;
    add(idx, val, l, m, 2 * n);
    add(idx, val, m + 1, r, 2 * n + 1);
    tree[n] = max(tree[2 * n], tree[2 * n + 1]);
  }
  pair<long long int, long long int> left_most(long long int k, int a, int b,
                                               int l, int r, int n) {
    if (b < l || r < a) return pair<long long int, long long int>(-1, -1);
    if (a <= l && r <= b) {
      if (tree[n].first < k) return pair<long long int, long long int>(-1, -1);
      if (l == r) {
        if (tree[n].first >= k)
          return tree[n];
        else
          return pair<long long int, long long int>(-1, -1);
      }
      int m = (l + r) >> 1;
      if (tree[2 * n].first >= k)
        return left_most(k, a, b, l, m, 2 * n);
      else
        return left_most(k, a, b, m + 1, r, 2 * n + 1);
    }
    int m = (l + r) >> 1;
    pair<long long int, long long int> t = left_most(k, a, b, l, m, 2 * n);
    if (t != pair<long long int, long long int>(-1, -1))
      return t;
    else
      return left_most(k, a, b, m + 1, r, 2 * n + 1);
  }
} bit, bit2;
vector<int> X;
map<int, int> dx;
void compress() {
  for (int i = 0; i < N; i++) X.push_back(frog[i].x);
  for (int i = 0; i < M; i++) X.push_back(mosq[i].p);
  sort((X).begin(), (X).end());
  X.resize(unique((X).begin(), (X).end()) - X.begin());
  Xn = X.size();
  for (int i = 0; i < Xn; i++) dx[X[i]] = i;
  for (int i = 0; i < N; i++) {
    frog[i].x = dx[frog[i].x];
  }
  for (int i = 0; i < M; i++) {
    mosq[i].p = dx[mosq[i].p];
  }
}
vector<pair<long long int, long long int> > ans, restore;
int main() {
  scanf("%d %d", &N, &M);
  frog.resize(N);
  for (int i = 0; i < N; i++) {
    int x, t;
    scanf("%d %d", &x, &t);
    frog[i] = {x, t, i};
  }
  mosq.resize(M);
  for (int i = 0; i < M; i++) {
    int p, b;
    scanf("%d %d", &p, &b);
    mosq[i] = {p, b};
  }
  compress();
  bit.init();
  for (int i = 0; i < N; i++) {
    bit.udt(
        frog[i].x,
        pair<long long int, long long int>(
            X[frog[i].x] + (long long int)frog[i].t, (long long int)frog[i].id),
        0, Xn - 1, 1);
  }
  ans.resize(N);
  for (int i = 0; i < N; i++) {
    ans[i] = pair<long long int, long long int>(0, (long long int)frog[i].t);
  }
  bit2.init();
  restore = vector<pair<long long int, long long int> >(
      Xn, pair<long long int, long long int>(0, 0));
  for (int i = 0; i < M; i++) {
    int p = mosq[i].p, b = mosq[i].b;
    pair<long long int, long long int> t =
        bit.left_most(X[p], 0, p, 0, Xn - 1, 1);
    if (t == pair<long long int, long long int>(-1, -1)) {
      bit2.udt(p, pair<long long int, long long int>(1, p), 0, Xn - 1, 1);
      restore[p].first++;
      restore[p].second += (long long int)b;
      continue;
    }
    ans[t.second].first++;
    ans[t.second].second += (long long int)b;
    bit.add(frog[t.second].x,
            pair<long long int, long long int>((long long int)b, 0), 0, Xn - 1,
            1);
    while (1) {
      pair<long long int, long long int> t2 =
          bit2.left_most(1, frog[t.second].x, Xn - 1, 0, Xn - 1, 1);
      if (t2 == pair<long long int, long long int>(-1, -1)) break;
      if (X[t2.second] > (long long int)X[frog[t.second].x] +
                             (long long int)ans[t.second].second)
        break;
      bit2.udt(t2.second, pair<long long int, long long int>(-1, -1), 0, Xn - 1,
               1);
      ans[t.second].first += restore[t2.second].first;
      ans[t.second].second += restore[t2.second].second;
      bit.add(frog[t.second].x,
              pair<long long int, long long int>(restore[t2.second].second, 0),
              0, Xn - 1, 1);
      restore[t2.second] = pair<long long int, long long int>(0, 0);
    }
  }
  for (int i = 0; i < N; i++) {
    printf("%I64d %I64d\n", ans[i].first, ans[i].second);
  }
}
