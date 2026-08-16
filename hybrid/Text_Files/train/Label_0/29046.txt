#include <bits/stdc++.h>
using namespace std;
long long k, ans;
string s, s1;
int main() {
  cin >> s >> s1;
  for (int i = 0; i < s.size(); i++)
    if (s[i] == s1[i]) ans++;
  if ((s.size() - ans) % 2 == 1) {
    cout << "impossible";
    return 0;
  }
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == s1[i]) cout << s[i];
    if (s[i] != s1[i]) {
      if (k == 1) {
        cout << s1[i];
        k = 0;
      } else {
        cout << s[i];
        k = 1;
      }
    }
  }
}
