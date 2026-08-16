#include <bits/stdc++.h>
#define whlie while
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define rep(i,N) for(int i = 0; i < (N); i++)
#define repr(i,N) for(int i = (N) - 1; i >= 0; i--)
#define rep1(i,N) for(int i = 1; i <= (N) ; i++)
#define repr1(i,N) for(int i = (N) ; i > 0 ; i--)
#define each(x,v) for(auto& x : v)
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v).size())
#define vrep(v,it) for(auto it = v.begin(); it != v.end(); it++)
#define vrepr(v,it) for(auto it = v.rbegin(); it != v.rend(); it++)
#define ini(...) int __VA_ARGS__; in(__VA_ARGS__)
#define inl(...) ll __VA_ARGS__; in(__VA_ARGS__)
#define ins(...) string __VA_ARGS__; in(__VA_ARGS__)
using namespace std; void solve();
using ll = long long; using vl = vector<ll>;
using vi = vector<int>; using vvi = vector< vector<int> >;
constexpr int inf = 1001001001;
constexpr ll infLL = (1LL << 61) - 1;
struct IoSetupNya {IoSetupNya() { cin.tie(nullptr); ios::sync_with_stdio(false); cout << fixed << setprecision(15); cerr << fixed << setprecision(7);} } iosetupnya;
template<typename T, typename U> inline bool amin(T &x, U y) { return (y < x) ? (x = y, true) : false; }
template<typename T, typename U> inline bool amax(T &x, U y) { return (x < y) ? (x = y, true) : false; }
template<typename T, typename U> ostream& operator <<(ostream& os, const pair<T, U> &p) { os << p.first << " " << p.second; return os; }
template<typename T, typename U> istream& operator >>(istream& is, pair<T, U> &p) { is >> p.first >> p.second; return is; }
template<typename T> ostream& operator <<(ostream& os, const vector<T> &v) { int s = (int)v.size(); rep(i,s) os << (i ? " " : "") << v[i]; return os; }
template<typename T> istream& operator >>(istream& is, vector<T> &v) { for(auto &x : v) is >> x; return is; }
void in(){} template <typename T,class... U> void in(T &t,U &...u){ cin >> t; in(u...);}
void out(){cout << "\n";} template <typename T,class... U> void out(const T &t,const U &...u){ cout << t; if(sizeof...(u)) cout << " "; out(u...);}
template<typename T>void die(T x){out(x); exit(0);}
#ifdef NyaanDebug
  #include "NyaanDebug.h"
  #define trc(...) do { cerr << #__VA_ARGS__ << " = "; dbg_out(__VA_ARGS__);} while(0)
  #define trca(v,...) do { cerr << #v << " = "; array_out(v , __VA_ARGS__ );} while(0)
#else
  #define trc(...)
  #define trca(...)
  int main(){solve();}
#endif

constexpr int MOD = /** 1000000007; //*/ 998244353;
/////////////////

template< typename G >
struct StronglyConnectedComponents {
  using UnWeightedGraph = vvi;
  const G &g;
  UnWeightedGraph gg, rg;
  vector< int > comp, order, used;

  StronglyConnectedComponents(G &g) : g(g), gg(g.size()), rg(g.size()), comp(g.size(), -1), used(g.size()) {
    for(int i = 0; i < (int)g.size(); i++) {
      for(auto e : g[i]) {
        gg[i].emplace_back((int) e);
        rg[(int) e].emplace_back(i);
      }
    }
  }

  int operator[](int k) {
    return comp[k];
  }

  void dfs(int idx) {
    if(used[idx]) return;
    used[idx] = true;
    for(int to : gg[idx]) dfs(to);
    order.push_back(idx);
  }

  void rdfs(int idx, int cnt) {
    if(comp[idx] != -1) return;
    comp[idx] = cnt;
    for(int to : rg[idx]) rdfs(to, cnt);
  }

  void build(UnWeightedGraph &t) {
    for(int i = 0; i < (int)gg.size(); i++) dfs(i);
    reverse(begin(order), end(order));
    int ptr = 0;
    for(int i : order) if(comp[i] == -1) rdfs(i, ptr), ptr++;

    t.resize(ptr);
    for(int i = 0; i < (int)g.size(); i++) {
      for(auto &to : g[i]) {
        int x = comp[i], y = comp[to];
        if(x == y) continue;
        t[x].push_back(y);
      }
    }
  }
};

using P = pair<int,int>;
using vp= vector<P>;

vp data(int x,int y,int z){
  vp ret = {
    P(x+y+z , x+y+z) ,
    P(x+y-z , x+y-z) ,
    P(x-y+z , x-y+z) ,
    P(x-y-z , x-y-z)
  };
  return ret;
}

vp dataini(){
  vp ret;
  rep(i,4) ret.eb(-inf , inf);
  return ret;
}

ll evaldata(vp data , int x,int y,int z){
  ll ret = 0;
  amax(ret, abs(x+y+z - data[0].fi));
  amax(ret, abs(x+y+z - data[0].se));
  amax(ret, abs(x+y-z - data[1].fi));
  amax(ret, abs(x+y-z - data[1].se));
  amax(ret, abs(x-y+z - data[2].fi));
  amax(ret, abs(x-y+z - data[2].se));
  amax(ret, abs(x-y-z - data[3].fi));
  amax(ret, abs(x-y-z - data[3].se));
  return ret;
}

void merge(vp &cur , vp &add){
  rep(i,4){
    cur[i].fi = max(cur[i].fi , add[i].fi );
    cur[i].se = min(cur[i].se , add[i].se );
  }
}

void solve(){
  int N,M; in(N , M);
  vi x(N) , y(N) , z(N);
  rep(i,N) in(x[i] , y[i] , z[i]);
  vvi g(N);
  rep(i,M){
    ini(x,y); x--; y--;
    g[x].pb(y);
  }
  StronglyConnectedComponents<vvi> scc(g);
  vvi t;
  scc.build(t);
  int T = sz(t);
  vector<vp>memo(T);
  rep(i,T){ memo[i] = dataini();}
  rep(i,N){
    vp cur = data(x[i],y[i],z[i]);
    merge( memo[scc[i]] , cur );
  }
  

  vvi inv(T);
  rep(i,T) each(x , t[i]) inv[x].pb(i);
  repr(i , T){
    each(x , inv[i]) merge(memo[x] , memo[i]);
  }
  rep(i,T) trc(memo[i]);
  vl ans(T , 0);

  rep(i,N) out( evaldata(memo[scc[i]] , x[i],y[i],z[i]) );

  

}
