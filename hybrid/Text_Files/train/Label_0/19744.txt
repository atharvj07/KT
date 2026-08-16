#include <bits/stdc++.h>
using namespace std;
int n, a[111];
bool u[111];
bool pr(int x) {
  int y = -1, z = -1;
  for (int i = x; i < n; ++i)
    if (!u[i]) {
      y = a[i];
      break;
    }
  for (int i = x; i >= 0; --i)
    if (!u[i]) {
      z = a[i];
      break;
    }
  if (y < 0 || z < 0)
    return 0;
  else
    return abs(y - z) > 1;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    if (i > 0)
      if (abs(a[i] - a[i - 1]) > 1) return cout << "NO", 0;
  }
  for (int i = 0; i < n; ++i) {
    int mx = 0, mi;
    for (int j = 0; j < n; ++j)
      if (a[j] > mx && !u[j]) {
        mx = a[j];
        mi = j;
      }
    u[mi] = 1;
    if (pr(mi)) return cout << "NO", 0;
  }
  cout << "YES";
  return 0;
}
