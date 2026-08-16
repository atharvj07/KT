#include <bits/stdc++.h>
using namespace std;
int main() {
  int w, m;
  cin >> w >> m;
  while (m > 0) {
    int r = m % w;
    if (r == 0)
      m = m / w;
    else if (r == 1)
      m = (m - 1) / w;
    else if (r == w - 1)
      m = (m + 1) / w;
    else {
      cout << "NO\n";
      return 0;
    }
  }
  cout << "YES\n";
  return 0;
}
