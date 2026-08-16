#include <bits/stdc++.h>
using namespace std;
int main() {
  string s;
  cin >> s;
  string j = s;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] != 'A' && s[i] != 'H' && s[i] != 'O' && s[i] != 'M' &&
        s[i] != 'T' && s[i] != 'X' && s[i] != 'Y' && s[i] != 'I' &&
        s[i] != 'W' && s[i] != 'U' && s[i] != 'V') {
      cout << "NO" << endl;
      return 0;
    }
  }
  reverse(s.begin(), s.end());
  if (s == j)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
}
