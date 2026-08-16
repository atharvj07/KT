#include <bits/stdc++.h>
using namespace std;

typedef int flow_type;

struct edge {
	int to;
	flow_type cap;
	int rev;
	edge(int t, flow_type c, int r):to(t), cap(c), rev(r){}
};

const flow_type INF = 0xfffffff;
vector<vector<edge> > G;
vector<int> level;
vector<int> iter;

inline void init(int V) {
	G.assign(V, vector<edge>());
	level.assign(V, 0);
	iter.assign(V, 0);
}

inline void add_edge(int from, int to, flow_type cap) {
	G[from].push_back(edge(to, cap, G[to].size()));
	G[to].push_back(edge(from, 0, G[from].size() - 1));
}

void bfs(int s) {
	fill(level.begin(), level.end(), -1);
	queue<int> que;
	level[s] = 0;
	que.push(s);

	while(!que.empty()) {
		const int v = que.front();
		que.pop();

		for(int i = 0; i < static_cast<int>(G[v].size()); ++i) {
			const edge& e = G[v][i];
			if(e.cap > 0 && level[e.to] < 0) { // 実数ならEPS比較
				level[e.to] = level[v] + 1;
				que.push(e.to);
			}
		}
	}
}

flow_type dfs(int v, int t, flow_type f) {
	if(v == t) return f;

	for(int& i = iter[v]; i < static_cast<int>(G[v].size()); ++i) {
		edge& e = G[v][i];
		if(e.cap > 0 && level[v] < level[e.to]) {
			const flow_type d = dfs(e.to, t, min(f, e.cap));
			if(d > 0) {
				e.cap -= d;
				G[e.to][e.rev].cap += d;
				return d;
			}
		}
	}

	return 0;
}

flow_type max_flow(int s, int t) {
	flow_type flow = 0;

	for(;;) {
		bfs(s);
		if(level[t] < 0)
			return flow;

		fill(iter.begin(), iter.end(), 0);
		while(flow_type f = dfs(s, t, INF) > 0) {
			flow += f;
		}
	}
}

int main() {
	int n;
	cin >> n;

	vector<pair<int, int>> blocks;
	for(int i = 0; i < n; ++i) {
		int w, h;
		cin >> w >> h;
		if(w > h) swap(w, h);
		blocks.emplace_back(w, h);
	}

	const int source = n + n;
	const int sink = source + 1;
	const int num = sink + 1;
	init(num);

	for(int i = 0; i < n; ++i) {
		add_edge(source, i, 1);

		for(int j = 0; j < n; ++j) {
			if(blocks[i].first < blocks[j].first && blocks[i].second < blocks[j].second) {
				add_edge(i, j + n, 1);
			}
		}
	}

	for(int i = 0; i < n; ++i) {
		add_edge(i + n, sink, 1);
	}

	cout << n - max_flow(source, sink) << endl;

	return 0;
}
