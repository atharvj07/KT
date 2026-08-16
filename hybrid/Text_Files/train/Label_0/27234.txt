#include <bits/stdc++.h>
using namespace std;
int main() {
  cin.sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cout.sync_with_stdio(false);
  int r, n;
  vector<pair<int, int> > all;
  cin >> r >> n;
  if (n == 0)
    cout << ((r & 1) ? "WIN" : "LOSE");
  else {
    int res = 0;
    for (int i = 0; i < n; i++) {
      int x, y;
      cin >> x >> y;
      all.push_back(make_pair(x, y));
    }
    sort(all.begin(), all.end());
    res ^= all[0].first - 1;
    res ^= r - all[n - 1].first;
    for (int i = 1; i < n; i++) {
      int x = (all[i].first - all[i - 1].first) & 1;
      if (all[i].second == all[i - 1].second)
        res ^= !x;
      else
        res ^= x;
    }
    cout << (res ? "WIN" : "LOSE");
  }
  return 0;
}
