#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  string g, s;
  cin >> g >> s;
  int a[26], flag = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (s.at(i) == '*') flag = 1;
  }
  for (int i = 0; i < 26; ++i) {
    a[i] = 0;
  }
  for (int i = 0; i < g.size(); ++i) {
    a[g.at(i) - 'a'] = 1;
  }
  int n;
  cin >> n;
  for (int k = 0; k < n; k++) {
    string str;
    cin >> str;
    int z = 0, f = 0;
    z = s.size() - str.size();
    int i = 0, j = 0;
    while (i < s.size() && j < str.size()) {
      if (s.at(i) == str.at(j)) {
        i++;
        j++;
      } else if (s.at(i) == '?') {
        if (a[str.at(j) - 'a'] == 1) {
          i++;
          j++;
        } else {
          f = 1;
          break;
        }
      } else if (s.at(i) == '*') {
        if (z == 0) {
          if (a[str.at(j) - 'a'] == 0)
            i++, j++;
          else {
            f = 1;
            break;
          }
        } else if (z == 1) {
          i++;
        } else if (z < 0) {
          z = fabs(z);
          z++;
          while (z--) {
            if (a[str.at(j) - 'a'] == 0)
              j++;
            else {
              f = 1;
              break;
            }
          }
          if (f == 1) break;
          i++;
        } else {
          f = 1;
          break;
        }
      } else {
        f = 1;
        break;
      }
    }
    if (f == 1 || z > 1 || (flag == 0 && z != 0))
      cout << "NO\n";
    else
      cout << "YES\n";
  }
  return 0;
}
