#include <bits/stdc++.h>
using namespace std;
template <typename T>
T gcd(T x, T y) {
  if (x < y) swap(x, y);
  while (y > 0) {
    T f = x % y;
    x = y;
    y = f;
  }
  return x;
}
const int maxn = 100007;
const int maxslog = 18;
const int maxs = 100007;
const int treesize = 10000007;
int n;
int a[maxn];
int ls[treesize], rs[treesize], tr[maxn], treenode = 0;
long long S[treesize];
void update(int& x, int fr, int to, int pos, int val) {
  if (!x) x = ++treenode;
  S[x] += val;
  if (fr == to) return;
  int m = (fr + to) / 2;
  if (pos <= m)
    update(ls[x], fr, m, pos, val);
  else
    update(rs[x], m + 1, to, pos, val);
}
long long ask(int x, int fr, int to, int a, int b) {
  if (!x || (fr == a && to == b)) return S[x];
  int m = (fr + to) / 2;
  if (b <= m) return ask(ls[x], fr, m, a, b);
  if (a > m) return ask(rs[x], m + 1, to, a, b);
  return ask(ls[x], fr, m, a, m) + ask(rs[x], m + 1, to, m + 1, b);
}
void modify(int x, int y, int val) {
  if (x == 0 || y == n + 1) return;
  while (x < maxn) {
    update(tr[x], 1, n, y, val);
    x += x & -x;
  }
}
long long query(int x, int y) {
  if (x == 0 || y == n + 1) return 0;
  long long r = 0;
  while (x > 0) {
    r += ask(tr[x], 1, n, 1, y);
    x -= x & -x;
  }
  return r;
}
set<int> pos[maxn];
void insert_pos(int p, int val) {
  if (pos[val].empty()) {
    pos[val] = {0, n + 1};
    modify(0, n + 1, n + 1 - (0));
  }
  auto it = pos[val].upper_bound(p);
  int p_before = *prev(it);
  int p_after = *it;
  pos[val].insert(p);
  modify(p_before, p_after, -(p_after - (p_before)));
  modify(p_before, p, p - (p_before));
  modify(p, p_after, p_after - (p));
}
void remove_pos(int p, int val) {
  auto it = pos[val].find(p);
  if (it != pos[val].end()) {
    int p_before = *prev(it);
    int p_after = *next(it);
    modify(p_before, p, -(p - (p_before)));
    modify(p, p_after, -(p_after - (p)));
    pos[val].erase(p);
    modify(p_before, p_after, p_after - (p_before));
  }
}
int main(int argc, char* argv[]) {
  std::cin.sync_with_stdio(false);
  std::cin.tie(nullptr);
  int m;
  cin >> n >> m;
  {
    for (int i = 1; i <= n; i++) {
      cin >> a[i];
      insert_pos(i, a[i]);
    }
    for (int i = 1; i <= m; i++) {
      int x, y, z;
      cin >> x >> y >> z;
      if (x == 1)
        remove_pos(y, a[y]), insert_pos(y, a[y] = z);
      else
        cout << query(z, z) - query(y - 1, z) << endl;
    }
  }
  return 0;
}
