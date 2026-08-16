#include <bits/stdc++.h>
using namespace std;
const long long N = 4e5 + 7;
long long ans[N], be[N];
int32_t main() {
  ios_base::sync_with_stdio(0);
  long long n, m;
  cin >> n >> m;
  for (long long i = 0; i < n; i++) {
    cin >> be[i];
  }
  sort(be, be + n);
  vector<long long> vec;
  for (long long i = 0; i < m; i++) {
    long long x1, x2, y;
    cin >> x1 >> x2 >> y;
    if (x1 == 1) {
      vec.push_back(x2);
    }
  }
  long long ans = 1e9;
  be[n] = 1e9;
  long long ks = 0;
  n++;
  sort(vec.begin(), vec.end());
  for (long long i = 0; i < n; i++) {
    while (ks < vec.size() && vec[ks] < be[i]) ks++;
    ans = min(ans, i + (long long)(vec.size() - ks));
  }
  cout << ans;
}
