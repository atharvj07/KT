#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=(a);i<(b);++i)
#define allof(a) (a).begin(),(a).end()
typedef pair< int, int > pii;

class BipartiteMatching {
private:
	int V;
	vector< vector< int > > adj;
	vector< int > match;
	vector< bool > used;
	vector< bool > visible;
	
	bool dfs(int v) {
		used[v] = 1;
		
		for (int u : adj[v]) {
			if (!visible[u]) continue;
			
			int w = match[u];
			if (w < 0 || (!used[w] && dfs(w))) {
				match[v] = u;
				match[u] = v;
				return 1;
			}
		}
		
		return 0;
	}
	
public:
	BipartiteMatching(int n) : V(n), adj(n, vector< int >()), match(n, -1), used(n, 0), visible(n, false) {}
	
	void addEdge(int u, int v) {
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	
	bool startDFS(int v) {
		if (!visible[v] || match[v] >= 0) return false;
		fill(allof(used), 0);
		return dfs(v);
	}
	
	void setVisible(int v) { visible[v] = true; }
	void setUnvisible(int v) { visible[v] = false; }
	void setUnmatch(int v) { match[v] = -1; }
	
	int getMatch(int v) { return match[v]; }
};



int n, x[5000][3], y[5000][3], par[5000][3];
set< pii > candidates[5000];
set< int > cand_id[5000];

const int dx[2][3] = {{1,0,-1}, {1,0,-1}};
const int dy[2][3] = {{0,-1,0}, {0,1,0}};
const int add[3][2][3] = {
	{{0,0,0}, {0,0,0}},
	{{1,0,1}, {0,1,0}},
	{{0,1,0}, {1,0,1}}
};

int getPar(pii p) { return (abs(p.first) + abs(p.second)) % 2; }

bool validPieces(set< pii >& pset) {
	int deg_sum = 0, max_deg = 0;
	for (pii p : pset) {
		int deg = 0;
		for_(d,0,3) {
			pii pi(p.first + dx[getPar(p)][d], p.second + dy[getPar(p)][d]);
			deg += pset.count(pi);
		}
		max_deg = max(max_deg, deg);
		deg_sum += deg;
	}
	
	if (deg_sum != 6) return false;
	if (max_deg == 3) return true;
	
	for (pii p : pset) for_(a,0,3) {
		bool flag = true;
		pii cur = p;
		int par = getPar(p);
		for_(d,0,3) {
			pii np(cur.first + dx[getPar(cur)][add[a][par][d]], cur.second + dy[getPar(cur)][add[a][par][d]]);
			flag &= (pset.count(np) == 1);
			cur = np;
		}
		if (flag) return true;
	}
	return false;
}

void makeCandidates() {
	for_(i,0,n) {
		candidates[i].clear();
		set< pii > pset;
		for_(j,0,3) pset.insert(pii(x[i][j], y[i][j]));
		for_(j,0,3) for_(d,0,3) {
			set< pii > pset_j = pset;
			pii np(x[i][j] + dx[par[i][j]][d], y[i][j] + dy[par[i][j]][d]);
			pset_j.insert(np);
			if (pset_j.size() == 4 && validPieces(pset_j)) candidates[i].insert(np);
		}
	}
}

void solve() {
	makeCandidates();
	
	map< pii, int > pii_to_id;
	int new_id = 0;
	for_(i,0,n) {
		for (pii p : candidates[i]) {
			if (pii_to_id.count(p)) continue;
			pii_to_id[p] = new_id++;
			cand_id[i].insert(pii_to_id[p]);
		}
	}
	
	int m = pii_to_id.size();
	BipartiteMatching bm(n + m);
	for_(i,0,n) for (pii p : candidates[i]) bm.addEdge(i, n + pii_to_id[p]);
		
	for_(i,0,n+m) bm.setVisible(i);
	for_(i,0,n) for_(j,0,3) {
		pii p(x[i][j], y[i][j]);
		if (pii_to_id.count(p)) bm.setUnvisible(n + pii_to_id[p]);
	}
	
	vector< int > miss;
	for_(v,0,n) bm.startDFS(v);
	for_(v,0,n) if (bm.getMatch(v) < 0) miss.push_back(v);
	
	if (miss.size() == 0) puts("Valid");
	else if (miss.size() > 4) puts("Invalid");
	else {
		vector< int > ans;		
		for_(u,0,n) {
			for_(j,0,3) {
				pii p(x[u][j], y[u][j]);
				if (pii_to_id.count(p)) bm.setVisible(n + pii_to_id[p]);
			}
			int id = bm.getMatch(u);
			if (id >= 0) {
				bm.setUnmatch(u);
				bm.setUnmatch(id);
			}
			
			for_(v,0,n) if (v != u) bm.startDFS(v);
			bool no_miss = true;
			for_(v,0,n) if (v != u) no_miss &= (bm.getMatch(v) >= 0);
			if (no_miss) ans.push_back(u);
			
			for_(j,0,3) {
				pii p(x[u][j], y[u][j]);
				if (pii_to_id.count(p)) {
					id = n + pii_to_id[p];
					bm.setUnvisible(id);
					for_(v,0,n) {
						if (bm.getMatch(v) == id) {
							bm.setUnmatch(v);
							bm.setUnmatch(id);
						}
					}
				}
			}
		}
		
		if (ans.size() == 0) puts("Invalid");
		else {
			puts("Remove");
			for (int v : ans) printf("%d\n", v+1);
		}
	}
}

int main() {
	while (1) {
		cin >> n;
		if (n == 0) break;
		for_(i,0,n) for_(j,0,3) {
			cin >> x[i][j] >> y[i][j];
			par[i][j] = (abs(x[i][j]) + abs(y[i][j])) % 2;
		}
		solve();
	}
}