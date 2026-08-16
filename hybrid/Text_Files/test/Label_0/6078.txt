#include <bits/stdc++.h>
using namespace std;
const int N = 200010;
long long i, j, n, m, k, a[N], s, r, ss;
int main() {
  cin >> n >> m;
  for (i = 0; i < n; i++) cin >> a[i];
  s = 0, r = 1;
  for (i = n - 1; i >= 0; i--, r *= m) s = s + r * a[i];
  cin >> n >> m;
  for (i = 0; i < n; i++) cin >> a[i];
  ss = 0, r = 1;
  for (i = n - 1; i >= 0; i--, r *= m) ss = ss + r * a[i];
  if (ss < s)
    cout << '>';
  else if (ss > s)
    cout << '<';
  else
    cout << '=';
  return 0;
}
