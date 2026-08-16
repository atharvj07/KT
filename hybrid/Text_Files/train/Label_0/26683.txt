#include <bits/stdc++.h>
using namespace std;
int main() {
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);
  cout.setf(ios_base::fixed);
  cout.precision(24);
  int n;
  cin >> n;
  vector<int> deep(n, 0);
  string s;
  cin >> s;
  int cnt = 0, mx = 0;
  for (int i = 0; i < n; ++i) {
    if (s[i] == '[') {
      deep[i] = cnt;
      cnt++;
    } else {
      cnt--;
      deep[i] = cnt;
    }
    mx = max(mx, deep[i]);
  }
  int sz = (1 + mx) * 2 + 1;
  int j = 0;
  vector<string> table(sz, string(10 * n, ' '));
  for (int i = 0; i < n; ++i) {
    int t = mx - deep[i];
    int cnt = (t)*2 + 1;
    if (s[i] == '[') {
      table[deep[i]][j] = '+';
      table[deep[i]][j + 1] = '-';
      for (int k = deep[i] + 1, tt = 0; tt < cnt; ++tt, ++k) {
        table[k][j] = '|';
      }
      table[deep[i] + cnt + 1][j + 1] = '-';
      table[deep[i] + cnt + 1][j] = '+';
      j++;
    } else {
      table[deep[i]][j] = '-';
      table[deep[i]][j + 1] = '+';
      for (int k = deep[i] + 1, tt = 0; tt < cnt; ++tt, ++k) {
        table[k][j + 1] = '|';
      }
      table[deep[i] + cnt + 1][j + 1] = '+';
      table[deep[i] + cnt + 1][j] = '-';
      j += 2;
      if (i + 1 != n) {
        if (s[i + 1] == ']') {
          j--;
        }
      }
    }
    if (s[i] == '[' && deep[i] == deep[i + 1]) {
      j += 2;
    }
  }
  bool ok = true;
  while (ok) {
    for (int i = 0; i < sz; ++i) {
      table[i].pop_back();
    }
    for (int i = 0; i < sz; ++i) {
      if (table[i].back() != ' ') {
        ok = false;
        break;
      }
    }
  }
  for (auto p : table) {
    cout << p << "\n";
  }
  return 0;
}
