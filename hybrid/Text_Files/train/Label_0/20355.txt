#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, a, b, c, d, i;
  long long int ans = 0;
  cin >> n >> a >> b >> c >> d;
  swap(c, d);
  for (i = 1; i <= n; i++) {
    if ((i + c - a) >= 1 && (i + c - a) <= n && (i + c - a - d + b) >= 1 &&
        (i + c - a - d + b) <= n && (i - d + b) >= 1 && (i - d + b) <= n)
      ans = ans + n;
  }
  cout << ans << endl;
  return 0;
}
