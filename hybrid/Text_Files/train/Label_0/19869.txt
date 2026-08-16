#include <bits/stdc++.h>
using namespace std;
char c[10] = {'a', 'e', 'i', 'o', 'u', 'y'};
int main() {
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  int n;
  cin >> n;
  string s;
  cin >> s;
  string ans;
  bool t = 0;
  for (int i = 0; i < s.size(); i++) {
    bool is = 0;
    for (int j = 0; j < 6; j++) {
      if (s[i] == c[j]) is = 1;
    }
    if (is == 1 && t == 0) {
      t = 1;
      ans += s[i];
    } else if (is == 0 && t == 1) {
      t = 0;
      ans += s[i];
    } else if (is == 0 && t == 0) {
      ans += s[i];
    }
  }
  cout << ans << '\n';
  return 0;
}
