#include <bits/stdc++.h>
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
using namespace std;
typedef long long int ll;
typedef long double ld;
typedef pair<int,int> pii;

void sol() {
	int N; cin >> N;
	vector<vector<int>> adj(N);

	for(int i = 0; i < N-1; i++) {
		int u, v; cin >> u >> v;
		u--; v--;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	int LOG = 0; while((1<<LOG) <= N) LOG++;
	vector<int> depth(N), inTime(N), outTime(N);
	vector<vector<int>> lift(LOG, vector<int>(N, -1));
	int curTime = 0;

	function<void(int,int)> dfs1 = [&](int u, int p) {
		inTime[u] = curTime++;
		for(int v : adj[u]) if(v != p) {
			depth[v] = 1+depth[u];
			lift[0][v] = u;
			dfs1(v, u);
		}
		outTime[u] = curTime++;
	};
	dfs1(0, -1);

	for(int lg = 1; lg < LOG; lg++)
		for(int i = 0; i < N; i++) {
			int up = lift[lg-1][i];
			if(up != -1) lift[lg][i] = lift[lg-1][up];
		}


	int hack1 = -1, hack2 = -1;
	auto get_lca = [&](int u, int v) {
		if(u == v) {
			hack1 = hack2 = -1;
			return u;
		}

		bool swapped = false;
		if(depth[u] < depth[v]) {
			swapped = true;
			swap(u, v);
		}

		for(int lg = LOG-1; lg >= 0; lg--) {
			if(lift[lg][u] >= 0 && depth[lift[lg][u]] > depth[v])
				u = lift[lg][u];
		}
		if(lift[0][u] == v) {
			hack1 = u; hack2 = -1;
			if(swapped) swap(hack1, hack2);
			return v;
		}
		if(lift[0][u] >= 0 && depth[lift[0][u]] >= depth[v])
				u = lift[0][u];
		for(int lg = LOG-1; lg >= 0; lg--) {
			if(lift[lg][u] != lift[lg][v]) {
				u = lift[lg][u];
				v = lift[lg][v];
			}
		}
		hack1 = u; hack2 = v;
		if(swapped) swap(hack1, hack2);
		return lift[0][v];
	};

	vector<int> idxIn(N, -1);
	for(int i = 0; i < N; i++)
		for(int j = 0; j < sz(adj[i]); j++) {
			if(adj[i][j] != lift[0][i]) idxIn[adj[i][j]] = j;
		}

	int Q; cin >> Q;
	vector<pii> paths(Q), easyPairs(Q);
	vector<vector<pii>> pairsAt(N);
	vector<int> openings(N), closings(N), totalSum(N), lcaOf(Q);
	vector<vector<int>> sumEach(N);


	for(int i = 0; i < Q; i++) {
		int u, v; cin >> u >> v;
		u--; v--;

		int lca = get_lca(u, v);

		int s1 = hack1, s2 = hack2;
		if(s1 > s2) {
			swap(s1, s2);
			swap(u, v);
		}

		paths[i] = {u, v};
		lcaOf[i] = lca;
		easyPairs[i] = {s1, s2};
		pairsAt[lca].push_back({s1, s2});
		
		if(s1 != -1) {
			openings[u]++;
			closings[s1]++;
		}
		if(s2 != -1) {
			openings[v]++;
			closings[s2]++;
		}
	}


	function<int(int)> dfs2 = [&](int u) {
		totalSum[u] += openings[u];
		sumEach[u] = vector<int>(sz(adj[u]));

		for(int i = 0; i < sz(adj[u]); i++) {
			int v = adj[u][i];
			if(v == lift[0][u]) continue;
			int ret = dfs2(v);
			sumEach[u][i] = ret;
			totalSum[u] += ret;
		}

		return totalSum[u] - closings[u];
	};
	dfs2(0);

	ll type1 = 0, type2 = 0;

	//type 1 interactions
	vector<int> subtreeCnts(N);
	for(int lca = 0; lca < N; lca++) {
		sort(all(pairsAt[lca]));
		for(auto p : pairsAt[lca]) {
			if(p.first != -1) subtreeCnts[p.first]++;
			if(p.second != -1) subtreeCnts[p.second]++;
		}

		int M = sz(pairsAt[lca]);

		for(int i = 0; i < M; i++) {
			int j = i; while(j < M && pairsAt[lca][i] == pairsAt[lca][j]) j++;
			int addBack = j-i-1;

			for(int k = i; k < j; k++) {
				ll amt = M-1;
				auto p = pairsAt[lca][k];
				if(p.first != -1) amt -= subtreeCnts[p.first]-1;
				if(p.second != -1) amt -= subtreeCnts[p.second]-1;
				if(p.first != -1 && p.second != -1) {
					amt += addBack;
				}
				type1 += amt;
			}

			i = --j;
		}

		for(auto p : pairsAt[lca]) {
			if(p.first != -1) subtreeCnts[p.first]--;
			if(p.second != -1) subtreeCnts[p.second]--;
		}
	}

	//type 2 interactions 
	for(int i = 0; i < Q; i++) {
		int lca = lcaOf[i];
		ll amt = totalSum[lca];
		auto e = easyPairs[i];
		if(e.first != -1) amt -= sumEach[lca][idxIn[e.first]];
		if(e.second != -1) amt -= sumEach[lca][idxIn[e.second]];

		type2 += amt;
	}
	type1 /= 2;

	ll res = type1+type2;
	cout << res << endl;
}

int main() {
	// freopen("stats.in", "r", stdin);
	// freopen("stats.out", "w", stdout);
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	// int T; cin >> T;
	// while(T--)
	sol();

	return 0;
}
