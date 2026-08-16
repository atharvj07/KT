#include <bits/stdc++.h>
using namespace std;
using lli = long long;
using ld = long double;
inline void Solve() {
  lli n = 0, u = 0;
  cin >> n >> u;
  vector<lli> data(n);
  for (auto &it : data) cin >> it;
  lli p = 0, q = 0;
  for (lli i = 0, k = 0; i < n - 1; i++) {
    while ((k + 1 < n) && (data[k + 1] - data[i] <= u)) k++;
    if (k - i < 2) continue;
    lli j = i + 1;
    lli p1 = data[k] - data[j], q1 = data[k] - data[i];
    if (((p == 0) && (q == 0)) || (p1 * q > p * q1)) {
      p = p1;
      q = q1;
    }
  }
  if ((p == 0) && (q == 0))
    cout << -1;
  else {
    double result = (double)p / q;
    cout << result;
  }
}
signed main() {
  cout << fixed << setprecision(9);
  Solve();
  return 0;
}
