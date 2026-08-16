#include <bits/stdc++.h>
using namespace std;
const long long N = 100005;
long long a[N], cnt[N];
signed main() {
  long long T, n;
  cin >> T;
  while (T--) {
    cin >> n;
    for (long long i = 1; i <= n; ++i) cin >> a[i];
    sort(a + 1, a + n + 1);
    long long tmp1 = -1e18, tmp2 = 1;
    for (long long st = 0; st <= 5; ++st) {
      tmp2 = 1;
      for (long long j = n; j >= n - 4 + st; --j) tmp2 *= a[j];
      for (long long j = 1; j <= st; ++j) tmp2 *= a[j];
      tmp1 = max(tmp1, tmp2);
    }
    cout << tmp1 << endl;
  }
  return 0;
}
