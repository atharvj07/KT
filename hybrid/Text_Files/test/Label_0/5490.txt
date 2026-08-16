#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int x = 0, fu = 0;
  char ch = getchar();
  for (; ch < 48 || ch > 57; ch = getchar()) fu |= (ch == '-');
  for (; ch > 47 && ch < 58; ch = getchar()) x = x * 10 + ch - '0';
  return fu ? -x : x;
}
inline void add(int &x, const int &y) {
  x += y;
  x = x < 1000000007 ? x : x - 1000000007;
}
inline long long gcd(long long a, long long b) {
  return b == 0 ? a : gcd(b, a % b);
}
int n, fa[1000005], f[1000005], dp[1000005], ans;
long long a[1000005];
int main() {
  n = read(), dp[1] = 1;
  for (int i = 1; i <= n; i++) a[i] = read();
  for (int i = 2; i <= n; i++) fa[i] = read();
  for (int i = n; i >= 2; i--) a[fa[i]] += a[i];
  for (int i = n; i >= 1; i--) a[i] = a[1] / gcd(a[1], a[i]);
  for (int i = 1; i <= n; i++) a[i] > n ? 0 : f[a[i]]++;
  for (int i = n; i >= 1; i--)
    for (int j = i << 1; j <= n; j += i) add(f[j], f[i]);
  for (int i = 1; i <= n; i++)
    if (f[i] == i) {
      add(ans, dp[i]);
      for (int j = i << 1; j <= n; j += i) add(dp[j], dp[i]);
    }
  printf("%d\n", ans);
  return 0;
}
