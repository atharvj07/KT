#include <bits/stdc++.h>
using namespace std;
int n, m;
vector<pair<int, int> > v1, v2;
set<int> a1, a2;
void solve() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    int first, second;
    cin >> first >> second;
    v1.push_back({min(first, second), max(first, second)});
  }
  for (int i = 0; i < m; i++) {
    int first, second;
    cin >> first >> second;
    v2.push_back({min(first, second), max(first, second)});
  }
  for (int i = 0; i < n; i++) {
    set<int> s1;
    for (int k = 0; k < m; k++) {
      if (v1[i] == v2[k]) continue;
      multiset<int> s;
      s.insert(v1[i].first);
      s.insert(v1[i].second);
      s.insert(v2[k].first);
      s.insert(v2[k].second);
      if (s.count(v1[i].first) == 2) {
        s1.insert(v1[i].first);
      }
      if (s.count(v1[i].second) == 2) {
        s1.insert(v1[i].second);
      }
    }
    if ((int)s1.size() > 1) {
      cout << -1 << '\n';
      return;
    }
    if ((int)s1.size() == 1) {
      a1.insert(*s1.begin());
    }
  }
  swap(v1, v2);
  for (int i = 0; i < m; i++) {
    set<int> s1;
    for (int k = 0; k < n; k++) {
      if (v1[i] == v2[k]) continue;
      multiset<int> s;
      s.insert(v1[i].first);
      s.insert(v1[i].second);
      s.insert(v2[k].first);
      s.insert(v2[k].second);
      if (s.count(v1[i].first) == 2) {
        s1.insert(v1[i].first);
      }
      if (s.count(v1[i].second) == 2) {
        s1.insert(v1[i].second);
      }
    }
    if ((int)s1.size() > 1) {
      cout << -1 << '\n';
      return;
    }
    if ((int)s1.size() == 1) {
      a2.insert(*s1.begin());
    }
  }
  if ((int)a1.size() == 1 and (int) a2.size() == 1) {
    cout << *a1.begin() << '\n';
  } else {
    cout << 0 << '\n';
  }
}
signed main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t = 1;
  while (t--) {
    solve();
  }
  return 0;
}
