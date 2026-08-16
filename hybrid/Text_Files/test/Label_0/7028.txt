#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct T {
  ll l, r;
  int id;
};
int main() {
  ios_base::sync_with_stdio(false);
  int n;
  cin >> n;
  vector<T> v;
  for (int i = 0; i < n; ++i) {
    ll x, y;
    cin >> x >> y;
    v.push_back({x, y, i});
  }
  sort((v).begin(), (v).end(), [](const T &a, const T &b) {
    if (a.l == b.l) {
      return a.r > b.r;
    }
    return a.l < b.l;
  });
  set<pair<ll, int>> m;
  for (auto &i : v) {
    if (m.empty()) {
      m.insert({-i.r, i.id});
      continue;
    }
    auto &cur = *m.begin();
    if (-cur.first >= i.r) {
      cout << i.id + 1 << ' ' << cur.second + 1 << endl;
      return 0;
    }
    m.insert({-i.r, i.id});
  }
  cout << "-1 -1\n";
  return 0;
}
