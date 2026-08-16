#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<ll, ll>;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  ll n, m;
  cin >> n >> m;
  vector<vector<ll>> d(n);
  vector<ll> debt(n);
  for (int i = 0; i < m; i++) {
    ll u, v, c;
    cin >> u >> v >> c;
    u--;
    v--;
    d[u].push_back(v);
    d[v].push_back(u);
    debt[u] -= c;
    debt[v] += c;
  }
  vector<bool> seen(n);
  vector<vector<ll>> ans;
  for (int i = 0; i < n; i++) {
    if (!seen[i]) {
      queue<ll> que;
      que.push(i);
      set<P> pd;
      set<P> md;
      if (debt[i] > 0)
        pd.insert(P(i, debt[i]));
      else if (debt[i] < 0)
        md.insert(P(i, debt[i]));
      while (que.size()) {
        ll v = que.front();
        que.pop();
        if (seen[v]) continue;
        seen[v] = true;
        for (ll nx : d[v]) {
          if (seen[nx]) continue;
          que.push(nx);
          if (debt[nx] > 0)
            pd.insert(P(nx, debt[nx]));
          else if (debt[nx] < 0)
            md.insert(P(nx, debt[nx]));
        }
      }
      while (pd.size()) {
        P plus = *pd.begin();
        P minus = *md.begin();
        if (plus.second > -minus.second) {
          ans.push_back({minus.first + 1, plus.first + 1, -minus.second});
          md.erase(minus);
          pd.erase(plus);
          pd.insert(P(plus.first, plus.second + minus.second));
        } else if (plus.second < -minus.second) {
          ans.push_back({minus.first + 1, plus.first + 1, plus.second});
          md.erase(minus);
          pd.erase(plus);
          md.insert(P(minus.first, minus.second + plus.second));
        } else {
          ans.push_back({minus.first + 1, plus.first + 1, plus.second});
          md.erase(minus);
          pd.erase(plus);
        }
      }
    }
  }
  cout << ans.size() << "\n";
  for (int i = 0; i < ans.size(); i++) {
    vector<ll> v = ans[i];
    cout << v[0] << " " << v[1] << " " << v[2] << "\n";
  }
}
