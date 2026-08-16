#include <bits/stdc++.h>
using namespace std;
signed main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long n, m1;
  cin >> n >> m1;
  string s[n];
  for (long long i = 0; i < n; i++) cin >> s[i];
  map<pair<long long, long long>, bool> m;
  for (long long i = 1; i < n - 1; i++) {
    for (long long j = 1; j < m1 - 1; j++) {
      if (s[i - 1][j - 1] == '#' && s[i + 1][j + 1] == '#' &&
          s[i + 1][j - 1] == '#' && s[i - 1][j + 1] == '#' &&
          s[i - 1][j] == '#' && s[i + 1][j] == '#' && s[i][j - 1] == '#' &&
          s[i][j + 1] == '#') {
        m[{i - 1, j - 1}] = true;
        m[{i + 1, j + 1}] = true;
        m[{i + 1, j - 1}] = true;
        m[{i - 1, j + 1}] = true;
        m[{i - 1, j}] = true;
        m[{i + 1, j}] = true;
        m[{i, j + 1}] = true;
        m[{i, j - 1}] = true;
      }
    }
  }
  for (long long i = 0; i < n; i++) {
    for (long long j = 0; j < m1; j++) {
      if (s[i][j] == '#') {
        if (m[{i, j}])
          continue;
        else {
          cout << "NO\n";
          return 0;
        }
      }
    }
  }
  cout << "YES\n";
}
