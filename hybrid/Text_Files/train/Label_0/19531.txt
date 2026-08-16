#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  long long int mi = INT_MAX, ma = INT_MIN, gcd, i, j, k, w, d, x, y, x1, y1, p,
                q, r, n, m, root, sum;
  cin >> n >> m;
  long long int a[m];
  for (i = 0; i < m; i++) cin >> a[i];
  long long int ans[n + 2];
  memset(ans, 0, sizeof(ans));
  for (i = 0; i < m - 1; i++) {
    p = min(a[i], a[i + 1]);
    q = max(a[i], a[i + 1]);
    if (p == q) continue;
    ans[0] += (q - p);
    ans[p] -= (q - p);
    ans[p] += (q - 1);
    ans[p + 1] -= (q - 1);
    ans[p + 1] += (q - p - 1);
    ans[q] -= (q - p - 1);
    ans[q] += (p);
    ans[q + 1] -= (p);
    ans[q + 1] += (q - p);
  }
  for (i = 1; i <= n; i++) {
    ans[i] += ans[i - 1];
    cout << ans[i] << " ";
  }
  return 0;
}
