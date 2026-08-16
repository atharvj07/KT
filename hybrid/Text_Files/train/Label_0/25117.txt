#include <bits/stdc++.h>
using namespace std;
bool isPalindrom(string s) {
  for (int i = 0; i < s.size() / 2; ++i)
    if (s[i] != s[s.size() - 1 - i]) {
      return false;
    }
  return true;
}
int main() {
  string s;
  cin >> s;
  if (isPalindrom(s)) {
    if (s.size() % 2 == 0)
      cout << "NO";
    else
      cout << "YES";
    return 0;
  }
  for (int i = 0; i < s.size(); ++i) {
    char temp = s[i];
    s[i] = s[s.size() - 1 - i];
    if (isPalindrom(s)) {
      cout << "YES";
      return 0;
    }
    s[i] = temp;
  }
  cout << "NO";
}
