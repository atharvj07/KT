#include <bits/stdc++.h>
using namespace std;
int c[200200], C[200200], d[200200];
int n;
int magic = -1;
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> c[i] >> d[i];
  for (int i = 1; i <= n; i++) {
    C[i] = C[i - 1] + c[i - 1];
    if (d[i] == 2) {
      if (magic == -1)
        magic = i;
      else if (C[magic] < C[i])
        magic = i;
    }
  }
  if (magic == -1) {
    cout << "Infinity" << endl;
    return 0;
  }
  int cur = 1899 - C[magic];
  bool flag = true;
  for (int i = 1; i <= n; i++) {
    if (cur < 1900 && d[i] == 1) flag = false;
    if (cur >= 1900 && d[i] == 2) flag = false;
    cur += c[i];
  }
  if (flag)
    cout << cur << endl;
  else
    cout << "Impossible" << endl;
  return 0;
}
