#include <bits/stdc++.h>
using namespace std;
string func(int c4, int c7) {
  string res;
  while (c4--) res += '4';
  while (c7--) res += '7';
  return res;
}
int main() {
  string s;
  while (cin >> s) {
    int n = s.size();
    if (n % 2 == 1) {
      cout << string((n + 1) / 2, '4') << string((n + 1) / 2, '7') << endl;
      continue;
    }
    string t = string(n / 2, '7') + string(n / 2, '4');
    if (t < s) {
      cout << string(n / 2 + 1, '4') << string(n / 2 + 1, '7') << endl;
      continue;
    }
    int c4 = n / 2, c7 = n / 2;
    string res;
    for (int i = 0; i < n; ++i) {
      if (c4 == 0 || c7 == 0) {
        string s2 = s.substr(i);
        if (s2 > func(c4, c7)) {
          int k = res.find_last_of('4');
          c4++;
          c7 += res.size() - k - 2;
          res = res.substr(0, k) + "7" + func(c4, c7);
        } else {
          res += func(c4, c7);
        }
        break;
      }
      if (s[i] == '4') {
        res += '4';
        c4--;
      } else if (s[i] == '7') {
        res += '7';
        c7--;
      } else if (s[i] < '4') {
        res += func(c4, c7);
        break;
      } else if (s[i] < '7') {
        res += '7';
        c7--;
        res += func(c4, c7);
        break;
      } else if (s[i] > '7') {
        int k = res.find_last_of('4');
        c4++;
        c7 += res.size() - k - 2;
        res = res.substr(0, k) + "7" + func(c4, c7);
        break;
      }
    }
    cout << res << endl;
  }
  return 0;
}
