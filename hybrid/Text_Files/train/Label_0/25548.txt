#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  long long n, k;
  cin >> n >> k;
  vector<int> x(n), y(n);
  for (int& xi : x) cin >> xi;
  for (int& yi : y) cin >> yi;
  for (long long i = 0, px = 0, py = 0, qx, qy; i < n; ++i, px = qx, py = qy) {
    qx = max(0LL, x[i] + px - y[i] * k);
    qy = max(0LL, y[i] + py - x[i] * k);
    if (qx > k || qy > k) {
      cout << "NO\n";
      return 0;
    }
  }
  cout << "YES\n";
  return 0;
}
