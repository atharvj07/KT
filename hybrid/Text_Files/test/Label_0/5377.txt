#include <bits/stdc++.h>
using namespace std;
long long n, m, x, y, s, t, res, ans = -1LL << 60;
long long get(long long t) {
  x = m / t;
  y = m % t;
  return (t - y) * x * x + y * (x + 1) * (x + 1);
}
int main() {
  cin >> n >> m;
  if (!n) {
    cout << -m * m << endl;
    for (int i = 0; i < m; i++) cout << "x";
    return 0;
  }
  for (int i = 0; i < n; i++) {
    res = (n - i) * (n - i) + i - get(i + 2);
    if (res > ans) {
      ans = res;
      s = i;
    }
  }
  cout << ans << endl;
  t = s + 2;
  x = m / t;
  y = m % t;
  for (int j = 0; j < s + 2; j++) {
    if (j)
      if (j > 1)
        cout << "o";
      else
        for (int i = 0; i < n - s; i++) cout << "o";
    for (int i = 0; i < x + (j < y); i++) cout << "x";
  }
  return 0;
}
