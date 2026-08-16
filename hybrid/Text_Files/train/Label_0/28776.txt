#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define valid(y,x,h,w) (0<=y&&y<h&&0<=x&&x<w)
#define tpl(...) make_tuple(__VA_ARGS__)
const int INF = 0x3f3f3f3f;
const double EPS = 1e-8;
const double PI = acos(-1);
typedef long long ll;
typedef pair<int,int> pii;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
template<class T>ostream&operator<<(ostream &o,const vector<T>&t){o<<'[';FOR(i,t){if(i!=t.begin())o<<',';o<<*i;}return o<<']';}
template<class S,class T>ostream&operator<<(ostream &o,const pair<S,T>&t){return o<<'('<<t.first<<','<<t.second<<')';}
template<int N,class Tp>void output(ostream&,const Tp&){}
template<int N,class Tp,class,class ...Ts>void output(ostream &o,const Tp&t){if(N)o<<',';o<<get<N>(t);output<N+1,Tp,Ts...>(o,t);}
template<class ...Ts>ostream&operator<<(ostream&o,const tuple<Ts...>&t){o<<'(';output<0,tuple<Ts...>,Ts...>(o,t);return o<<')';}
template<class T>void output(T t,char z=10){if(t<0)t=-t,putchar(45);int c[20];
int k=0;while(t)c[k++]=t%10,t/=10;for(k||(c[k++]=0);k;)putchar(c[--k]^48);putchar(z);}
template<class T>void outputs(T t){output(t);}
template<class S,class ...T>void outputs(S a,T...t){output(a,32);outputs(t...);}
template<class T>void output(T *a,int n){REP(i,n)output(a[i],i!=n-1?',':10);}
template<class T>void output(T *a,int n,int m){REP(i,n)output(a[i],m);}
template<class T>bool input(T &t){int n=1,c;for(t=0;!isdigit(c=getchar())&&~c&&c-45;);
if(!~c)return 0;for(c-45&&(n=0,t=c^48);isdigit(c=getchar());)t=10*t+c-48;t=n?-t:t;return 1;}
template<class S,class ...T>bool input(S&a,T&...t){input(a);return input(t...);}

const int MAX_V = 100000;
const int MAX_E = 100000;
// T : define {T+T, T<T, int*T}
template<class T> 
struct MinCostFlow {
  struct Edge {
    int s,t,cap;
    T cost;
    int next;
    Edge(){}
    Edge(int s, int t, int cap, T cost, int next) : s(s),t(t),cap(cap),cost(cost),next(next) {}
  };
  int n;
  Edge edge[MAX_E+10];
  int head[MAX_V+10];
  int cnt;
  void add_edge(int s, int t, int cap, T cost) {
    edge[cnt] = Edge(s,t,cap,cost,head[s]); head[s] = cnt++;
    edge[cnt] = Edge(t,s,0,-cost,head[t]); head[t] = cnt++;
  }
  T zero, inf;
  void init(int _n, T _zero, T _inf) {
    n = _n;
    REP(i,n) head[i] = 0;
    zero = _zero;
    inf = _inf;
    cnt = 2;
  }
  T dis[MAX_V];
  int inQ[MAX_V],pre[MAX_V];
  bool spfa(int s, int t) {
    queue<int> Q;
    REP(i,n) dis[i] = inf, inQ[i] = 0;
    for (dis[s]=zero,inQ[s]=1,Q.push(s); !Q.empty(); ) {
      int v = Q.front(); Q.pop();
      inQ[v] = 0;
      for (int k=head[v]; k; k=edge[k].next) {
        int u = edge[k].t;
        if (edge[k].cap && chmin(dis[u],dis[v]+edge[k].cost)) {
          pre[u] = k;
          if (!inQ[u]) inQ[u] = 1, Q.push(u);
        }
      }
    }
    return dis[t] < inf;
  }
  T minCost;
  pair<T,int> run(int s, int t, int F=INF) {
    pair<T,int> res(zero, 0);
    minCost = zero;
    while(F&&spfa(s,t)) {
      int f = F;
      for (int v=t; v!=s; v=edge[pre[v]].s)
        chmin(f, edge[pre[v]].cap);
      for (int v=t; v!=s; v=edge[pre[v]].s) {
        res.first += edge[pre[v]].cost * f;
        edge[pre[v]].cap -= f;
        edge[pre[v]^1].cap += f;
      }
      F -= f;
      res.second += f;
      chmin(minCost, res.first);
    }
    return res;
  }
};

template<class T, int N>
struct Vector {
  T v[N];
  int n;
  T& operator[](int i) { return v[i]; }
  const T operator[](int i) const { return v[i]; }
  Vector() : n(0) {}
  Vector(int n) : n(n) { REP(i,n)v[i]=0; }
  Vector(const initializer_list<T> &u) : n(0) { for(auto&i:u)v[n++]=i; }
  Vector(int n, const T &x) : n(n) { REP(i,n) v[i]=x; }
  Vector& operator+=(const Vector &u) { REP(i,n)v[i]+=u[i]; return *this; }
  Vector& operator-=(const Vector &u) { REP(i,n)v[i]-=u[i]; return *this; }
  Vector operator+(const Vector &u) const { return Vector(*this)+=u; }
  Vector operator-(const Vector &u) const { return Vector(*this)-=u; }
  Vector operator*=(const T &x) { REP(i,n)v[i]*=x; return *this; }
  Vector operator*(const T &x) const { return Vector(*this)*=x; }
  Vector operator-() const { Vector res(n); REP(i,n) res[i]=-v[i]; return res; }
  bool operator<(const Vector &u) const { REP(i,n) if (v[i]!=u[i]) return v[i]<u[i]; return 0; }
  // bool operator>(const Vector &u) const { return u<v; }
  bool operator==(const Vector &u) const { REP(i,n) if (v[i]!=u[i]) return 0; return 1;}
  friend ostream& operator<<(ostream &os, const Vector& v) { return os<<vector<T>{v.v,v.v+v.n}; }
};

typedef Vector<int,3> Vec;

int g1[100][100];
int g2[100][100];
int g3[100][100];
int g4[100][100];

void inp(int g[100][100]) {
  int L;
  cin >> L;
  REP(i,L) {
    int a,b;
    input(a,b);
    g[a][b] = 1;
  }
}

int main() {
  int n,m;
  while(input(n,m)) {
    REP(i,n)REP(j,n) {
      g1[i][j]=g2[i][j]=g3[i][j]=g4[i][j]=0;
    }
    inp(g1);
    inp(g2);
    inp(g3);
    inp(g4);
    static MinCostFlow<Vec> mcf;
    mcf.init(n+m+2, {0,0,0}, {INF,INF,INF});
    REP(i,n) REP(j,m) {
      if (g1[i][j] && g3[j][i]) {
        mcf.add_edge(i, n+j, 1, {-1,0,0});
      } else if (g1[i][j] && g4[j][i] || g2[i][j] && g3[j][i]) {
        mcf.add_edge(i, n+j, 1, {0,-1,0});
      } else if (g2[i][j] && g4[j][i]) {
        mcf.add_edge(i, n+j, 1, {0,0,-1});
      }
    }
    REP(i,n) mcf.add_edge(n+m,i,1,{0,0,0});
    REP(i,m) mcf.add_edge(n+i,n+m+1,1,{0,0,0});
    mcf.run(n+m,n+m+1);
    Vec cost = mcf.minCost;
    // cout << cost << endl;
    outputs(-cost[0], -cost[1], -cost[2]);
  }
}
