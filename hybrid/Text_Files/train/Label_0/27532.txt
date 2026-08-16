#include <bits/stdc++.h>
using namespace std;
int n, s1, s2, c1, c2;
string s;
int main() {
  cin >> n;
  cin >> s;
  for (int i = 0; i < n / 2; i++) {
    if (s[i] == '?')
      c1++;
    else
      s1 += s[i] - '0';
  }
  for (int i = n / 2; i < n; i++) {
    if (s[i] == '?')
      c2++;
    else
      s2 += s[i] - '0';
  }
  s1 += c1 / 2 * 9;
  s2 += c2 / 2 * 9;
  puts(s1 == s2 ? "Bicarp" : "Monocarp");
  return 0;
}
