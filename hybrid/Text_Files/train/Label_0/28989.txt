#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int n, a, d;
int t[100005], v[100005];
double ans[100005];
int main() {
  cin.tie(0);
  cin >> n >> a >> d;
  for (int i = 1; i <= n; i++) cin >> t[i] >> v[i];
  ans[0] = 0;
  for (int i = 1; i <= n; i++) {
    double tt = 1.0 * v[i] / a;
    double dd = 0.5 * a * tt * tt, res = -1;
    if (dd < d) {
      res = tt + (d - dd) / v[i];
    } else {
      res = sqrt(2.0 * d / a);
    }
    ans[i] = res + t[i];
    ans[i] = max(ans[i], ans[i - 1]);
    cout << fixed << setprecision(10) << ans[i] << endl;
  }
  return 0;
}
