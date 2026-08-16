#include <bits/stdc++.h>
using namespace std;
int n;
int mod = 1e9 + 7;
int fa[1000100];
long long s[1000100];
long long f[1000100], h[1000100];
long long gcd(long long a, long long b) {
  if (a % b == 0) return b;
  return gcd(b, a % b);
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) scanf("%lld", &s[i]);
  for (int i = 1; i < n; ++i) {
    scanf("%d", &fa[i]);
  }
  for (int i = n - 1; i >= 1; --i) {
    s[fa[i]] += s[i + 1];
  }
  long long g;
  for (int i = 1; i <= n; ++i) {
    g = s[1] / gcd(s[1], s[i]);
    if (g <= n) f[g]++;
  }
  for (int i = n / 2; i >= 1; --i) {
    for (int j = i + i; j <= n; j += i) (f[j] += f[i]) %= mod;
  }
  h[1] = 1;
  long long ans = 0;
  for (int i = 1; i <= n; ++i) {
    if (f[i] != i) {
      h[i] = 0;
      continue;
    }
    for (int j = i + i; j <= n; j += i) {
      (h[j] += h[i]) %= mod;
    }
    (ans += h[i]) %= mod;
  }
  printf("%lld\n", ans);
}
