#include <bits/stdc++.h>
using namespace std;
long long oo = 2e15;
const int maxn = 4e5, maxm = 1e6;
long long z0[maxm], z1[maxm], m0[maxm], m1[maxm];
int c[maxn];
int L, R, x, n, i, q;
void update(int o) {
  m0[o] = min(z0[2 * o] + m0[2 * o], z0[2 * o + 1] + m0[2 * o + 1]);
  m1[o] = min(z1[2 * o] + m1[2 * o], z1[2 * o + 1] + m1[2 * o + 1]);
}
void pushdown(int o) {
  z0[2 * o] += z0[o];
  z0[2 * o + 1] += z0[o];
  z0[o] = 0;
  z1[2 * o] += z1[o];
  z1[2 * o + 1] += z1[o];
  z1[o] = 0;
}
void build(int o, int l, int r) {
  if (l + 1 == r) {
    m0[o] = m1[o] = oo;
    if (l & 1) {
      m1[o] = c[l] - x;
      x = m1[o];
    } else {
      m0[o] = c[l] - x;
      x = m0[o];
    }
    return;
  }
  int m = (l + r) >> 1;
  build(2 * o, l, m);
  build(2 * o + 1, m, r);
  update(o);
}
void change(int o, int l, int r, int x, int y, long long u, long long v) {
  if (x <= l && r <= y) {
    z0[o] += u;
    z1[o] += v;
    return;
  }
  pushdown(o);
  int m = (l + r) >> 1;
  if (x < m) change(2 * o, l, m, x, y, u, v);
  if (m < y) change(2 * o + 1, m, r, x, y, u, v);
  update(o);
}
long long find(int o, int l, int r, int v) {
  if (l + 1 == r) {
    if (l & 1)
      return m1[o] + z1[o];
    else
      return m0[o] + z0[o];
  }
  pushdown(o);
  int m = (l + r) >> 1;
  long long re;
  if (v < m)
    re = find(2 * o, l, m, v);
  else
    re = find(2 * o + 1, m, r, v);
  update(o);
  return re;
}
void find(int o, int l, int r, int x, int y, long long &M0, long long &M1) {
  if (x <= l && r <= y) {
    M0 = min(M0, m0[o] + z0[o]);
    M1 = min(M1, m1[o] + z1[o]);
    return;
  }
  pushdown(o);
  int m = (l + r) >> 1;
  if (x < m) find(2 * o, l, m, x, y, M0, M1);
  if (m < y) find(2 * o + 1, m, r, x, y, M0, M1);
  update(o);
}
void modify(int x, int y, int z) {
  int u = 0, v = 0, len = y - x + 1;
  if (x & 1)
    u = 0, v = z;
  else
    u = z, v = 0;
  change(1, L, R, x, y + 1, u, v);
  if (len & 1) {
    if (y & 1) {
      u = -z;
      v = z;
    } else {
      u = z;
      v = -z;
    }
    if (y + 1 < n) change(1, L, R, y + 1, n, u, v);
  }
}
int ask(int x, int y) {
  int C = 0, p;
  p = (y - x) % 2 ? -1 : 1;
  if (x) C = find(1, L, R, x - 1);
  long long M0 = oo, M1 = oo;
  find(1, L, R, x, y + 1, M0, M1);
  if (x & 1) swap(M0, M1);
  if (M1 - C < 0) return 0;
  if (M0 + C < 1) return 0;
  long long D = find(1, L, R, y) + p * C;
  return D == (y - x + 1) % 2;
}
int main() {
  scanf("%d", &n);
  L = 0, R = n;
  for (i = 0; i < n; i++) scanf("%d", &c[i]);
  x = 0;
  build(1, 0, n);
  scanf("%d", &q);
  for (int qq = 1; qq <= q; qq++) {
    int opt, x, y, z;
    scanf("%d", &opt);
    if (opt == 1) {
      scanf("%d%d%d", &x, &y, &z);
      modify(x, y, z);
    } else {
      scanf("%d%d", &x, &y);
      int ans = ask(x, y);
      printf("%d\n", ans);
    }
  }
  return 0;
}
