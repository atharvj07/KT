#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
struct edge{ll to, cost;};
vector<edge> G[100000];
ll d[100000];
const ll INF = 1e18;
void dfs(ll v) {
  if (d[v] == INF) {d[v] = 0;}
  for (ll i = 0; i < G[v].size(); i++) {
    edge e = G[v][i];
    if (d[e.to] == INF) {
      d[e.to] = d[v] + e.cost;
      dfs(e.to);
    }
  }
}
int main() {
  ll N; cin >> N;
  for (ll i = 0; i < N-1; i++) {
    ll a,b,c; cin >> a >> b >> c;
    a--; b--;
    G[a].push_back({b,c}); G[b].push_back({a,c});
  }
  fill(d,d+N, INF);
  ll Q, K; cin >> Q >> K; K--;
  dfs(K);
  for (ll i = 0; i < Q; i++) {
    ll x, y; cin >> x >> y; x--; y--;
    cout << d[x]+d[y] << endl;
  }
}