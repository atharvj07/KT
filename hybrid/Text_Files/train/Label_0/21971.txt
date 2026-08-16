#include <bits/stdc++.h>
using namespace std;

const int INF = 0x3f3f3f3f;

typedef double DB;
typedef long long LL;
#define pb push_back
#define mp make_pair

const int maxN = 444;
const int maxE = maxN * maxN * 2;
int n, m, c[maxN];
int h[maxN], to[maxE], nxt[maxE], ec;

struct Node {
	int u, w;
	LL p;
	bool operator < (const Node&rhs) const {
		return w > rhs.w;
	}
	Node() {}
	Node(int u, int w, LL p):u(u), w(w), p(p) {}
};

priority_queue<Node> que;

vector<int> adj[maxN];
int dis[maxN];

int main() {
#ifdef lol
	freopen("hd.in", "r", stdin);
	freopen("hd.out", "w", stdout);
#endif

	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; ++i)
		scanf("%d", &c[i-1]);
	ec = 0;
	memset(h, -1, sizeof h);
	for (int i = 1; i <= m; ++i) {
		int u, v;
		scanf("%d %d", &u, &v);
		--u, --v;
		adj[u].pb(v);
		adj[v].pb(u);
		to[ec] = v, nxt[ec] = h[u], h[u] = ec++;
		to[ec] = u, nxt[ec] = h[v], h[v] = ec++;
	}

	que.push(Node(0, c[0], 1LL));
	int ans = INF;
	
	while (!que.empty()) {
		int u = que.top().u;
		int w = que.top().w;
		LL p = que.top().p;
		que.pop();
		for (int i = h[u]; i != -1; i = nxt[i]) {
			int v = to[i];
			int vw = w;
			LL vp = p;
			if (!((vp>>v)&1)) {
				for (int j = 0; j < (int)adj[u].size(); ++j) {
					if (!((vp>>adj[u][j])&1)) {
						vp |= 1LL<<adj[u][j];
						vw += c[adj[u][j]];
					}
				}
				que.push(Node(v, vw, vp));
				if (v == n-1) {
					for (int j = 0; j < (int)adj[v].size(); ++j) {
						if (!((vp>>adj[v][j])&1)) {
							vp |= 1LL<<adj[v][j];
							vw += c[adj[v][j]];
						}
					}
					ans = min(ans, vw);
				}
			}
		}
	}
	printf("%d\n", ans);

	return 0;
}