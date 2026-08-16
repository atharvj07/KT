#include <bits/stdc++.h>
const int MAX = 2e5 + 10;
const int MOD = 1e9 + 7;
using namespace std;
int t;
long long n, m;
long long x[5], y[5];
int main() {
  ios::sync_with_stdio(false), cout.tie(NULL);
  cin >> t;
  while (t--) {
    cin >> n >> m;
    long long ans1 = (n * m) / 2, ans2 = (n * m) / 2;
    if ((n + 1) % 2 == 0 && (m + 1) % 2 == 0) ans1++;
    cin >> x[1] >> y[1] >> x[2] >> y[2];
    cin >> x[3] >> y[3] >> x[4] >> y[4];
    long long sz1 = (x[2] - x[1] + 1) * (y[2] - y[1] + 1),
              sz2 = (x[4] - x[3] + 1) * (y[4] - y[3] + 1);
    long long sum1 = sz1 / 2, sum2 = sz2 / 2;
    if (sz1 % 2 == 1 && (x[1] + y[1]) % 2 == 1) sum1++;
    if (sz2 % 2 == 1 && (x[3] + y[3]) % 2 == 0) sum2++;
    long long x1 = max(x[1], x[3]), y1 = max(y[1], y[3]);
    long long x2 = min(x[2], x[4]), y2 = min(y[2], y[4]);
    long long sum = 0, sz;
    if (x2 >= x1 && y2 >= y1) {
      sz = (x2 - x1 + 1) * (y2 - y1 + 1);
      sum = sz / 2;
      if (sz % 2 == 1 && (x1 + y1) % 2 == 1) sum++;
    }
    sum1 -= sum;
    ans1 = ans1 + sum1 - sum2;
    ans2 = ans2 + sum2 - sum1;
    cout << ans1 << " " << ans2 << endl;
  }
}
