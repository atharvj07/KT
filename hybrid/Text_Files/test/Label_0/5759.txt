#include <bits/stdc++.h>
using namespace std;
long long a, b;
int k;
int mod;
inline int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
const int maxn = 400000;
int d[maxn];
int get(int r1, int r2) {
  assert(r1 <= r2);
  d[r1] = 0;
  int r[k];
  for (int i = 0; i < k; i++) r[i] = r1 % (i + 1);
  for (int i = r1 + 1; i <= r2; i++) {
    for (int j = 0; j < k; j++)
      if (++r[j] == j + 1) r[j] = 0;
    d[i] = d[i - 1] + 1;
    for (int j = 0; j < k; j++) {
      if (r[j] && i - r[j] >= r1) d[i] = min(d[i], d[i - r[j]] + 1);
    }
  }
  return d[r2];
}
long long solve() {
  int ra = a % mod, rb = b % mod;
  if (a - b < mod && ra >= rb) return get(rb, ra);
  long long ans = (get(rb, mod - 1) + 1) + get(0, ra);
  ans += (get(0, mod - 1) + 1) * (((a - ra) - (b - rb + mod)) / mod);
  return ans;
}
int main() {
  while (scanf("%lld"
               "%lld"
               "%d",
               &a, &b, &k) >= 1) {
    mod = 1;
    for (int i = 2; i <= k; i++) mod = mod * i / gcd(i, mod);
    assert(maxn > mod);
    printf(
        "%lld"
        "\n",
        solve());
  }
  return 0;
}
