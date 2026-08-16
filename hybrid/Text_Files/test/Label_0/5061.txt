#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  double d, h, v, e;
  cin >> d >> h >> v >> e;
  double ans = (3.14159265358979323846 * pow(d, 2) * h) /
               (4 * v - 3.14159265358979323846 * pow(d, 2) * e);
  if (ans < 0)
    cout << "NO\n";
  else {
    cout << "YES\n";
    cout << setprecision(10) << ans << "\n";
  }
  return 0;
}
