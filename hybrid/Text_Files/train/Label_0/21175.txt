#include <bits/stdc++.h>
using namespace std;
int main(void) {
  std::ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  int n;
  cin >> n;
  std::vector<long long> a(n + 1);
  for (int i = 1; i <= n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  std::vector<long long> v(n + 1);
  for (int i = 2; i <= n; i++) v[i] = a[i] - a[i - 1];
  sort(v.begin() + 2, v.begin() + n + 1);
  std::vector<long long> sum(n + 1);
  for (int i = 2; i <= n; i++) sum[i] = sum[i - 1] + v[i];
  int q;
  cin >> q;
  while (q--) {
    long long l, r;
    cin >> l >> r;
    r = r - l + 1;
    int prefix = lower_bound(v.begin(), v.begin() + n + 1, r) - v.begin();
    long long ans = r + sum[prefix - 1] + (n - prefix + 1) * r;
    cout << ans << endl;
  }
  return 0;
}
