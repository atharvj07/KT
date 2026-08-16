#include <bits/stdc++.h>
using namespace std;
int main() {
  double n, a;
  cin >> n >> a;
  cout << 1 << " " << 2 << " ";
  double ans = 1000000;
  double minDiff = 1000000;
  double maxAngle = 180 - 360 / n;
  double stepSize = 180 / n;
  for (int i = 3; i <= n; i++) {
    double angle = maxAngle - stepSize * (i - 3);
    if (fabs(angle - a) < minDiff) {
      minDiff = abs(angle - a);
      ans = i;
    }
  }
  cout << (int)ans;
  return 0;
}
