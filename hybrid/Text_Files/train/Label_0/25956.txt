#include <bits/stdc++.h>
using namespace std;
const int N = 202;
int n, m, k, p, q, ans, sum, tot, cnt, a[N], b[N], minn = 1e9;
int main() {
  cin >> n >> k;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    tot = max(tot, a[i]);
    minn = min(a[i], minn);
  }
  if (tot < k) {
    cout << 0 << endl;
    return 0;
  }
  for (int i = k; i <= tot; i++) {
    sum = 0;
    for (int j = 1; j <= n; j++) {
      sum += a[j] / i;
    }
    ans = max(ans, sum * i);
  }
  cout << ans;
  return 0;
}
