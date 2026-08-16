#include <bits/stdc++.h>
using namespace std;
const long double eps = 1e-9;
const long double pi = acos(-1.0);
const long long inf = 1e+9;
const long long inf64 = inf * inf;
#pragma comment(linker, "/STACK:36777216")
template <typename T>
istream &operator>>(istream &, vector<T> &);
template <typename T>
ostream &operator<<(ostream &, const vector<T> &);
void solve() {
  int m;
  cin >> m;
  string s;
  cin >> s;
  int n = s.size();
  vector<int> cnt(26);
  for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
  for (char t = 'a'; t <= 'z'; t++) {
    int last = -1;
    bool fl = 1;
    int count = 0;
    for (int i = 0; i < n; i++) {
      if (s[i] < t) {
        if (i - last > m) {
          fl = 0;
          break;
        }
        last = i;
      }
      if (s[i] == t) {
        int pos = -1;
        int pos2 = -1;
        for (int j = last + 1; j < n && j < last + 1 + m; j++) {
          if (s[j] < t) pos = j;
          if (s[j] == t) pos2 = j;
        }
        if (pos > i) {
          last = pos;
          i = pos;
          continue;
        }
        if (pos2 != -1) {
          i = pos2;
          last = pos2;
          count++;
        } else {
          fl = 0;
          break;
        }
      }
      if (n - last <= m) break;
    }
    if (fl && n - last <= m) {
      string ans = "";
      for (char z = 'a'; z < t; z++) ans += string(cnt[z - 'a'], z);
      ans += string(count, t);
      cout << ans << endl;
      return;
    }
  }
}
int main() {
  solve();
  return 0;
}
template <typename T>
istream &operator>>(istream &is, vector<T> &v) {
  for (int i = 0; i < v.size(); ++i) is >> v[i];
  return is;
}
template <typename T>
ostream &operator<<(ostream &os, const vector<T> &v) {
  for (int i = 0; i < v.size(); ++i) os << v[i];
  return os;
}
