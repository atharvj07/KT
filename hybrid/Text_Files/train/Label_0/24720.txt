#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e3 + 5;
const int inf = 1e9 + 5;
int n, m;
string s;
vector<string> v;
bool check(string g) {
  for (int i = 0; i < n; ++i) {
    if (s[i] != '*') {
      if (s[i] != g[i]) {
        return false;
      }
      for (int j = 0; j < n; ++j) {
        if (g[j] == s[i] && s[j] == '*') {
          return false;
        }
      }
    }
  }
  return true;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> s >> m;
  string g;
  for (int i = 1; i <= m; ++i) {
    cin >> g;
    v.push_back(g);
  }
  for (int i = 0; i < v.size(); ++i) {
    if (!check(v[i])) {
      v.erase(v.begin() + i);
      i--;
    }
  }
  m = v.size();
  vector<char> ans;
  for (int i = 0; i < n; ++i) {
    if (s[i] == '*') {
      bool is = true;
      for (int j = 0; j < ans.size(); ++j) {
        if (ans[j] == v[0][i]) {
          is = false;
          break;
        }
      }
      if (is) {
        ans.push_back(v[0][i]);
      }
    }
  }
  for (int i = 1; i < m; ++i) {
    for (int j = 0; j < ans.size(); ++j) {
      for (int u = 0; u < n; ++u) {
        if (ans[j] == v[i][u]) {
          break;
        }
        if (u == n - 1) {
          ans.erase(ans.begin() + j);
          j--;
        }
      }
    }
  }
  cout << ans.size();
  return 0;
}
