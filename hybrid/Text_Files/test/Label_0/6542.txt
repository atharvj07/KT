#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n;
  cin >> n;
  long long x[n];
  long long y[n];
  long long sumx = 0;
  long long sumy = 0;
  long long sumx2 = 0;
  long long sumy2 = 0;
  for (int i = 0; i < n; i++) {
    cin >> x[i] >> y[i];
    sumx += x[i];
    sumy += y[i];
    sumx2 += x[i] * x[i];
    sumy2 += y[i] * y[i];
  }
  long long ans = 0;
  for (int i = 0; i < n; i++) {
    ans += (n - 1) * (x[i] * x[i] + y[i] * y[i]) + sumx2 - x[i] * x[i] + sumy2 -
           (y[i] * y[i]);
    ans -= (2 * (x[i] * (sumx - x[i]) + y[i] * (sumy - y[i])));
  }
  cout << ans / 2 << endl;
}
