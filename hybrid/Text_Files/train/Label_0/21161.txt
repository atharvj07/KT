#include <bits/stdc++.h>
using namespace std;
int main() {
  map<string, string> mp;
  string s, t, k;
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    cin >> s >> t;
    mp[s] = t;
  }
  for (int i = 0; i < n; i++) {
    cin >> k;
    if (k.length() <= mp[k].length()) {
      cout << k << " ";
    } else
      cout << mp[k] << " ";
  }
  return 0;
}
