#include <bits/stdc++.h>
using namespace std;
int t;
char s[201];
int main() {
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> s[i];
  }
  int total = 0;
  for (int i = 0; i < t; i++) {
    int x = 0, y = 0;
    for (int k = i; k < t; k++) {
      if (s[k] == 'R') x++;
      if (s[k] == 'L') x--;
      if (s[k] == 'D') y--;
      if (s[k] == 'U') y++;
      if (x == 0 && y == 0) total++;
    }
  }
  cout << total << endl;
}
