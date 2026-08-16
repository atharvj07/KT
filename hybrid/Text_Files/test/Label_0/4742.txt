#include <bits/stdc++.h>
#define LL long long
using namespace std;
const int N = 500005;
const int mod = 998244353;

int n, m, ans, fac[N], inv[N];

inline int C(int x, int y) {
  if (x < 0 || y < 0 || x < y) {
    return 0;
  }
  return 1LL * fac[x] * inv[y] % mod * inv[x - y] % mod;
}

int main() {
  scanf("%d%d",&n,&m);
  fac[0] = fac[1] = inv[0] = inv[1] = 1;
  for (int i = 2; i <= m; ++i) {
    fac[i] = 1LL * fac[i - 1] * i % mod;
    inv[i] = 1LL * (mod - mod / i) * inv[mod % i] % mod;
  }
  for (int i = 2; i <= m; ++i) {
    inv[i] = 1LL * inv[i - 1] * inv[i] % mod;
  }
  for (int i = n; i <= m; ++i) {
    ans = (ans + C(m, i)) % mod;
    ans = (ans - C(m, i * 2 - n + 1) + mod) % mod;
  }
  printf("%d\n", ans);
  return 0;
}