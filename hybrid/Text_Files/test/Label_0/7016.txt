#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k, t;
  cin >> n >> k >> t;
  double sum = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j <= k; ++j) {
      double up_bd = (double)(j + (i)*k) * 100 / (n * k);
      double low_bd = (double)(j + (i)*k + 1) * 100 / (n * k);
      if (up_bd <= t && t < low_bd) {
        for (int t = 0; t < i; ++t) cout << k << " ";
        cout << j << " ";
        for (int t = i + 1; t < n; ++t) cout << 0 << " ";
        cout << endl;
        return 0;
      }
    }
  }
  return 0;
}
