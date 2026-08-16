#include <bits/stdc++.h>
using namespace std;
const long long maxn = 3e5 + 10;
long long N, R, arr[maxn], T;
signed main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> T;
  while (T--) {
    cin >> N >> R;
    for (register long long i = 1; i <= N; ++i) {
      cin >> arr[i];
    }
    sort(arr + 1, arr + 1 + N);
    N = unique(arr + 1, arr + 1 + N) - arr - 1;
    long long sum = 0, ans = 0;
    for (long long i = N; i >= 1; --i) {
      if (arr[i] - sum <= 0) {
        break;
      }
      ++ans;
      sum += R;
    }
    cout << ans << endl;
  }
  return 0;
}
