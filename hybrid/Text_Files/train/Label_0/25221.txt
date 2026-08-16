#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int a, b, c, d, k;
    cin >> a >> b >> c >> d >> k;
    int sum1, sum2;
    sum1 = (a - 1) / c + 1;
    sum2 = (b - 1) / d + 1;
    if (sum1 + sum2 > k)
      cout << "-1" << endl;
    else
      cout << sum1 << " " << sum2 << endl;
  }
  return 0;
}
