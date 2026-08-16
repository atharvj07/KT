// In The Name Of Allah
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair <int, int> pii;
 
#define error(x) cout << #x << " = " << x << endl;
 
const int N = 1e5 + 5, mod = 1e9 + 7;
const ll inf = 1e15;
 
inline int sum(int a, int b) {
	a += b;
	if(a >= mod)
		a -= mod;
	if(a < 0)
		a += mod;
	return a;
}
 
inline int mult(int a, int b) {
	return (1LL * a * b) % mod;
}
 
int n, m, dp[N][2], S, T;
ll dist[N][2];
vector <pii> adj[N];
vector <pair <pii, int> > edge;
 
inline void dijkstra(int src, int id) {
	for (int i = 0; i < n; i++)
		dist[i][id] = inf;
	dp[src][id] = 1;
	dist[src][id] = 0;
	set <pair <ll, int>> s;
	s.insert({0, src});
	while(!s.empty()) {
		pair <ll, int> p = (*s.begin());
		s.erase(p);
		int v = p.second;
		for (auto e : adj[v]) {
			int u = e.first, w = e.second;
			if(dist[u][id] > dist[v][id] + w) {
				s.erase({dist[u][id], u});
				dist[u][id] = dist[v][id] + w;
				s.insert({dist[u][id], u});
				dp[u][id] = dp[v][id];
			}
			else if(dist[u][id] == dist[v][id] + w)
				dp[u][id] = sum(dp[u][id], dp[v][id]);
		}
	}
}
 
int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);	
	cin >> n >> m >> S >> T;
	S--, T--;
	for (int i = 0; i < m; i++) {
		int v, u, w;
		cin >> v >> u >> w;
		v--, u--;
		adj[v].push_back({u, w});
		adj[u].push_back({v, w});
		edge.push_back({{u, v}, w});
	}
	dijkstra(S, 0);
	dijkstra(T, 1);
	int ans = mult(dp[S][1], dp[T][0]);
	// error(dp[S][1]);
	// error(dp[T][0]);
	for (int i = 0; i < n; i++) {
		if(dist[i][0] == dist[i][1]) {
			// error(i);
			ans = sum(ans, - mult(mult(dp[i][0], dp[i][0]), mult(dp[i][1], dp[i][1])));
		}
	}

	for (auto e : edge) {
		int vv = e.first.first, uu = e.first.second, w = e.second;
		for (auto x : {make_pair(vv, uu), make_pair(uu, vv)}) {
			int v = x.first, u = x.second;
			if(dist[v][0] < (dist[S][1] / 2) && dist[u][1] < (dist[S][1] / 2) && dist[v][0] + dist[u][1] + w == dist[S][1]) {
				ans = sum(ans, -mult(mult(dp[v][0], dp[u][1]), mult(dp[v][0], dp[u][1])));
			}
		}
	}

	cout << ans << "\n";
 
}