#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <queue>
#include <functional>
#include <cstdio>
using namespace std;

const double eps = 1e-8;

bool equals(double a, double b) {
  return abs(a-b) < eps;
}

typedef vector<double> vec;
typedef vector<vec> mat;


vec gauss_jordan(const mat &A, const vec &b) {
  int n = A.size();
  mat B(n, vec(n+1));
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < n; ++j) {
      B[i][j] = A[i][j];
    }
  }

  for(int i = 0; i < n; ++i) B[i][n] = b[i];

  for(int i = 0; i < n; ++i) {
    int pivot = i;
    for(int j = i; j < n; ++j) {
      if(abs(B[j][i]) > abs(B[pivot][i])) pivot = j;
    }
    swap(B[i], B[pivot]);

    if(abs(B[i][i]) < eps) return vec();

    for(int j = i+1; j <= n; ++j) B[i][j] /= B[i][i];
    for(int j = 0; j < n; ++j) {
      if(i != j) {
        for(int k = i + 1; k <= n; ++k) {
          B[j][k] -= B[j][i] * B[i][k];
        }
      }
    }
  }
  vec x(n);
  for(int i = 0; i < n; ++i) {
    x[i] = B[i][n];
  }
  return x;
}


struct Edge {
  int to, cap, rev;
  double cost;
  Edge(int to, int cap, double cost, int rev)
    : to(to), cap(cap), cost(cost), rev(rev) {}
};

typedef pair<double, int> P;
const int MAX_N = 101;
const double inf = 1e80;

void addEdge(vector<Edge> G[], int from, int to, int cap, double cost) {
  G[from].push_back(Edge(to, cap, cost, G[to].size()));
  G[to].push_back(Edge(from, 0, -cost, (int)G[from].size()-1));
}

double min_cost_flow(int N, vector<Edge> G[], int s, int t, int f) {
  double res = 0;
  vector<double> h(N, 0.0);
  vector<int> prevv(N), preve(N);

  while(f > 0) {
    priority_queue<P, vector<P>, greater<P> > que;
    vector<double> dist(N, inf);
    dist[s] = 0.0;
    que.push(P(0.0, s));
    while(!que.empty()) {
      P p = que.top(); que.pop();
      int v = p.second;
      if(dist[v] < p.first) continue;
      for(int i = 0; i < G[v].size(); ++i) {
        Edge &e = G[v][i];
        double ndist = dist[v] + max(0.0, e.cost + h[v] - h[e.to]);
        if(e.cap > 0 && dist[e.to] > ndist) {
          dist[e.to] = ndist;
          prevv[e.to] = v;
          preve[e.to] = i;
          que.push(P(dist[e.to], e.to));
        }
      }
    }
    if(dist[t] == inf) {
      return -1;
    }
    for(int v = 0; v < N; ++v) h[v] += dist[v];

    int d = f;
    for(int v = t; v != s; v = prevv[v]) {
      d = min(d, G[prevv[v]][preve[v]].cap);
    }
    f -= d;
    res += d * h[t];
    for(int v = t; v != s; v = prevv[v]) {
      Edge &e = G[prevv[v]][preve[v]];
      e.cap -= d;
      G[v][e.rev].cap += d;
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  while(T--) {
    int n, s, t, F;
    cin >> n >> s >> t >> F;

    vector<vector<double> > A(n, vector<double>(n));
    vector<double> b(n);
    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < n; ++j) {
        cin >> A[i][j];
      }
      cin >> b[i];
    }
    vector<double> values = gauss_jordan(A, b);

    vector<Edge> G[MAX_N];
    for(int i = 0; i < n; ++i) {
      int m;
      cin >> m;
      vector<int> to(m), cap(m);
      for(int j = 0; j < m; ++j) cin >> to[j];
      for(int j = 0; j < m; ++j) cin >> cap[j];
      for(int j = 0; j < m; ++j) {
        addEdge(G, i, to[j], cap[j], abs(values[i] - values[to[j]]));
      }
    }
    double ans = min_cost_flow(n, G, s,t,F);

    if(ans == -1) printf("impossible\n");
    else printf("%.8f\n", ans);
  }
  return 0;
}