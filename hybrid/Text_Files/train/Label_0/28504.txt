#include <bits/stdc++.h>
using namespace std;
long long ex_gcd(long long a, long long b) {
  return b == 0 ? a : ex_gcd(b, a % b);
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  while (t--) {
    long long a, b, k, x, y;
    cin >> x >> y >> k;
    a = min(x, y), b = max(x, y);
    long long xh = a * b / ex_gcd(a, b);
    long long t1 = xh / b, t2 = ceil((xh / a - 1) * 1.0 / t1);
    if (k > t2)
      cout << "OBEY" << endl;
    else
      cout << "REBEL" << endl;
  }
  return 0;
}
