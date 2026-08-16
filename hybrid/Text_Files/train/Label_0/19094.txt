#include <bits/stdc++.h>
using namespace std;
const int N = 111111;
int n, m, k, a[N], ans, cnt;
int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; ++i) cin >> a[i];
  a[n + 1] = (int)1e9;
  for (int i = 1; i <= n + 1; ++i) {
    cnt += a[i];
    if (cnt > m) ++ans, cnt = a[i];
  }
  cout << ans;
  return 0;
}
