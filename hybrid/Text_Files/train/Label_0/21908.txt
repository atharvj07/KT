#include <bits/stdc++.h>
using namespace std;
int n, k, ans;
string s;
int main() {
  cin >> n >> k >> s;
  if (k == 2) {
    string sp;
    for (int i = 0; i < n; i++) {
      if (i % 2 == 0)
        sp += 'A';
      else
        sp += 'B';
      if (sp[i] != s[i]) ans++;
    }
    cout << min(ans, n - ans) << endl;
    if (ans <= n - ans)
      cout << sp << endl;
    else
      for (int i = 0; i < n; i++) {
        if (i % 2 == 1)
          cout << "A";
        else
          cout << "B";
      }
    cout << endl;
    return 0;
  }
  for (int i = 1; i < n; i++) {
    if (s[i] == s[i - 1]) {
      ans++;
      if (s[i] == 'A') {
        if (i < n - 1 && s[i + 1] != 'B')
          s[i] = 'B';
        else
          s[i] = 'C';
      } else {
        if (i < n - 1 && s[i + 1] != 'A')
          s[i] = 'A';
        else {
          if (s[i] == 'B')
            s[i] = 'C';
          else
            s[i] = 'B';
        }
      }
    }
  }
  cout << ans << endl << s << endl;
  return 0;
}
