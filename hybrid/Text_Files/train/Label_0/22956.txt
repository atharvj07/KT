#include <bits/stdc++.h>
using namespace std;
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const int N = 3e5 + 9;
const long long mod = 1e9 + 7;
int d[N], n;
void solve() {
  for (int i = 1; i <= n; i++) scanf("%d", d + i);
  sort(d + 1, d + n + 1);
  long long sum = 0, ans = 0, p = 2;
  sum = d[1];
  for (int i = 2; i <= n; i++) {
    ans = (ans + d[i] * (p - 1) - sum) % mod;
    sum = (2 * sum + d[i]) % mod;
    p = (p * 2) % mod;
  }
  printf("%lld\n", ans);
}
int main(void) {
  while (cin >> n) solve();
  return 0;
}
