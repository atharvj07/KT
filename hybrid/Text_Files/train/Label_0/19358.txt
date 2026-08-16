#include <bits/stdc++.h>
using namespace std;
pair<long long, int> dist[400000];
long long sum[400000];
long long ans[400000];
int main() {
  int n, k;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    long long t;
    cin >> t;
    dist[i] = pair<long long, int>(t, i);
  }
  cin >> k;
  sort(dist + 1, dist + 1 + n);
  for (int i = 1; i <= n; i++) sum[i] = sum[i - 1] + dist[i].first;
  long long t = 0;
  for (int i = 1; i <= k; i++) t = t + (i - 1) * dist[i].first - sum[i - 1];
  long long ans = t;
  int s = 1;
  for (int i = k + 1; i <= n; i++) {
    t = t - 2 * (sum[i - 1] - sum[i - k + 1] + dist[i - k + 1].first) +
        (k - 1) * (dist[i].first + dist[i - k].first);
    if (t < ans) {
      s = i - k + 1;
      ans = t;
    }
  }
  for (int i = 0; i < k; i++) {
    cout << dist[s + i].second << " ";
  }
  return 0;
}
