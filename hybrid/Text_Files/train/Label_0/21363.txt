#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  long long p[n];
  for (int q = 0; q < n; q++) cin >> p[q];
  long long prefsum[n];
  long long prefct[n];
  long long suffsum[n];
  long long suffct[n];
  prefsum[0] = 0;
  prefct[0] = 0;
  for (int q = 1; q < n; q++) {
    prefct[q] = prefct[q - 1];
    prefsum[q] = prefsum[q - 1];
    if (q % m == 1 || m == 1) {
      prefsum[q] += p[q - 1];
      prefct[q]++;
    }
  }
  suffsum[n - 1] = 0;
  suffct[n - 1] = 0;
  for (int q = n - 2; q >= 0; q--) {
    suffct[q] = suffct[q + 1];
    suffsum[q] = suffsum[q + 1];
    if ((n - 1 - q) % m == 1 || m == 1) {
      suffsum[q] += p[q + 1];
      suffct[q]++;
    }
  }
  long long ans = LLONG_MAX;
  for (int q = 0; q < n; q++) {
    long long tot =
        prefct[q] * p[q] - prefsum[q] + suffsum[q] - suffct[q] * p[q];
    ans = min(ans, tot * 2);
  }
  cout << ans << "\n";
  return 0;
}
