#include <bits/stdc++.h>
const int maxn = 100000;
long long tree[5][10][maxn + 1];
int num[maxn + 1];
int lowbit(int x) { return x & -x; }
long long s(int z, int i) {
  int t = i % (2 * (z - 1));
  if (!t)
    return 2;
  else if (t <= z)
    return t;
  else
    return 2 * z - t;
}
long long query(long long* tree, int a) {
  long long ret = 0;
  while (a) {
    ret += tree[a];
    a -= lowbit(a);
  }
  return ret;
}
void update(long long* tree, int n, int a, long long x) {
  while (a <= n) {
    tree[a] += x;
    a += lowbit(a);
  }
}
int main() {
  int n;
  int i;
  int z, st;
  scanf("%d", &n);
  for (i = 1; i <= n; ++i) {
    scanf("%d", num + i);
    for (z = 0; z < 5; ++z) {
      for (st = 0; st < z * 2 + 2; ++st)
        update(tree[z][st], n, i, num[i] * s(z + 2, st + i));
    }
  }
  int m;
  scanf("%d", &m);
  int l, r, p, v;
  int cmd;
  while (m--) {
    scanf("%d", &cmd);
    if (cmd == 1) {
      scanf("%d%d", &p, &v);
      for (z = 0; z < 5; ++z) {
        for (st = 0; st < z * 2 + 2; ++st) {
          update(tree[z][st], n, p, ((long long)v - num[p]) * s(z + 2, st + p));
        }
      }
      num[p] = v;
    } else {
      scanf("%d%d%d", &l, &r, &z);
      z -= 2;
      st = ((1 - l) % (z * 2 + 2) + (z * 2 + 2)) % (z * 2 + 2);
      printf("%I64d\n", query(tree[z][st], r) - query(tree[z][st], l - 1));
    }
  }
  return 0;
}
