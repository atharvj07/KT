#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
const int mod = 1000000021;
const long long inf = 1LL << 61;
struct edge { int to, cost, id; };
struct edge2 { int to, id; };
struct state { int pos; long long cost; };
bool operator<(const state& s1, const state& s2) { return s1.cost > s2.cost; }
int N, M, dp[100009], dp2[100009], va[100009]; bool vis1[100009], vis2[100009]; vector<int> a, b, c;
vector<long long> shortest_path(vector<vector<edge> > g, int src) {
	vector<long long> ret(g.size(), inf); ret[src] = 0;
	priority_queue<state> que; que.push(state{ src, 0 });
	while (!que.empty()) {
		int u = que.top().pos; que.pop();
		for (edge e : g[u]) {
			long long nd = ret[u] + e.cost;
			if (ret[e.to] > nd) {
				ret[e.to] = nd;
				que.push(state{ e.to, nd });
			}
		}
	}
	return ret;
}
vector<int> solve() {
	vector<vector<edge> > g(N);
	vector<vector<edge> > rg(N);
	for (int i = 0; i < M; i++) {
		g[a[i]].push_back(edge{ b[i], c[i], i });
		rg[b[i]].push_back(edge{ a[i], c[i], i });
	}
	vector<long long> ds = shortest_path(g, 0);
	vector<long long> dt = shortest_path(rg, 1);
	vector<bool> ok(M);
	vector<vector<edge2> > sg(N), sr(N);
	for (int i = 0; i < M; i++) {
		if (ds[a[i]] + c[i] + dt[b[i]] == ds[1]) {
			sg[a[i]].push_back(edge2{ b[i], i });
			sr[b[i]].push_back(edge2{ a[i], i });
			ok[i] = true;
		}
	}
	fill(vis1, vis1 + N, false);
	fill(vis2, vis2 + N, false);
	fill(dp, dp + N, 0);
	fill(dp2, dp2 + N, 0);
	vector<int> dpm1(M), dpm2(M);
	priority_queue<state> que; que.push(state{ 0, 0 }); dp[0] = 1;
	while (!que.empty()) {
		int u = que.top().pos; que.pop();
		if (!vis1[u]) {
			vis1[u] = true;
			for (edge2 i : sg[u]) {
				dp[i.to] += dp[u];
				dpm1[i.id] = dp[u];
				if (dp[i.to] >= mod) dp[i.to] -= mod;
				que.push(state{ i.to, ds[i.to] });
			}
		}
	}
	que.push(state{ 1, 0 }); dp2[1] = 1;
	while (!que.empty()) {
		int u = que.top().pos; que.pop();
		if (!vis2[u]) {
			vis2[u] = true;
			for (edge2 i : sr[u]) {
				dp2[i.to] += dp2[u];
				dpm2[i.id] = dp2[u];
				if (dp2[i.to] >= mod) dp2[i.to] -= mod;
				que.push(state{ i.to, dt[i.to] });
			}
		}
	}
	for (int i = 0; i < N; i++) va[i] = 1LL * dp[i] * dp2[i] % mod;
	map<tuple<int, int, int>, int> cnts;
	for (int i = 0; i < M; i++) {
		cnts[make_tuple(a[i], b[i], c[i])]++;
	}
	vector<int> ret(M);
	for (int i = 0; i < M; i++) {
		if (!ok[i]) {
			ret[i] = (ds[b[i]] + dt[a[i]] + c[i] < ds[1] ? 2 : 1);
		}
		else {
			if (ds[b[i]] + dt[a[i]] + c[i] < ds[1]) ret[i] = 2;
			else if (ds[b[i]] + dt[a[i]] + c[i] == ds[1]) ret[i] = 1;
			else {
				if (1LL * dpm1[i] * dpm2[i] % mod == va[0] && cnts[make_tuple(a[i], b[i], c[i])] == 1) ret[i] = 0;
				else ret[i] = 1;
			}
		}
	}
	return ret;
}
vector<int> brute_force() {
	vector<int> ret(M);
	vector<vector<edge> > ig(N);
	for (int i = 0; i < M; i++) {
		ig[a[i]].push_back(edge{ b[i], c[i] });
	}
	long long res = shortest_path(ig, 0)[1];
	if (res == inf) return { -1 };
	for (int i = 0; i < M; i++) {
		vector<vector<edge> > g(M);
		for (int j = 0; j < M; j++) {
			if (i != j) g[a[j]].push_back(edge{ b[j], c[j] });
			else g[b[j]].push_back(edge{ a[j], c[j] });
		}
		long long re = shortest_path(g, 0)[1];
		if (re < res) ret[i] = 2;
		if (re == res) ret[i] = 1;
		if (re > res) ret[i] = 0;
	}
	return ret;
}
int rand_rng(int l, int r) {
	long long seed = rand() * 123456789LL + rand() * 3456789LL + rand() * 12345LL;
	return l + (seed) % (r - l);
}
void random_test() {
	N = 7; M = 7;
	for (int i = 0; i < 10000; i++) {
		a = vector<int>(M);
		b = vector<int>(M);
		c = vector<int>(M);
		for (int j = 0; j < M; j++) {
			while (a[j] == b[j]) {
				a[j] = rand_rng(0, N);
				b[j] = rand_rng(0, N);
			}
			c[j] = rand_rng(1, 10);
		}
		vector<int> ret1 = brute_force();
		if (ret1[0] != -1) {
			vector<int> ret2 = solve();
			if (ret1 != ret2) {
				cout << "BUG" << endl;
				solve();
			}
			if (i % 100 == 99) cout << i + 1 << endl;
		}
		else {
			i--;
			continue;
		}
	}
}
int main() {
	//random_test();
	ios::sync_with_stdio(false);
	cin >> N >> M;
	a = vector<int>(M);
	b = vector<int>(M);
	c = vector<int>(M);
	for (int i = 0; i < M; i++) {
		cin >> a[i] >> b[i] >> c[i]; a[i]--, b[i]--;
	}
	vector<int> ret = solve();
	for (int i = 0; i < M; i++) {
		if (ret[i] == 2) cout << "HAPPY\n";
		else if (ret[i] == 1) cout << "SOSO\n";
		else cout << "SAD\n";
	}
	return 0;
}