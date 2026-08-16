#include <bits/stdc++.h>
using namespace std;
string s;
int m = 0, l = 1;
void rd(int &);
void wrt(int);
int main() {
  cin >> s;
  s += s;
  s += s[s.size() - 1];
  for (int i = 1; i <= (s.size() - 1); ++i)
    if (s[i - 1] != s[i])
      ++l;
    else
      m = max(m, l), l = 1;
  m = min(m, (int)s.size() / 2);
  cout << m;
  return 0;
}
void rd(int &x) {
  static int s, c;
  x = 0;
  s = 1;
  c = getchar();
  while (c != '-' && (c < 48 || 57 < c)) c = getchar();
  if (c == '-') s = -1, c = getchar();
  while (47 < c && c < 58) x = (x << 3) + (x << 1) + c - 48, c = getchar();
  x = s * x;
}
void wrt(int x) {
  if (x < 0) {
    putchar('-');
    x = -x;
  }
  static int y, cc;
  y = cc = 0;
  while (x && x % 10 == 0) ++cc, x /= 10;
  while (x > 9) y = y * 10 + x % 10, x /= 10;
  putchar(x + 48);
  while (y) putchar(y % 10 + 48), y /= 10;
  while (cc--) putchar(48);
}
