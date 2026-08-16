#include <bits/stdc++.h>
using namespace std;
long long n, ans, r, a[1000 * 102], b[1000 * 102], c[1000 * 102];
vector<long long> v[10];
signed main() {
  for (long long i = 0; i < 3; i++) cin >> a[i];
  for (long long i = 0; i < 3; i++) cin >> b[i];
  cin >> n;
  for (long long i = 0; i < n; i++) cin >> c[i];
  for (long long i = 0; i < n; i++) {
    ans = c[i];
    for (long long j = 0; j < 3; j++) {
      (v[j].size()) >= a[j] ? ans = max(v[j][v[j].size() - a[j]] + b[j], ans)
                            : ans = ans;
      v[j].push_back(ans);
      ans += b[j];
    }
    r = max(r, ans - c[i]);
  }
  cout << r << endl;
}
