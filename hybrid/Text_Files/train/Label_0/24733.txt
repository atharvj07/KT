#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-9;
const int mod = (int)1e+9 + 7;
const double pi = acos(-1.);
const int maxn = 100100;
string s, t;
long double check(string s) {
  int g = 0, t = 0, f = 0, c = 0;
  for (unsigned int i = 0; i < s.length(); i++) {
    if (s[i] == 'X')
      t++;
    else if (s[i] == (t & 1 ? 'R' : 'L'))
      g++, t++, f = 0;
    else
      g++, t += 2, c += f, f = !f;
  }
  if (t & 1) t++, c += f;
  if (g * 2 > t) g -= c, t -= c * 2;
  return double(g) / t;
}
int main() {
  {
    srand(time(0));
    const string file = "";
    if (!file.empty()) {
      freopen((file + ".in").c_str(), "r", stdin);
      freopen((file + ".out").c_str(), "w", stdout);
    }
  }
  getline(cin, s);
  int n = s.length();
  for (int i = 0; i < n; i++) {
    if (i && s[i] == s[i - 1] && s[i] != 'X') t += 'X';
    t += s[i];
  }
  long double ans;
  if (s[0] == s[n - 1] && s[0] != 'X') {
    ans = max(check('X' + t), check(t + 'X'));
  } else {
    ans = check(t);
  }
  printf("%.6lf\n", double(floor(ans * 1e8) / 1e6));
  return (0);
}
