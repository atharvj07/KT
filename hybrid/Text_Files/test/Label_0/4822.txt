#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int maxn = 1e5 + 10;
const int mod = 1e9 + 7;
const double eps = 1e-5;
double R, D, x, y, r;
int n;
int main() {
  while (cin >> R >> D >> n) {
    int ans = 0;
    for (int i = 0; i < n; i++) {
      cin >> x >> y >> r;
      double dis = sqrt((x * x) + (y * y)) - r;
      double dis2 = sqrt((x * x) + (y * y)) + r;
      if (dis >= (R - D) && dis2 <= R) ans++;
    }
    cout << ans << endl;
  }
  return 0;
}
