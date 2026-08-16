#include <bits/stdc++.h>
using namespace std;
void solve() {
  int n, min;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; i++) cin >> a[i];
  sort(a, a + n, greater<int>());
  min = a[0] - a[1];
  for (int i = 0; i < n - 1; i++)
    if (a[i] - a[i + 1] < min) min = a[i] - a[i + 1];
  cout << min << endl;
}
int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
