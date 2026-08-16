#include <bits/stdc++.h>
using namespace std;
int n;
string s;
map<int, int> m;
int main() {
  ios::sync_with_stdio(false);
  cin >> n;
  while (n--) {
    cin >> s;
    int num = 0;
    bool f1 = 1, f2 = 1;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == '(')
        num++;
      else
        num--;
      if (num < 0) f1 = 0;
    }
    num = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
      if (s[i] == ')')
        num++;
      else
        num--;
      if (num < 0) f2 = 0;
    }
    if (f1 || f2) {
      m[num]++;
    }
  }
  int ans = 0;
  for (auto a : m) {
    if (m.count(-a.first)) ans += min(a.second, m[-a.first]);
  }
  cout << ans / 2;
}
