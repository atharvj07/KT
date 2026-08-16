#include <bits/stdc++.h>
using namespace std;
bool isLeft(const pair<int, int>& a, const pair<int, int>& b,
            const pair<int, int>& c) {
  return (b.first - a.first) * 1LL * (c.second - a.second) -
             (b.second - a.second) * 1LL * (c.first - a.first) <=
         0LL;
}
vector<pair<int, int>> convexHull(vector<pair<int, int>> p) {
  sort(p.begin(), p.end());
  vector<pair<int, int>> h;
  for (int i = 0; i < 2; i++) {
    auto start = h.size();
    for (const pair<int, int>& q : p) {
      while (h.size() >= start + 2 &&
             isLeft(h[h.size() - 2], h[h.size() - 1], q))
        h.pop_back();
      h.push_back(q);
    }
    h.pop_back();
    reverse(p.begin(), p.end());
  }
  return h;
}
int main() {
  ios::sync_with_stdio(false), cin.tie(nullptr);
  while (true) {
    int n, m;
    cin >> n >> m;
    if (n == 0 && m == 0) break;
    vector<pair<int, int>> pts(m);
    vector<int> mn(n + 3, +n);
    vector<int> mx(n + 3, -n);
    for (int i = 0; i < (m); i++) {
      cin >> pts[i].first >> pts[i].second;
      if (mn[pts[i].first] > pts[i].second) mn[pts[i].first] = pts[i].second;
      if (mx[pts[i].first] < pts[i].second) mx[pts[i].first] = pts[i].second;
    }
    vector<pair<int, int>> ans;
    for (int i = 0; i < (m); i++) {
      for (int a : {pts[i].first - 1, pts[i].first, pts[i].first + 1}) {
        for (int b :
             {pts[i].second - 1, pts[i].second - 1, pts[i].second + 1}) {
          int cnt = 0;
          for (int x : {a + 1, a}) {
            for (int y : {b + 1, b}) {
              if (mn[x] <= y && y <= mx[x]) {
                cnt++;
              }
            }
          }
          if (cnt == 4) {
            ans.push_back({a, b});
          }
        }
      }
    }
    ans = convexHull(ans);
    reverse(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    int i = int(min_element(ans.begin(), ans.end()) - ans.begin());
    cout << ans[i].first << ' ' << ans[i].second << '\n';
    for (int j = (i + 1) % ans.size(); j != i; j = (j + 1) % ans.size())
      cout << ans[j].first << ' ' << ans[j].second << '\n';
  }
}
