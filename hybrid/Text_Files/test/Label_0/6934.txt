#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, s = 0, x1 = 0, x2 = 0, y;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> y;
    s += y;
    if (y % 2 == 0)
      x2++;
    else
      x1++;
  }
  if (s % 2 == 0)
    cout << x2;
  else
    cout << x1;
}
