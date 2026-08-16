#include <bits/stdc++.h>
using namespace std;
int p[200100], a[200100], b[200100];
int main() {
  int n;
  cin >> n;
  map<int, pair<int, int> > mp;
  set<int> s[4];
  for (int i = 1; i <= n; i++) cin >> p[i];
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    s[a[i]].insert(p[i]);
  }
  for (int i = 1; i <= n; i++) {
    cin >> b[i];
    s[b[i]].insert(p[i]);
    mp[p[i]] = {a[i], b[i]};
  }
  int m;
  cin >> m;
  for (int i = 1; i <= m; i++) {
    int c;
    cin >> c;
    if (s[c].size() == 0) {
      cout << "-1 ";
      continue;
    }
    int val = *(s[c].begin());
    s[c].erase(val);
    cout << val << " ";
    if (mp[val].first != c)
      s[mp[val].first].erase(val);
    else if (mp[val].second != c)
      s[mp[val].second].erase(val);
  }
  cout << endl;
  return 0;
}
