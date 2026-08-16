#include <bits/stdc++.h>
using namespace std;
int f, w, h;
const int mod = 1e9 + 7;
int ac, all;
int fastpow(int x, int a) {
  int ret = 1;
  while (a) {
    if (a & 1) ret = 1LL * ret * x % mod;
    x = x * 1LL * x % mod;
    a >>= 1;
  }
  return ret;
}
struct Combin {
  int fac[200005], rv[200005], facrv[200005];
  Combin() {
    fac[0] = rv[1] = facrv[0] = 1;
    for (int i = 2; i < 200005; i++)
      rv[i] = ((-(long long)(mod / i) * rv[mod % i] % mod) + mod) % mod;
    for (int i = 1; i < 200005; i++) fac[i] = (long long)fac[i - 1] * i % mod;
    for (int i = 1; i < 200005; i++)
      facrv[i] = (long long)facrv[i - 1] * rv[i] % mod;
  }
  int C(int r1, int n1) {
    if (r1 > n1) return 0;
    return fac[n1] * (long long)facrv[r1] % mod * facrv[n1 - r1] % mod;
  }
} mc;
int main() {
  scanf("%d%d%d", &f, &w, &h);
  if (w == 0) return puts("1"), 0;
  if (f == 0) return (w <= h ? puts("0") : puts("1")), 0;
  int mx = f + w;
  for (int i = 2; i <= mx; i++) {
    if (i / 2 <= f && (i + 1) / 2 <= w) {
      int nf = i / 2, nw = (i + 1) / 2;
      (all += mc.C(nf - 1, f - 1) * 1LL * mc.C(nw - 1, w - 1) % mod) %= mod;
      if (w >= (h + 1) * (long long)nw)
        (ac +=
         mc.C(nf - 1, f - 1) * 1LL * mc.C(nw - 1, w - h * nw - 1) % mod) %= mod;
    }
    if (i / 2 <= w && (i + 1) / 2 <= f) {
      int nf = (i + 1) / 2, nw = i / 2;
      (all += mc.C(nf - 1, f - 1) * 1LL * mc.C(nw - 1, w - 1) % mod) %= mod;
      if (w >= (h + 1) * (long long)nw)
        (ac +=
         mc.C(nf - 1, f - 1) * 1LL * mc.C(nw - 1, w - h * nw - 1) % mod) %= mod;
    }
  }
  int ans = 1LL * ac * fastpow(all, mod - 2) % mod;
  cout << ans << endl;
  return 0;
}
