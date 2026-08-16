#include <bits/stdc++.h>
using namespace std;
const int N = 100010;
const int mod = (int)1e9 + 7;
int a[N];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(0);
  int n, i;
  cin >> n;
  for (i = 0; i < n; i++) {
    cin >> a[i];
  }
  int m = (int)1e6;
  int ans = m + 20;
  sort(a, a + n);
  for (i = 0; i < n; i++) {
    if (!i) ans = min(ans, m - a[i]);
    if (i == n - 1)
      ans = min(ans, a[i] - 1);
    else
      ans = min(ans, max(a[i] - 1, m - a[i + 1]));
  }
  cout << ans;
  return 0;
}
