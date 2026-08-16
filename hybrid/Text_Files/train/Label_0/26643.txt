#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n, d, m, l, X = 0, cur = 0;
  cin >> n >> d >> m >> l;
  bool f = false;
  for (int i = 1; i <= n;) {
    cur = ((X + l) / d) * d;
    cur += d;
    while (cur > X + l && i <= n) X = (i - 1) * m, i++;
    if (cur < X) {
      f = true;
      break;
    }
  }
  if (f)
    cout << cur;
  else {
    X = (n - 1) * m;
    cur = ((X + l) / d) * d;
    cur += d;
    cout << cur;
  }
  return 0;
}
