#include <bits/stdc++.h>

using namespace std;

#define REP(i,a,b) for(int i=a;i<(int)b;i++)
#define rep(i,n) REP(i,0,n)

typedef long double D;

struct edge { int to; D cap, cost; int rev; };
//int const INF = 1<<29;
double const Inf = 1e40;
int const Max = 300;
D h[Max], dist[Max];
int prevv[Max], preve[Max];

int V;

vector<edge> G[Max];

inline void add_edge(int f, int t, D cap, D cost) {
  G[f].push_back((edge){t, cap, cost, (int)G[t].size()});
  G[t].push_back((edge){f, 0, -cost, (int)G[f].size()-1});
}

double const INF = 1e40;
long double const EPS = 1e-5;

typedef pair<D, int> P;

D min_cost_flow(int S, int T, D f) {
  D ret = 0;
  fill(h, h+V, 0);
  while(f > 0) {
    priority_queue<P, vector<P>, greater<P> > pq;
    fill(dist, dist+V, INF);
    dist[S] = 0;
    pq.push(P(0, S));
    while(!pq.empty()) {
      D cost = pq.top().first;
      int curr = pq.top().second; pq.pop();
      if(dist[curr] < cost) { continue; }
      rep(i, G[curr].size()) {
	edge& e = G[curr][i];
	if(e.cap > EPS && dist[e.to] > dist[curr] + e.cost + h[curr] - h[e.to] + EPS) {
	  dist[e.to] = dist[curr] + e.cost + h[curr] - h[e.to];
	  prevv[e.to] = curr;
	  preve[e.to] = i;
	  pq.push(P(dist[e.to], e.to));
	}
      }
    }
    
    if(dist[T] == INF) { return -1; }
    
    rep(i, V) h[i] += dist[i];
    
    D d = f;
    for(int v = T; v!=S; v=prevv[v]) {
      d = min(d, G[prevv[v]][preve[v]].cap);
    }
    
    f -= d;
    ret += d*h[T];
    
    for(int v=T; v!=S; v=prevv[v]) {
      edge& e = G[prevv[v]][preve[v]];
      e.cap -= d;
      G[v][e.rev].cap += d;
    }
  }
  
  return ret;
}

template<class T>
vector<T> gauss_jordan(vector<vector<T> > const& A, vector<T> const& b) {
  int N = A.size();
  vector<vector<T> > B(A);
  rep(i, B.size()) B[i].resize(N+1);
  rep(i, N) B[i][N] = b[i];
  rep(i, N) {
    int pivot = i;
    REP(j, i, N) {
      if(abs(B[pivot][i]) < abs(B[j][i])) {
	pivot = j;
      }
    }
    swap(B[i], B[pivot]);
    
    if(abs(B[i][i]) < EPS) { return vector<T>(); }
    
    REP(j, i+1, N+1) { B[i][j] /= B[i][i]; }
    rep(j, N) if(i != j) {
      REP(k, i+1, N+2) B[j][k] -= B[j][i] * B[i][k];
    }
  }
  vector<T> x(N);
  rep(i, N) x[i] = B[i][N];
  return x;
}

typedef vector<D> Vec;
typedef vector<Vec> Mat;

int main() {
  
  int Tc; cin >> Tc;
  while(Tc--) {
    int N, s, t; D F; cin >> N >> s >> t >> F;
    V = N;
    rep(i, N) G[i].clear();
    
    Mat A(N, Vec(N)); Vec b(N);
    rep(i, N) {
      rep(j, N) {
	cin >> A[i][j];
      }
      cin >> b[i];
    }
    
    Vec X(gauss_jordan(A, b));
    
    rep(i, N) {
      int M; cin >> M;
      vector<int> ds(M);
      rep(j, M) { cin >> ds[j]; }
      rep(j, M) {
	D f; cin >> f;
	//	cerr << i << " -> " << ds[j] << endl;
	add_edge(i, ds[j], f, abs(X[i]-X[ds[j]]));
      }
    }
    
    D r = min_cost_flow(s, t, F);
    if(r < EPS) {
      cout << "impossible\n";
    }
    else {
      printf("%.10Lf\n", r);
    }
  }
  
  return 0;
}