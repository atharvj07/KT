#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  string s;
  cin >> n >> s;
  int a, c, g, t, q;
  a = c = g = t = q = 0;
  int m;
  if (n % 4 == 0) {
    for (int i = 0; i < n; i++) {
      if (s[i] == 'A')
        a++;
      else if (s[i] == 'C')
        c++;
      else if (s[i] == 'G')
        g++;
      else if (s[i] == 'T')
        t++;
      else
        q++;
    }
    m = n / 4;
    a = abs(m - a);
    c = abs(m - c);
    g = abs(m - g);
    t = abs(m - t);
    if ((a + c + g + t) != q) {
      cout << "===";
    } else {
      for (int i = 0; i < n; i++) {
        if (s[i] == '?') {
          if (a != 0) {
            s[i] = 'A';
            a--;
          } else if (c != 0) {
            s[i] = 'C';
            c--;
          } else if (g != 0) {
            s[i] = 'G';
            g--;
          } else {
            s[i] = 'T';
            t--;
          }
        }
      }
      cout << s;
    }
  } else {
    cout << "===";
  }
  return 0;
}
