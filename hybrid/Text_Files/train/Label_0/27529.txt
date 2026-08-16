#include <bits/stdc++.h>
using namespace std;
int main() {
  double n, m;
  cin >> n >> m;
  double ans = 1e18;
  for (int i = 0; i < n; i++) {
    double a, b;
    cin >> a >> b;
    ans = min(ans, a / b * m);
  }
  printf("%.6lf\n", ans);
}
