#include <bits/stdc++.h>
using namespace std;
long long int n, l, a[107];
int main() {
  cin >> n >> l;
  long long int maxn = 0;
  for (long long int i = 0; i < n; ++i) {
    cin >> a[i];
    maxn = max(a[i], maxn);
  }
  long long int ans = 0;
  for (long long int i = l; i <= maxn; ++i) {
    long long int res = 0;
    for (long long int j = 0; j < n; ++j) res += a[j] / i;
    ans = max(ans, res * i);
  }
  cout << ans << endl;
  return 0;
}
