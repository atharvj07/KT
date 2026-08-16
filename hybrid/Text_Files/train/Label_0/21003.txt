#include <bits/stdc++.h>
using namespace std;
#define FOR(i,k,n) for(int i = (k); i < (n); i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(), a.end()
#define MS(m,v) memset(m,v,sizeof(m))
#define D10 fixed<<setprecision(10)
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
const int MOD = 1000000007;
const int INF = 10000000;
const ld EPS = 1e-12;
template<class T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template<class T> T &chmax(T &a, const T &b) { return a = max(a, b); }

/*--------------------template--------------------*/

typedef int Weight;
typedef int Flow;
struct Edge {
	int src, dest, rev;
	Flow cap;
	Weight cost;
	bool operator < (const Edge &rhs) const
	{
		return cost > rhs.cost;
	}
	Edge(int s, int d) : src(s), dest(d) { ; }
	Edge(int s, int d, int c) : src(s), dest(d), cost(c) { ; }
	Edge(int s, int d, int r, Flow cp, Weight cst) : src(s), dest(d), rev(r), cap(cp), cost(cst) { ; }
};
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;
typedef vector<Weight> Array;
typedef vector<Array> Matrix;
void add_edge(Graph &g, int src, int dest, Flow cap)
{
	g[src].push_back(Edge{ src, dest, (int)g[dest].size(), cap, 0 });
	g[dest].push_back(Edge{ dest, src, (int)g[src].size() - 1, 0, 0 });
}

void add_edge(Graph &g, int from, int to, Flow cap, Weight cost)
{
	g[from].push_back(Edge(from, to, (int)g[to].size(), cap, cost));
	g[to].push_back(Edge(to, from, (int)g[from].size() - 1, 0, -cost));
}

Weight mincost_flow(Graph &g, int s, int t, Flow f)
{
	const int n = g.size();
	Weight res = 0;
	Array dist(n);
	vi prevv(n), preve(n);
	while (f > 0)
	{
		REP(i, n) dist[i] = (i == s) ? 0 : INF;
		bool update = true;
		while (update)
		{
			update = false;
			for (int v = 0; v < n; v++)
			{
				if (dist[v] == INF) continue;
				REP(i, g[v].size())
				{
					Edge& e = g[v][i];
					if (e.cap > 0 && dist[e.dest] > dist[v] + e.cost)
					{
						dist[e.dest] = dist[v] + e.cost;
						prevv[e.dest] = v;
						preve[e.dest] = i;
						update = true;
					}
				}
			}
		}
		if (dist[t] == INF) return -1; // cannot flow
		Flow d = f;
		for (int v = t; v != s; v = prevv[v])
		{
			d = min(d, g[prevv[v]][preve[v]].cap);
		}
		f -= d;
		res += d * dist[t];
		for (int v = t; v != s; v = prevv[v])
		{
			Edge &e = g[prevv[v]][preve[v]];
			e.cap -= d;
			g[v][e.rev].cap += d;
		}
	}
	return res;
}


int main()
{
	int n; cin >> n;
	vi a(n), b(n);
	map<int, int> mp;
	int wid = 0;
	REP(i, n)
	{
		cin >> a[i]>> b[i];
		if (!mp.count(a[i])) mp[a[i]] = wid++;
		if (!mp.count(b[i])) mp[b[i]] = wid++;
	}
	Graph g(n + mp.size() + 2);
	int V = g.size();
	REP(i, n)
	{
		add_edge(g, V - 2, i, 1, 0);
		add_edge(g, i, V - 1, INF, 0);
		add_edge(g, i, n + mp[a[i]], 1, -b[i]);
		add_edge(g, i, n + mp[b[i]], 1, -a[i]);
	}
	REP(i, wid) add_edge(g, n + i, V - 1, 1, 0);
	cout << -mincost_flow(g, V - 2, V - 1, n) << endl;
	return 0;
}