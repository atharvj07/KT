#include <bits/stdc++.h>
using namespace std;
int i, j, d, p, q, x[4] = {1, 1, 0, -1}, y[4] = {0, 1, 1, 1};
string s[12];
int main() {
  s[0] = s[11] = "OOOOOOO";
  for (i = 1; i <= 10; i++) cin >> s[i], s[i] = "O" + s[i] + "O";
  for (i = 1; i <= 10; i++)
    for (j = 1; j <= 10; j++)
      if (s[i][j] == '.')
        for (d = 0; d < 4; d++) {
          for (p = 1; s[i + p * y[d]][j + p * x[d]] == 'X'; p++)
            ;
          for (q = 1; s[i - q * y[d]][j - q * x[d]] == 'X'; q++)
            ;
          if (p + q > 5) return cout << "YES", 0;
        }
  cout << "NO";
}
