#include <bits/stdc++.h>
using namespace std;
#define db(x) cerr << #x << "=" << x << endl
#define db2(x, y) cerr << #x << "=" << x << "," << #y << "=" << y << endl
#define db3(x, y, z) cerr << #x << "=" << x << "," << #y << "=" << y << "," << #z << "=" << z << endl
#define dbv(v) cerr << #v << "="; for (auto _x : v) cerr << _x << ", "; cerr << endl
#define dba(a, n) cerr << #a << "="; for (int _i = 0; _i < (n); ++_i) cerr << a[_i] << ", "; cerr << endl
template <typename A, typename B>
ostream& operator<<(ostream& os, const pair<A, B>& x) {
	return os << "(" << x.first << "," << x.second << ")";
}
typedef long long ll;
typedef long double ld;
struct Shop {
	int s, p;
	ll c;
};
int mp[35][35];
struct Mcmf {
	const ll INFC = 1LL << 60;
	struct Edge {
		int to;
		int f, cap;
		ll cost;
	};
	int n, src, sink;
	vector<ll> pi, dist;
	vector<int> fromEdge;
	vector<Edge> edges;
	vector<vector<int>> G;
	Mcmf(int _n, int _src = -1, int _sink = -1) : n(_n), src(_src), sink(_sink) {
		G.resize(n);
		dist.resize(n);
		pi.resize(n);
		fromEdge.resize(n);
	}
	void addEdge(int from, int to, int cap, ll cost) {
		G[from].push_back(edges.size());
		edges.push_back({to, 0, cap, cost});
		G[to].push_back(edges.size());
		edges.push_back({from, 0, 0, -cost});
	}
	ll cheapestPath() {
		typedef pair<ll, int> Pair;
		priority_queue<Pair, vector<Pair>, greater<Pair>> pq;
		fill(dist.begin(), dist.begin() + n, INFC);
		dist[src] = 0;
		pq.emplace(dist[src], src);
		while (!pq.empty()) {
			int u = pq.top().second;
			ll cdist = pq.top().first;
			pq.pop();
			if (cdist > dist[u]) continue;
			for (int x : G[u]) {
				Edge e = edges[x];
				if (e.f == e.cap) continue;
				int v = e.to;
				// assert pi[u], pi[v] <<< INFC
				ll val = dist[u] + pi[u] - pi[v] + e.cost;
				if (val < dist[v]) {
					dist[v] = val;
					fromEdge[v] = x;
					pq.emplace(dist[v], v);
				}
			}
		}
		if (dist[sink] >= INFC) return INFC;
		ll cost = dist[sink] + pi[sink];
		for (int k = 0; k < n; ++k)
			pi[k] = min(INFC, pi[k] + dist[k]);
		return cost;
	}
	vector<ll> maxFlow() {
		vector<ll> ret(1, 0);
		int totflow = 0;
		const int LIM = 27905;
		while (totflow < LIM) {
			ll cost = cheapestPath();
			// Change INFC to 0 to find min-cost flow (not maxflow)
			// Can prove that marginal-cost of flows increases (by exchange)
			if (cost >= INFC) break;
			int flow = INT_MAX;
			for (int x = sink; x != src;) {
				int e = fromEdge[x];
				flow = min(flow, edges[e].cap - edges[e].f);
				x = edges[e ^ 1].to;
			}
			for (int x = sink; x != src;) {
				int e = fromEdge[x];
				edges[e].f += flow;
				edges[e ^ 1].f -= flow;
				x = edges[e ^ 1].to;
			}
			flow = min(flow, LIM - totflow);
			totflow += flow;
			// Inc one flow at a time
			for (int i = 0; i < flow; ++i) {
				ret.push_back(cost);
			}
		}
		return ret;
	}
	// pi makes all edges nonnegative, so initialize if necessary
	void initPi() {
		fill(pi.begin(), pi.begin() + n, 0);
	}
};
int main() {
	int n;
	scanf("%d", &n);
	vector<vector<Shop>> shops(n);
	vector<vector<int>> shopSizes(n);
	int vars = 0;	
	for (int i = 0; i < n; ++i) {
		int k;
		scanf("%d", &k);
		shops[i].resize(k);
		for (int j = 0; j < k; ++j) {
			Shop& s = shops[i][j];
			scanf("%d%d%lld", &s.s, &s.p, &s.c);
			mp[i][j] = vars++;
		}
		mp[i][k] = vars++;
		sort(shops[i].begin(), shops[i].end(), [](Shop a, Shop b) {
			return a.s < b.s;
		});
		for (Shop& s : shops[i]) shopSizes[i].push_back(s.s);
	}
	auto var = [&](int a, int b) {
		return mp[a][b];
	};
	int m;
	scanf("%d", &m);
	vector<pair<pair<int, int>, pair<int, int>>> constraints;
	for (int i = 0; i < m; ++i) {
		int u, v, w;
		scanf("%d%d%d", &u, &v, &w);
		--u;
		--v;
		for (int j = 0; j < shops[v].size(); ++j) {
			int s = shops[v][j].s;
			int k = lower_bound(shopSizes[u].begin(), shopSizes[u].end(), s - w) - shopSizes[u].begin();
			// x(u, k) <= x(v, j)
			constraints.emplace_back(make_pair(u, k), make_pair(v, j));
		}
	}
	const int CAP = 1e8;
	Mcmf g(vars + 2, vars, vars + 1);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < shops[i].size(); ++j) {
			g.addEdge(var(i, j + 1), var(i, j), CAP, 0);
			g.addEdge(var(i, j), var(i, j + 1), CAP, shops[i][j].c);
			g.addEdge(var(i, j), var(i, j + 1), shops[i][j].p, 0);
//			int res = -shops[i][j].p;
//			if (j) res += shops[i][j - 1].p;
//			if (res < 0) g.addEdge(var(i, j), var(i, j + 1), -res, 0);
		}
		g.addEdge(g.src, var(i, 0), CAP, 0);
		g.addEdge(var(i, shops[i].size()), g.sink, CAP, 0);
	}
	for (auto& c : constraints) {
		g.addEdge(var(c.second.first, c.second.second), var(c.first.first, c.first.second), CAP, 0);
	}
	auto costs = g.maxFlow();
	vector<ll> pcost(costs.size() + 1);
	for (int i = 0; i < costs.size(); ++i) {
		pcost[i + 1] = pcost[i] + costs[i];
	}
	int q;
	scanf("%d", &q);
	while (q--) {
		ll qa;
		scanf("%lld", &qa);
		int i = lower_bound(costs.begin(), costs.end(), qa) - costs.begin();
		if (i == costs.size()) printf("-1\n");
		else {
			ll ans = qa * (i - 1) - pcost[i];
			assert(ans >= 0);
			printf("%lld\n", ans);
		}
	}
	return 0;
}
