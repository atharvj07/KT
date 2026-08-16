#include <bits/stdc++.h>
using namespace std;
inline bool cmin(int &x, int y) { return x > y ? x = y, 1 : 0; }
inline bool cmax(int &x, int y) { return x < y ? x = y, 1 : 0; }
const int _ = 5055, mod = 998244353;
int N, fac[_], inv[_];
int f[_][_];
int ans[_];
inline int dec(int x) { return x >= mod ? x - mod : x; }
inline int Pow(int x, int y = mod - 2) {
  int ans(1);
  for (; y; y >>= 1, x = (long long)x * x % mod)
    if (y & 1) ans = (long long)ans * x % mod;
  return ans;
}
int main() {
  cin >> N;
  fac[0] = fac[1] = inv[0] = 1;
  for (int i = 2, I = N; i <= I; ++i) fac[i] = 1ll * fac[i - 1] * i % mod;
  inv[N] = Pow(fac[N]);
  for (int i = N, I = 2; i >= I; --i) inv[i - 1] = 1ll * inv[i] * i % mod;
  f[0][0] = 1;
  for (int i = 1, I = N; i <= I; ++i)
    for (int j = 1, I = i; j <= I; ++j)
      f[i][j] =
          (1ll * f[i - 1][j] * j + 1ll * f[i - 1][j - 1] * (i - j + 1)) % mod;
  for (int i = 1, I = N; i <= I; ++i)
    for (int j = 1, I = N; j <= I; ++j)
      ans[j] = (ans[j] + 1ll * f[i][j] * inv[i]) % mod;
  for (int i = 1, I = N; i <= I; ++i)
    cout << 1ll * ans[i] * fac[N] % mod << " ";
  return 0;
}
