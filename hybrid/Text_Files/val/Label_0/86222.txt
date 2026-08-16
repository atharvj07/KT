#include <bits/stdc++.h>
using namespace std;
const int N = 3e5 + 5;
int n1, n2, n3, x, y, ss, tot, last[N], nex[N * 2], to[N * 2];
long long sum, h, ans, ans1, g1, g2, g3, w, s1, s2, s[N], f[N], g[N], f1[N][2];
int read() {
  int x = 0;
  char ch = getchar();
  for (; ch < '0' || ch > '9';) ch = getchar();
  for (; ch >= '0' && ch <= '9'; ch = getchar()) x = x * 10 + ch - '0';
  return x;
}
long long max(long long a, long long b) { return a > b ? a : b; }
void add(int x, int y) {
  to[++tot] = y;
  nex[tot] = last[x];
  last[x] = tot;
}
void dg(int x, int y) {
  s[x] = 1;
  for (int i = last[x]; i; i = nex[i])
    if (to[i] ^ y) {
      dg(to[i], x);
      f[x] += g[to[i]] * s[x] + g[x] * s[to[i]] + s[x] * s[to[i]];
      g[x] += g[to[i]] + s[to[i]];
      s[x] += s[to[i]];
    }
  sum += f[x];
}
void dg1(int x, int y) {
  for (int i = last[x]; i; i = nex[i])
    if (to[i] ^ y) {
      long long g1 = g[x] - g[to[i]] - s[to[i]];
      g[to[i]] += g1 + ss - s[to[i]];
      dg1(to[i], x);
    }
}
void dg2(int x, int y) {
  f1[x][0] = g[x] * s1, f1[x][1] = g[x] * s2;
  for (int i = last[x]; i; i = nex[i])
    if (to[i] ^ y) {
      dg2(to[i], x);
      ans1 = max(ans1, f1[x][0] + f1[to[i]][1] + w);
      ans1 = max(ans1, f1[x][1] + f1[to[i]][0] + w);
      f1[x][0] = max(f1[x][0], f1[to[i]][0] + w);
      f1[x][1] = max(f1[x][1], f1[to[i]][1] + w);
    }
  ans1 = max(ans1, g[x] * (s1 + s2));
}
int main() {
  n1 = read(), n2 = read(), n3 = read();
  for (int i = 1; i < n1; i++) {
    x = read(), y = read();
    add(x, y), add(y, x);
  }
  for (int i = 1; i < n2; i++) {
    x = read() + n1, y = read() + n1;
    add(x, y), add(y, x);
  }
  for (int i = 1; i < n3; i++) {
    x = read() + n1 + n2, y = read() + n1 + n2;
    add(x, y), add(y, x);
  }
  dg(1, 0), dg(n1 + 1, 0), dg(n1 + n2 + 1, 0);
  ss = n1, dg1(1, 0);
  ss = n2, dg1(n1 + 1, 0);
  ss = n3, dg1(n1 + n2 + 1, 0);
  for (int i = 1; i <= n1; i++) g1 = max(g1, g[i]);
  for (int i = n1 + 1; i <= n1 + n2; i++) g2 = max(g2, g[i]);
  for (int i = n1 + n2 + 1; i <= n1 + n2 + n3; i++) g3 = max(g3, g[i]);
  sum += (long long)n1 * n2 + (long long)n1 * n3 + (long long)n2 * n3;
  ans1 = 0, w = (long long)n2 * n3, s1 = n2, s2 = n3;
  dg2(1, 0);
  h = g2 * (n1 + n3) + g3 * (n1 + n2) + (long long)n2 * n3;
  ans = max(ans, sum + ans1 + h);
  ans1 = 0, w = (long long)n1 * n3, s1 = n1, s2 = n3;
  dg2(n1 + 1, 0);
  h = g1 * (n2 + n3) + g3 * (n2 + n1) + (long long)n1 * n3;
  ans = max(ans, sum + ans1 + h);
  ans1 = 0, w = (long long)n1 * n2, s1 = n1, s2 = n2;
  dg2(n1 + n2 + 1, 0);
  h = g2 * (n1 + n3) + g1 * (n3 + n2) + (long long)n1 * n2;
  ans = max(ans, sum + ans1 + h);
  printf("%lld", ans);
  return 0;
}
