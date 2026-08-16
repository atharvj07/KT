#include <bits/stdc++.h>
using namespace std;
const int N = 1.25e5 + 10, md = 998244353, G = 3;
char s[N], t[N];
int n, m;
vector<int> rev;
vector<int> w[25];
int c[6][6][N];
int fa[6];
int find(int x) { return fa[x] == x ? x : fa[x] = find(fa[x]); }
void merge(int x, int y) {
  x = find(x), y = find(y);
  if (x == y) return;
  fa[x] = y;
  return;
}
int qpow(int a, int b) {
  int res = 1;
  for (; b; b >>= 1, a = 1ll * a * a % md)
    if (b & 1) res = 1ll * res * a % md;
  return res;
}
void initr(int n, int &lim) {
  for (lim = 1; lim < n; lim <<= 1)
    ;
  rev.resize(lim);
  rev[0] = 0;
  for (int i = 1; i < lim; i++) {
    rev[i] = (rev[i >> 1] >> 1) | ((i & 1) ? lim >> 1 : 0);
  }
  for (int i = 1, k = 2; k <= lim; k <<= 1, i++) {
    w[i].resize(k / 2);
    w[i][0] = 1;
    int g = qpow(G, (md - 1) / k);
    for (int j = 1; j < (k / 2); j++) w[i][j] = 1ll * w[i][j - 1] * g % md;
  }
  return;
}
void FFT(vector<int> &a, int t) {
  int lim = a.size();
  for (int i = 0; i < lim; i++)
    if (i < rev[i]) swap(a[i], a[rev[i]]);
  for (int i = 2, c = 1; i <= lim; i <<= 1, c++) {
    for (int j = 0; j < lim; j += i) {
      for (int k = 0; k < (i >> 1); k++) {
        int x = a[j + k], y = 1ll * a[j + k + (i >> 1)] * w[c][k] % md;
        a[j + k] = (x + y) % md;
        a[j + k + (i >> 1)] = (x - y + md) % md;
      }
    }
  }
  if (t < 0) {
    reverse(a.begin() + 1, a.end());
    int ilm = qpow(lim, md - 2);
    for (int i = 0; i < lim; i++) a[i] = 1ll * a[i] * ilm % md;
  }
  return;
}
void match(char x, char y, int *vis, int lim) {
  vector<int> a(lim), b(lim);
  for (int i = 0; i < n; i++)
    if (s[i] == x) a[i] = 1;
  for (int i = 0; i < m; i++)
    if (t[i] == y) b[i] = 1;
  reverse(b.begin(), b.begin() + m);
  FFT(a, 1), FFT(b, 1);
  for (int i = 0; i < lim; i++) a[i] = 1ll * a[i] * b[i] % md;
  FFT(a, -1);
  for (int i = 0; i < n; i++)
    if (a[i + m - 1]) vis[i] = 1;
  return;
}
int main() {
  scanf("%s", s);
  scanf("%s", t);
  n = strlen(s), m = strlen(t);
  int lim;
  initr(n + m - 1, lim);
  for (char x = 'a'; x <= 'f'; x++) {
    for (char y = 'a'; y <= 'f'; y++) {
      if (x == y) continue;
      match(x, y, c[x - 'a'][y - 'a'], lim);
    }
  }
  for (int i = 0; i < n - m + 1; i++) {
    for (int j = 0; j < 6; j++) fa[j] = j;
    for (int j = 0; j < 6; j++)
      for (int k = 0; k < 6; k++)
        if (c[j][k][i]) merge(j, k);
    int cnt = 0;
    for (int j = 0; j < 6; j++)
      if (fa[j] == j) cnt++;
    printf("%d ", 6 - cnt);
  }
  printf("\n");
  return 0;
}
