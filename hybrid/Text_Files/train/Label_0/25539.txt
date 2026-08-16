#include<algorithm>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<map>
#include<numeric>
#include<queue>
#include<vector>
#include<set>
#include<string>
#include<stack>
#include<sstream>
#include<complex>

#define pb push_back
#define clr clear()
#define sz size()
#define fs first
#define sc second

#define rep(i,a) for(int i=0;i<(int)(a);i++)
#define rrep(i,a) for(int i=(int)(a)−1;i>=0;i−−)
#define all(a) (a).begin(),(a).end()
#define EQ(a,b) (abs((a)−(b)) < EPS)
#define INIT(a) memset(a,0,sizeof(a))

using namespace std;
typedef double D;
typedef pair<D,int> P;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

const D EPS = 1e-7;
const D INF = 1e9;
const D PI = acos(-1);

typedef vector<D> vec;
typedef vector<vec> mat;

struct matrix{
  mat m;
  int r,c;
  matrix(void){r=c=0;m.clr;}
  matrix(mat a){
    r = a.sz; c = a[0].sz;
    m.resize(r);
    rep(i,r)m[i].resize(c);
    rep(i,r)rep(j,c)m[i][j] = a[i][j];
  }

  matrix operator+(matrix a){
    if(r==a.r && c==a.c){
      rep(i,r)rep(j,c)a.m[i][j] += m[i][j];
    }
    return a;
  }

  matrix operator-(matrix a){
    rep(i,a.r)rep(j,a.c)a.m[i][j] *= -1;
    return *this+a;
  }

  matrix operator*(matrix a){
    matrix x;
    if(c==a.r){
      x.r = r; x.c = a.c;
      x.m.resize(r);
      rep(i,r)x.m[i].resize(a.c);
      rep(i,r)rep(j,a.c){
	x.m[i][j] = 0;
	rep(k,c)x.m[i][j] += m[i][k] * a.m[k][j];
      }
    }
    return x;
  }
};

vec gauss_jordan(const mat& A, const vec& b){
  int n = A.size();
  mat B(n,vec(n+1));
  rep(i,n)rep(j,n)B[i][j] = A[i][j];
  rep(i,n)B[i][n] = b[i];
  rep(i,n){
    int p=i;
    for(int j=i;j<n;j++)
      if(abs(B[j][i]) > abs(B[p][i]))p = j;
    swap(B[i],B[p]);
    //解か&#12441;ないか、一意て&#12441;ない
    if(abs(B[i][i]) < EPS)return vec();
    for(int j=i+1;j<=n;j++)B[i][j] /= B[i][i];
    rep(j,n)
      if(i != j)
	for(int k=i+1;k<=n;k++)B[j][k] -= B[j][i] * B[i][k];
  }
  vec x(n);
  rep(i,n)x[i] = B[i][n];
  return x;
}

int T;
int N,s,t,F;
mat a;
vec b;

//辺の定義。必要に応し&#12441;て削る。
struct edge{
  int from,to,cap,rev;
  D cost;
  edge(int a=0,int b=0,D c=0,int d=0,int e=0):from(a),to(b),cost(c),cap(d),rev(e){}
};
int v; //ク&#12441;ラフの頂点数
vector<edge> G[110]; //ク&#12441;ラフの隣接リスト表現

//辺の追加。2つ目の辺の追加はフローアルコ&#12441;リス&#12441;ムの残余ク&#12441;ラフ用。 
void AddEdge(int s,int g, D c,int p){
  G[s].pb(edge(s,g,c,p,G[g].sz));
  G[g].pb(edge(g,s,-c,0,G[s].sz-1));
}

D d[110];
D h[110];
int pv[110],pe[110];

D MinCostFlow(int s,int t,int f){
  D res = 0;
  fill(h,h+v,0);
  while(f>0){
    priority_queue<P ,vector<P> ,greater<P> > q;
    fill(d,d+v,INF);
    d[s] = 0; q.push(P(0,s));

    while(q.sz){
      P p = q.top();q.pop();
      int u = p.second;
      if(d[u] > p.first+EPS)continue;
      rep(i,G[u].sz){
	edge &e = G[u][i];
	if(e.cap>0 && d[e.to] > d[u] + e.cost + h[u] - h[e.to] + EPS){
	  d[e.to] = d[u] + e.cost + h[u] - h[e.to];
	  pv[e.to] = u; pe[e.to] = i;
	  q.push(P(d[e.to],e.to));
	}
      }
    }

    if(d[t]==INF)return -1;
    rep(u,v)h[u] += d[u];
    int x = f;
    for(int u=t;u!=s;u=pv[u])x = min(x,G[pv[u]][pe[u]].cap);
    f-=x;
    res += x*h[t];
    for(int u=t;u!=s;u=pv[u]){
      edge &e = G[pv[u]][pe[u]];
      e.cap -= x;
      G[u][e.rev].cap += x;
    }
  }
  return res;
}

int M[110];
int to[110][110], f[110][110]; 

int main(){
  cin >> T;
  while(T--){
    cin >> N >> s >> t >> F;
    a.resize(N); b.resize(N);
    rep(i,N){
      a[i].resize(N);
      rep(j,N)cin >> a[i][j];
      cin >> b[i];
      G[i].clr;
    }

    vec temp = gauss_jordan(a,b);

    rep(i,N){
      cin >> M[i];
      rep(j,M[i])cin >> to[i][j];
      rep(j,M[i])cin >> f[i][j];

      rep(j,M[i]){
	AddEdge(i,to[i][j],abs(temp[i]-temp[to[i][j]]),f[i][j]);
      }
    }

    v = N;
    D ans = MinCostFlow(s,t,F);
    if(ans < EPS)cout << "impossible" << endl;
    else cout << fixed << setprecision(10) << ans << endl;
  }
}