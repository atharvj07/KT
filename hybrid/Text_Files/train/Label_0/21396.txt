#include <bits/stdc++.h>
using namespace std;
int main() {
  string s1, s2;
  cin >> s1 >> s2;
  int idx = 0, len1 = s1.size(), len2 = s2.size();
  while (idx < len1 && s1[idx] == '0') idx++;
  s1 = s1.substr(idx);
  idx = 0;
  while (idx < len2 && s2[idx] == '0') idx++;
  s2 = s2.substr(idx);
  if (s1.size() > s2.size())
    cout << ">\n";
  else if (s1.size() < s2.size())
    cout << "<\n";
  else {
    reverse(s1.begin(), s1.end());
    reverse(s2.begin(), s2.end());
    idx = s1.size() - 1;
    while (idx >= 0 && s1[idx] == s2[idx]) idx--;
    if (idx < 0)
      cout << "=\n";
    else if (s1[idx] < s2[idx])
      cout << "<\n";
    else
      cout << ">\n";
  }
  return 0;
}
