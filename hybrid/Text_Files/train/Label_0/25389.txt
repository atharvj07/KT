#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0), cout.tie(0);
  int n, cnt = 0, i;
  cin >> n;
  string ans[200000], s;
  while (n--) {
    cin >> s;
    if (s == "pwd") {
      cout << "/";
      for (i = 0; i < cnt; i++) {
        cout << ans[i] << "/";
      }
      cout << endl;
    } else {
      cin >> s;
      string x, y;
      if (s[0] == '/')
        cnt = 0, i = 1;
      else
        i = 0;
      for (; i < s.size(); i++) {
        if (s[i] != '/') {
          x += s[i];
        }
        if (s[i] == '/' || i == s.size() - 1) {
          if (x == "..")
            cnt = max(0, cnt - 1);
          else
            ans[cnt++] = x;
          x = "";
        }
      }
    }
  }
}
