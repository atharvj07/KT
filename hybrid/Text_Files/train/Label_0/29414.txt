#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
int n, m, c[N], w[N];
pair<int, int> ans[N];
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++) cin >> c[i];
  for (int i = 0; i < n; i++) cin >> w[i];
  set<pair<int, int> > s;
  long long res = 0;
  for (int i = 0; i < n; i++) {
    int C = c[i] % 100, W = w[i];
    ans[i].first = c[i] / 100;
    ans[i].second = C;
    m -= C;
    if (C) s.insert(make_pair(W * (100 - C), i));
    while (m < 0) {
      pair<int, int> p = (*s.begin());
      s.erase(p);
      int idx = p.second;
      m += 100;
      res += p.first;
      ans[idx].second = 0;
      ans[idx].first++;
    }
  }
  cout << res << "\n";
  for (int i = 0; i < n; i++)
    cout << ans[i].first << " " << ans[i].second << "\n";
}
