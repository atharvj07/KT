#include <bits/stdc++.h>
using namespace std;
const long long inf = 2000000000000000000LL;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long t;
  cin >> t;
  while (t--) {
    long long n, m, i, j, k, temp = 0, flag = 0, ans;
    cin >> n;
    long long a[n], sum[n];
    for (i = 0; i < n - 1; i++) {
      cin >> a[i];
      if (!i) {
        sum[i] = a[i];
        ans = a[i];
      } else {
        sum[i] = max(sum[i - 1] + a[i], a[i]);
      }
      temp += a[i];
      ans = max(ans, sum[i]);
    }
    cin >> a[i];
    temp += a[i];
    if (temp <= ans) {
      cout << "NO\n";
      flag++;
    }
    for (i = n - 1, ans = 0; i > 0 && !flag; i--) {
      ans += a[i];
      if (ans >= temp) {
        cout << "NO\n";
        flag++;
      }
    }
    if (!flag) cout << "YES\n";
  }
}
