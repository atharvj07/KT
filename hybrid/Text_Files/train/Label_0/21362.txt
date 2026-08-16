#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10;
long long a[N * 2];
long long sum[N * 2];
int main() {
  ios::sync_with_stdio(false);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    a[i + n] = a[i];
  }
  sum[1] = a[1];
  for (int i = 2; i <= n * 2; i++) sum[i] = sum[i - 2] + a[i];
  long long ans = 0;
  for (int i = n + 1; i <= 2 * n; i++) ans = max(ans, sum[i] - sum[i - n - 1]);
  cout << ans;
  return 0;
}
