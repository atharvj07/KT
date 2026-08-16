#include <bits/stdc++.h>
using namespace std;
int main() {
  string s;
  cin >> s;
  int i;
  for (i = (0); i < ((s).size()); i++)
    if (s[i] == ':') s[i] = ' ';
  stringstream ss;
  ss << s;
  int h, m;
  ss >> h >> m;
  h = h % 12;
  m = m % 60;
  double x, y;
  x = h * 30.0 + m * 0.5;
  y = m * 6.0;
  cout << x << " " << y << "\n";
  return 0;
}
