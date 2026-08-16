#include <bits/stdc++.h>
using namespace std;
const int N = 200 * 1000 + 555;
int n, k, a[N];
int main() {
  cin >> n >> k;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  sort(a, a + n);
  a[n++] = int(2e9);
  int ans = 0, u = 0;
  for (int i = 0; i < n - 1; i++) {
    while (u < n && a[i] == a[u]) u++;
    if (a[u] - a[i] > k) ans++;
  }
  cout << ans << endl;
  return 0;
}
