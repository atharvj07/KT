#include <bits/stdc++.h>
using namespace std;
int N, dad[110000][20], num[110000], cnt, F[110000];
int d[110000], Q, ccnt, B[110000], E[110000];
pair<int, int> seg[110000 * 5];
long long D[110000], len[110000][20], res;
vector<pair<int, int> > v[110000];
void dfs(int x, int parent, long long l, int depth) {
  dad[x][0] = parent;
  D[x] = l;
  d[x] = depth;
  len[x][0] = D[x] - D[parent];
  B[x] = ++ccnt;
  for (int i = 1; i <= 18; i++) dad[x][i] = dad[dad[x][i - 1]][i - 1];
  for (int i = 1; i <= 18; i++)
    len[x][i] = len[dad[x][i - 1]][i - 1] + D[x] - D[dad[x][i - 1]];
  for (int i = 0; i < (int)v[x].size(); i++)
    if (v[x][i].first != parent)
      dfs(v[x][i].first, x, l + v[x][i].second, depth + 1);
  num[x] = ++cnt;
  E[x] = ccnt;
}
pair<int, long long> get_lca(int a, int b) {
  if (d[b] > d[a]) swap(a, b);
  if (!b) return pair<int, long long>(a, 0);
  long long l = 0;
  for (int i = 18; i >= 0; i--)
    if (d[b] <= d[dad[a][i]]) {
      l += len[a][i];
      a = dad[a][i];
    }
  if (a == b) return pair<int, long long>(a, l);
  for (int i = 18; i >= 0; i--)
    if (dad[a][i] != dad[b][i]) {
      l += len[a][i] + len[b][i];
      a = dad[a][i];
      b = dad[b][i];
    }
  l += len[a][0] + len[b][0];
  return pair<int, long long>(dad[a][0], l);
}
int find_mn() {
  int k = 1, b = 1, e = N;
  while (b != e) {
    if (seg[2 * k].first) {
      k = k + k;
      e = ((b + e) / 2);
    } else {
      k = k + k + 1;
      b = ((b + e) / 2) + 1;
    }
  }
  if (!seg[k].first) return 0;
  return seg[k].second;
}
int find_mx() {
  int k = 1, b = 1, e = N;
  while (b != e) {
    if (seg[2 * k + 1].first) {
      k = k + k + 1;
      b = ((b + e) / 2) + 1;
    } else {
      k = k + k;
      e = ((b + e) / 2);
    }
  }
  if (!seg[k].first) return 0;
  return seg[k].second;
}
void upd(int k, int b, int e, int a, int t, int l) {
  seg[k].first += t;
  if (b == e) {
    seg[k].second = l;
    return;
  }
  if (a <= ((b + e) / 2))
    upd(2 * k, b, ((b + e) / 2), a, t, l);
  else
    upd(2 * k + 1, ((b + e) / 2) + 1, e, a, t, l);
}
void remove(int x) {
  for (int i = B[x]; i <= N; i += (i & -i)) F[i]--;
  upd(1, 1, N, num[x], -1, 0);
  int mn = find_mn();
  int mx = find_mx();
  int old = get_lca(mn, mx).first;
  int sm = 0;
  for (int i = E[x]; i; i -= (i & -i)) sm += F[i];
  for (int i = B[x] - 1; i; i -= (i & -i)) sm -= F[i];
  pair<int, long long> lca = get_lca(old, x);
  if (lca.first != old) {
    res -= lca.second;
    return;
  }
  if (sm) return;
  for (int i = 18; i >= 0; i--) {
    int y = dad[x][i];
    sm = 0;
    for (int i = E[y]; i; i -= (i & -i)) sm += F[i];
    if (B[y] - 1 >= 0)
      for (int i = B[y] - 1; i; i -= (i & -i)) sm -= F[i];
    if (y && !sm) {
      res -= len[x][i], x = dad[x][i];
    }
  }
  res -= len[x][0];
}
void add(int x) {
  int mn = find_mn();
  int mx = find_mx();
  int old = get_lca(mn, mx).first;
  int sm = 0;
  for (int i = E[x]; i; i -= (i & -i)) sm += F[i];
  for (int i = B[x] - 1; i; i -= (i & -i)) sm -= F[i];
  for (int i = B[x]; i <= N; i += (i & -i)) F[i]++;
  upd(1, 1, N, num[x], 1, x);
  pair<int, long long> lca = get_lca(old, x);
  if (lca.first != old) {
    res += lca.second;
    return;
  }
  if (sm) return;
  for (int i = B[x]; i <= N; i += (i & -i)) F[i]--;
  int tt = x;
  for (int i = 18; i >= 0; i--) {
    int y = dad[x][i];
    sm = 0;
    for (int i = E[y]; i; i -= (i & -i)) sm += F[i];
    if (B[y] - 1 >= 0)
      for (int i = B[y] - 1; i; i -= (i & -i)) sm -= F[i];
    if (y && !sm) {
      res += len[x][i], x = dad[x][i];
    }
  }
  for (int i = B[tt]; i <= N; i += (i & -i)) F[i]++;
  res += len[x][0];
}
int main() {
  cin >> N;
  for (int i = 1, a, b, c; i < N; i++) {
    scanf(" %d %d %d", &a, &b, &c);
    v[a].push_back(pair<int, int>(b, c));
    v[b].push_back(pair<int, int>(a, c));
  }
  dfs(1, 0, 0, 1);
  cin >> Q;
  while (Q--) {
    char c;
    int a, b;
    scanf(" %c", &c);
    if (c == '-') {
      scanf(" %d", &a);
      remove(a);
    } else if (c == '+') {
      scanf(" %d", &a);
      add(a);
    } else
      printf("%I64d\n", res);
  }
  return 0;
}
