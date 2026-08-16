#include <bits/stdc++.h>
using namespace std;
int main() {
  string s, a, d, b;
  bool fnd = false;
  cin >> s;
  int i = 0;
  for (; s[i] != '.' and s[i] != 'e'; i++) a += s[i];
  if (s[i] == '.') {
    fnd = true;
    for (i += 1; s[i] != 'e'; i++) d += s[i];
  }
  for (i += 1; i < s.length(); i++) b += s[i];
  int bt = atoi(b.c_str());
  if (!fnd) {
    while (bt--) {
      a += "0";
    }
    cout << a << endl;
  } else {
    if (bt < d.length())
      d.insert(bt, ".");
    else {
      string add = "";
      int diff = bt - d.length();
      while (diff > 0) {
        add += '0';
        diff--;
      }
      d += add;
    }
    if (d == ".0")
      cout << a;
    else {
      string f = a + d;
      if (f[f.length() - 1] == '.') f.erase(f[f.length() - 1], 1);
      cout << f << endl;
    }
  }
}
