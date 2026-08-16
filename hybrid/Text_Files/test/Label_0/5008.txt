#include <bits/stdc++.h>
using namespace std;
void spic(string &s, int n) {
  for (int i = 0; i < n; i++) {
    s[i] = (char)tolower(s[i]);
  }
}
int main() {
  int p = 0, b;
  cin >> b;
  string s;
  cin >> s;
  if (b < 26)
    cout << "NO"
         << "\n";
  else {
    int t = 0;
    spic(s, b);
    sort(s.begin(), s.end());
    for (int j = 0; j < b; j++) {
      if (s[j] == 'a' + t) {
        p++;
        t++;
      }
    }
    if (p == 26)
      cout << "YES"
           << "\n";
    else
      cout << "NO"
           << "\n";
  }
}
