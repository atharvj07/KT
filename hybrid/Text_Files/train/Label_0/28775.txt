#include <bits/stdc++.h>
using namespace std;

typedef long long weight;
typedef pair<weight, int> P;

struct edge {
  int to;
  int cap;
  weight cost;
  int rev;
  edge(int to_, int cap_, weight cost_, int rev_):to(to_), cap(cap_), cost(cost_), rev(rev_) {}
};

constexpr weight INF = (1ll << 55);

vector<vector<edge>> G;

void init(int V) {
  G.assign(V, vector<edge>());
}

void add_edge(int from, int to, int cap, weight cost) {
  G[from].emplace_back(to, cap, cost, G[to].size());
  G[to].emplace_back(from, 0, -cost, G[from].size() - 1);
}

weight min_cost_flow(int s, int t, int f) {
  const int n = G.size();
  weight res = 0;
  vector<int> prevv(n), preve(n);
  vector<weight> h(n, 0);

  while(f > 0) {
    priority_queue<P, vector<P>, greater<P>> que;
    vector<weight> dist(n, INF);
    dist[s] = 0;
    que.push({0, s});

    while(!que.empty()) {
      const auto d = que.top().first;
      const auto v = que.top().second;
      que.pop();

      if(dist[v] < d) continue;

      for(unsigned i = 0; i < G[v].size(); ++i) {
	const edge &e = G[v][i];
	if(e.cap > 0 && dist[e.to] > d + e.cost + h[v] - h[e.to]) {
	  dist[e.to] = d + e.cost + h[v] - h[e.to];
	  prevv[e.to] = v;
	  preve[e.to] = i;
	  que.push({dist[e.to], e.to});
	}
      }
    }

    if(dist[t] == INF) return -1;

    for(int v = 0; v < n; ++v) {
      h[v] += dist[v];
    }

    int d = f;
    for(int v = t; v != s; v = prevv[v]) {
      d = min(d, G[prevv[v]][preve[v]].cap);
    }

    f -= d;
    res += d * h[t];
    for(int v = t; v != s; v = prevv[v]) {
      edge &e = G[prevv[v]][preve[v]];
      e.cap -= d;
      G[v][e.rev].cap += d;
    }
  }

  return res;
}

constexpr weight DD = 1000000;
constexpr weight DS = 1000;
constexpr weight SS = 1;

inline void input(vector<vector<int>> &like, int v) {
  int l;
  cin >> l;

  for(int i = 0; i < l; ++i) {
    int a, b;
    cin >> a >> b;
    like[a][b] = v;
  }
}

int main() {
  int n, m;
  cin >> n >> m;

  vector<vector<int>> like_m(n, vector<int>(m, 0));
  vector<vector<int>> like_f(m, vector<int>(n, 0));

  input(like_m, 2);
  input(like_m, 1);
  input(like_f, 2);
  input(like_f, 1);

  const int source = n + m;
  const int sink = source + 1;
  init(sink + 1);

  for(int i = 0; i < n; ++i) {
    add_edge(source, i, 1, 0);
  }

  for(int i = 0; i < m; ++i) {
    add_edge(i + n, sink, 1, 0);
  }

  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < m; ++j) {
      if(like_m[i][j] && like_f[j][i]) {
	const int sum = like_m[i][j] + like_f[j][i];
	switch(sum) {
	case 4: add_edge(i, j + n, 1, -DD); break;
	case 3: add_edge(i, j + n, 1, -DS); break;
	case 2: add_edge(i, j + n, 1, -SS); break;
	default: assert(false);
	}
      }
      else {
	add_edge(i, j + n, 1, 0);
      }
    }
  }

  const weight ans = -min_cost_flow(source, sink, min(n, m));
  const long long dd = ans / DD;
  const long long ds = ans % DD / DS;
  const long long ss = ans % DS;

  cout << dd << " " << ds << " " << ss << endl;

  return EXIT_SUCCESS;
}
