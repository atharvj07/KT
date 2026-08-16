#include <bits/stdc++.h>
using namespace std;
const long long int N = 200005;
const long long int LG = 22;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  long long int n, m;
  cin >> n >> m;
  map<long long int, long long int> r, c;
  string s[n];
  long long int cnt = 0, f = 0;
  for (long long int i = 0; i < n; i++) {
    cin >> s[i];
    for (long long int j = 0; j < m; j++) {
      if (s[i][j] == '*') {
        r[i]++, c[j]++;
        cnt++;
      }
    }
  }
  long long int x = -1, y = -1;
  for (long long int i = 0; i < n; i++) {
    for (long long int j = 0; j < m; j++) {
      long long int lol = r[i] + c[j] - (s[i][j] == '*');
      if (lol == cnt) {
        f = 1;
        x = i, y = j;
      }
    }
  }
  if (f) {
    cout << "YES\n";
    cout << x + 1 << ' ' << y + 1;
  } else
    cout << "NO\n";
  return 0;
}
