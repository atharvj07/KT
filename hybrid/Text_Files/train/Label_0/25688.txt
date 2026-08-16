#include <bits/stdc++.h>
using namespace std;
const int INF = 10000000;

class MaxFlow {
	struct edge {
		int to, cap, rev;
		edge(int to_, int cap_, int rev_) : to(to_), cap(cap_), rev(rev_) {};
	};

	int V;
	vector<vector<edge>> G;
	vector<int> level;
	vector<int> iter;

	void BFS(int s) {
		fill(level.begin(), level.end(), -1);
		queue<int> que;
		level[s] = 0;
		que.push(s);
		while (!que.empty()) {
			int v = que.front(); que.pop();
			for (size_t i = 0; i < G[v].size(); i++) {
				edge &e = G[v][i];
				if (e.cap > 0 && level[e.to] < 0) {
					level[e.to] = level[v] + 1;
					que.push(e.to);
				}
			}
		}
	}

	int DFS(int v, int t, int f) {
		if (v == t) return f;
		for (int &i = iter[v]; i < (int)G[v].size(); i++) {
			edge &e = G[v][i];
			if (e.cap > 0 && level[v] < level[e.to]) {
				int d = DFS(e.to, t, min(f, e.cap));
				if (d > 0) {
					e.cap -= d;
					G[e.to][e.rev].cap += d;
					return d;
				}
			}
		}
		return 0;
	}

public:
	MaxFlow(int _V) : V(_V), G(_V), level(_V), iter(_V) {}
	void add(int from, int to, int cap) {
		G[from].push_back(edge(to, cap, G[to].size()));
		G[to].push_back(edge(from, 0, G[from].size() - 1));
	}
	int Dinic(int s, int t) {
		int flow = 0;
		while (true) {
			BFS(s);
			if (level[t] < 0) return flow;
			fill(iter.begin(), iter.end(), 0);
			int f;
			while ((f = DFS(s, t, INF)) > 0) {
				flow += f;
			}
		}
	}
};

int main()
{
	cin.sync_with_stdio(false);
	int n, m;
	while (cin >> n >> m, n | m) {
		vector<int> u(m), v(m);
		for (int i = 0; i < m; i++) {
			cin >> u[i] >> v[i]; u[i]--; v[i]--;
		}
		int mi, ma;
		int l = 0, r = 50;
		while (l + 1 < r) {
			int c = (l + r) / 2;
			MaxFlow mf(n + m + 2);
			for (int i = 0; i < n; i++) {
				mf.add(n + m, i, c);
			}
			for (int i = 0; i < m; i++) {
				mf.add(u[i], n + i, 1);
				mf.add(v[i], n + i, 1);
				mf.add(n + i, n + m + 1, 1);
			}
			if (mf.Dinic(n + m, n + m + 1) == n * c) {
				l = c;
			}
			else {
				r = c;
			}
		}
		mi = l;
		l = 0, r = 100;
		while (l + 1 < r) {
			int c = (l + r) / 2;
			MaxFlow mf(n + m + 2);
			for (int i = 0; i < n; i++) {
				mf.add(n + m, i, c);
			}
			for (int i = 0; i < m; i++) {
				mf.add(u[i], n + i, 1);
				mf.add(v[i], n + i, 1);
				mf.add(n + i, n + m + 1, 1);
			}
			if (mf.Dinic(n + m, n + m + 1) == m) {
				r = c;
			}
			else {
				l = c;
			}
		}
		ma = r;
		cout << mi << ' ' << ma << endl;
	}
	return 0;
}