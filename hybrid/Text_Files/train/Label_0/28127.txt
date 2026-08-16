#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-9;
const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const int W = 0, B = 1, R = 2, Y = 3;
const int N = 8;
const int mod = 1000000007;
const int inv = 500000004;
int l, r;
int mtx[N][N], a[N][N];
int st[4][4], ts[N];
bool check(int i, int j) {
  if (i == j) return false;
  if (j == W && i == Y) return false;
  if (j == Y && i == W) return false;
  if (j == R && i == B) return false;
  if (j == B && i == R) return false;
  return true;
}
void init() {
  int tot = 0;
  memset(st, -1, sizeof(st));
  for (int i = 0; i < (int)(4); ++i)
    for (int j = 0; j < (int)(4); ++j)
      if (check(i, j)) {
        st[i][j] = tot;
        ts[tot++] = i * 4 + j;
      }
  memset(mtx, 0, sizeof(mtx));
  for (int i = 0; i < (int)(N); ++i)
    for (int k = 0; k < (int)(4); ++k) {
      int a = ts[i] / 4;
      int b = ts[i] % 4;
      if (!check(b, k)) continue;
      if (a == B && b == W && k == R) continue;
      if (a == R && b == W && k == B) continue;
      mtx[i][st[b][k]] = 1;
    }
}
void add(int dst[][N], int a[][N], int b[][N]) {
  int c[N][N];
  for (int i = 0; i < (int)(N); ++i)
    for (int j = 0; j < (int)(N); ++j) c[i][j] = (a[i][j] + b[i][j]) % mod;
  memcpy(dst, c, sizeof(c));
}
void mult(int dst[][N], int a[][N], int b[][N]) {
  int c[N][N];
  memset(c, 0, sizeof(c));
  for (int i = 0; i < (int)(N); ++i)
    for (int j = 0; j < (int)(N); ++j)
      for (int k = 0; k < (int)(N); ++k)
        c[i][j] = (c[i][j] + (long long)a[i][k] * b[k][j]) % mod;
  memcpy(dst, c, sizeof(c));
}
void power(int dst[][N], int a[][N], int k) {
  int r[N][N], t[N][N];
  memset(r, 0, sizeof(r));
  memcpy(t, a, sizeof(t));
  for (int i = 0; i < (int)(N); ++i) r[i][i] = 1;
  while (k) {
    if (k & 1) mult(r, t, r);
    mult(t, t, t);
    k >>= 1;
  }
  memcpy(dst, r, sizeof(r));
}
void calc(int dst[][N], int a[][N], int k) {
  if (k == 1) {
    memcpy(dst, a, sizeof(int) * N * N);
    return;
  }
  int x[N][N], y[N][N];
  power(x, a, k / 2);
  calc(y, a, k / 2);
  for (int i = 0; i < (int)(N); ++i) x[i][i]++;
  mult(dst, x, y);
  if (k & 1) {
    power(x, a, k);
    add(dst, dst, x);
  }
}
int f(int n) {
  if (n == 2) return 8;
  int a[N][N], ans = 8;
  calc(a, mtx, n - 2);
  for (int i = 0; i < (int)(N); ++i)
    for (int j = 0; j < (int)(N); ++j) ans = (ans + a[i][j]) % mod;
  return ans;
}
int gao(int n) {
  if (n == 0) return 0;
  if (n == 1) return 4;
  if (n == 2) return 8;
  int ans = f(n) + f((n + 1) / 2);
  ans = (long long)ans * inv % mod;
  return (ans % mod + mod + 4) % mod;
}
void solve() {
  long long ans = gao(r) - gao(l - 1);
  ans = (ans % mod + mod) % mod;
  printf("%d\n", (int)ans);
}
int main() {
  init();
  while (scanf("%d%d", &l, &r) != EOF) {
    solve();
  }
  return 0;
}
