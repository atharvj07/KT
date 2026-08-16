#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = 1e9;
const ll mod = 1e9 + 7;
const double eps = 1e-6;
const double PI = acos(-1);
int main() {
  string a, b;
  cin >> a >> b;
  map<char, char> mp;
  vector<pair<char, char>> ans;
  for (int i = 0; i < a.size(); i++) {
    if (mp[a[i]] == mp['^'] && mp[b[i]] == mp['^']) {
      mp[a[i]] = b[i];
      mp[b[i]] = a[i];
      if (a[i] != b[i]) {
        ans.push_back({a[i], b[i]});
      }
    } else {
      if (mp[a[i]] == b[i]) {
        continue;
      } else {
        cout << -1;
        return 0;
      }
    }
  }
  cout << ans.size() << "\n";
  for (auto i : ans) {
    cout << i.first << " " << i.second << "\n";
  }
}
