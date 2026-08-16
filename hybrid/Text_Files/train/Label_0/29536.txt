#include <bits/stdc++.h>
using namespace std;
int n, a[1005];
int gcd(int a, int b) { return !b ? a : gcd(b, a % b); }
int main() {
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  int result = 0;
  for (int i = 0; i < n - 1; ++i) {
    if (gcd(a[i], a[i + 1]) > 1) ++result;
  }
  cout << result << endl;
  for (int i = 0; i < n - 1; ++i) {
    cout << a[i] << " ";
    if (gcd(a[i], a[i + 1]) > 1) cout << 1 << " ";
  }
  cout << a[n - 1] << endl;
  return 0;
}
