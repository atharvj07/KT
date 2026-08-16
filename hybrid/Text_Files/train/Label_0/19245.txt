#include <bits/stdc++.h>
using namespace std;
long long int gcd(long long int a, long long int b) {
  if (b != 0)
    return gcd(b, a % b);
  else
    return a;
}
long long int power(long long int a, long long int b) {
  if (b == 0) return 1;
  if (b == 1) return a;
  if (b % 2 == 0) {
    long long int t = power(a, b / 2);
    return t * t;
  } else {
    long long int t = power(a, b / 2);
    return a * t * t;
  }
}
long long int powin(long long int a, long long int b) {
  if (b == 0)
    return 1;
  else if (b == 1)
    return a;
  else if (b % 2 == 0) {
    long long int t = powin(a, b / 2);
    return (t * t) % 1000000007;
  } else {
    long long int t = powin(a, b / 2);
    return (((t * t) % 1000000007) * a) % 1000000007;
  }
}
long long int n, k;
long long int dp[509][10 * 509];
long long int h[20];
void solve() {
  for (long long int i = 1; i < n + 1; i++) {
    for (long long int j = 1; j < k * n + 1; j++) {
      for (long long int p = 1; p < k + 1; p++) {
        if (j >= p) dp[i][j] = max(dp[i][j], dp[i - 1][j - p] + h[p]);
      }
    }
  }
}
long long int fr[100000 + 10];
long long int f[100000 + 10];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> k;
  memset(dp, 0, sizeof dp);
  memset(fr, 0, sizeof fr);
  memset(f, 0, sizeof f);
  for (long long int i = 0; i < n * k; i++) {
    long long int t;
    cin >> t;
    fr[t]++;
  }
  for (long long int i = 0; i < n; i++) {
    int p;
    cin >> p;
    f[p]++;
  }
  h[0] = 0;
  for (long long int i = 1; i < k + 1; i++) {
    cin >> h[i];
    dp[1][i] = h[i];
  }
  solve();
  long long int ans = 0;
  for (long long int i = 1; i < 100000 + 1; i++) {
    ans += dp[f[i]][fr[i]];
  }
  cout << ans << endl;
  return 0;
}
