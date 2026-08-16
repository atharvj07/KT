#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m, f = 0;
  cin >> n >> m;
  char c;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> c;
      if (c == 'C' || c == 'Y' || c == 'M') {
        f = 1;
      }
    }
  }
  if (f == 1)
    cout << "#Color" << endl;
  else
    cout << "#Black&White" << endl;
  return 0;
}
