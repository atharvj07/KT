#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
long long n, m, power[400010], H1[400010], H2[2010];
char c, table[210][2010];
long long get_hash(int len, int rin) {
  int l = len * m + 1, r = (rin + 1) * m;
  return (H1[r] - H1[l - 1] * power[r - l + 1] % mod + mod) % mod;
}
int main() {
  scanf("%lld%lld", &n, &m);
  power[0] = 1;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf(" %c", &c);
      H1[i * m + j + 1] = (H1[i * m + j] * 26 + (c - 'a')) % mod;
      power[i * m + j + 1] = (power[i * m + j] * 26) % mod;
    }
  }
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) scanf(" %c", &table[i][j]);
  }
  for (int i = 0; i <= n - m; i++) {
    for (int j = 0; j < m; j++) {
      for (int k = i; k < i + m; k++)
        H2[i] = (H2[i] * 26 + (table[j][k] - 'a')) % mod;
    }
  }
  for (int i = 0; i <= n - m; i++) {
    long long hash = get_hash(i, i + m - 1);
    for (int j = 0; j <= n - m; j++) {
      if (hash == H2[j]) return !printf("%d %d\n", i + 1, j + 1);
    }
  }
}
