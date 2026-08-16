#include <vector>
#include <iostream>
#include <climits>
#include <numeric>
#include <algorithm>
#include <cstdio>
#include <memory.h>
#include <limits>
#include <queue>

using namespace std;

// usage:
// MaxFlowDinic::Init(n);
// MaxFlowDinic::AddEdge(0, 1, 100, 100); // for bidirectional edge
// MaxFlowDinic::AddEdge(1, 2, 100); // directional edge
// result = MaxFlowDinic::Solve(0, 2); // source -> sink
// graph[i][edgeIndex].res -> residual
//
// in order to find out the minimum cut, use `l'.
// if l[i] == 0, i is unrechable.

struct MaxFlowDinic
{
	typedef int flow_t;

	struct Edge
	{
		int next;
		int inv; /* inverse edge index */
		flow_t res; /* residual */
		Edge(int q, int w, flow_t e) {
			next = q;
			inv = w;
			res = e;
		}
	};

	int n;
	vector<vector<Edge>> graph;

	vector<int> q, l, start;

	void Init(int _n) {
		n = _n;
		graph.resize(n);
		for (int i = 0; i < n; i++) graph[i].clear();
	}
	void AddNodes(int count) {
		n += count;
		graph.resize(n);
	}
	void AddEdge(int s, int e, flow_t cap, flow_t caprev = 0) {
		Edge forward = Edge(e, graph[e].size() + ((s == e) ? 1 : 0), cap);
		Edge reverse = Edge(s, graph[s].size(), caprev);
		graph[s].push_back(forward);
		graph[e].push_back(reverse);
	}

	bool AssignLevel(int source, int sink) {
		int t = 0;
		memset(&l[0], 0, sizeof(l[0]) * l.size());
		l[source] = 1;
		q[t++] = source;
		for (int h = 0; h < t && !l[sink]; h++) {
			int cur = q[h];
			for (int i = 0; i < graph[cur].size(); i++) {
				int next = graph[cur][i].next;
				if (l[next]) continue;
				if (graph[cur][i].res > 0) {
					l[next] = l[cur] + 1;
					q[t++] = next;
				}
			}
		}
		return l[sink] != 0;
	}

	flow_t BlockFlow(int cur, int sink, flow_t currentFlow) {
		if (cur == sink) return currentFlow;
		for (int &i = start[cur]; i < graph[cur].size(); i++) {
			int next = graph[cur][i].next;
			if (graph[cur][i].res == 0 || l[next] != l[cur] + 1)
				continue;
			if (flow_t res = BlockFlow(next, sink, min(graph[cur][i].res, currentFlow))) {
				int inv = graph[cur][i].inv;
				graph[cur][i].res -= res;
				graph[next][inv].res += res;
				return res;
			}
		}
		return 0;
	}

	flow_t Solve(int source, int sink)
	{
		q.resize(n);
		l.resize(n);
		start.resize(n);
		flow_t ans = 0;
		while (AssignLevel(source, sink)) {
			memset(&start[0], 0, sizeof(start[0])*n);
			while (flow_t flow = BlockFlow(source, sink, numeric_limits<flow_t>::max())) {
				ans += flow;
			}
		}
		return ans;
	}
};

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	for (;;) {
		int n, m; cin >> n >> m;
		if (n == 0 && m == 0) break;
		MaxFlowDinic mf;
		mf.Init(n + m + 2);
		for (int i = 1; i <= m; i++) {
			int x, y; cin >> x >> y;
			mf.AddEdge(x, i + n, 1);
			mf.AddEdge(y, i + n, 1);
			mf.AddEdge(i + n, n + m + 1, 1);
		}

		int mn = 0, mx = 0;
		int fin = 0;
		bool flag = true;

		for (int i = 1; i < n; i++) {
			for (int j = 1; j <= n; j++)
				mf.AddEdge(0, j, 1);
			int ret = mf.Solve(0, n + m + 1);
			fin += ret;
			if (ret == n && flag) mn = i;
			else flag = false;
			if (fin == m) {
				mx = i;
				break;
			}
		}

		cout << mn << " " << mx << "\n";
	}
	return 0;
}
