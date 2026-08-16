#include <bits/stdc++.h> // {{{

#define ARG5(a, b, c, d, NAME, ...) NAME
#define REP(...) ARG5(__VA_ARGS__, REP4, REP3, REP2, REP1)(__VA_ARGS__)
#define REP1(a) REP2(i, a)
#define REP2(i, a) REP3(i, 0, a)
#define REP3(i, a, b) REP4(i, a, b, 1)
#define REP4(i, a, b, s) for (int i = (a); i < (int)(b); i += (s))
#define REPR(...) ARG5(__VA_ARGS__, REPR4, REPR3, REPR2, REPR1)(__VA_ARGS__)
#define REPR1(a) REPR2(i, a)
#define REPR2(i, a) REPR3(i, 0, a)
#define REPR3(i, a, b) REPR4(i, a, b, 1)
#define REPR4(i, a, b, s) for (int i = (b)-1; i >= (int)(a); i -= (s))
#define ALL(c) (c).begin(), (c).end()
#define DUMP(x) (std::cerr << #x << ':' << ' ' << x << '\n')
#define TMPL_T template <typename T>
#define TMPL_TU template <typename T, typename U>
#define mut auto
#define let const auto

using Int = long long;
// clang-format off
namespace extio {
std::string delimiter=" ",pdelimiter=" ";
std::string bracket_b="",bracket_e="";
void chdelim(const std::string&s){delimiter=s;}
void chpdelim(const std::string&s){pdelimiter=s;}
void chbracket(const std::string&b,const std::string&e){bracket_b=b,bracket_e=e;}
TMPL_T  void pcont(std::ostream&os,const T&x){int c=0;for(const auto&a:x){if(c++)os<<delimiter;os<<a;}}
TMPL_TU void ppair(std::ostream&os,const std::pair<T,U>&p){os<<bracket_b<<p.first<<pdelimiter<<p.second<<bracket_e;}
}
namespace std {
TMPL_T ostream& operator<<(ostream&os,const vector<T>&x){extio::pcont(os,x);return os;}
TMPL_T ostream& operator<<(ostream&os,const set<T>&x){extio::pcont(os,x);return os;}
TMPL_T ostream& operator<<(ostream&os,const multiset<T>&x){extio::pcont(os,x);return os;}
TMPL_T ostream& operator<<(ostream&os,const deque<T>&x){extio::pcont(os,x);return os;}
TMPL_TU ostream& operator<<(ostream&os,const map<T,U>&x){extio::pcont(os,x);return os;}
TMPL_TU ostream& operator<<(ostream&os,const pair<T,U>&x){extio::ppair(os,x);return os;}
}
TMPL_TU inline bool chmax(T&x,U a){return x<a&&(x=a,1);}
TMPL_TU inline bool chmin(T&x,U a){return a<x&&(x=a,1);}

inline int in(){int x;std::cin>>x;return x;}
TMPL_T void read_seq(int N,std::vector<T>&v){v.reserve(N+2);REP(N){T x;std::cin>>x;v.emplace_back(x);}}
TMPL_T void read_seq(int N,T*v){REP(N)std::cin>>v[i];}

struct Initializer_{
  Initializer_(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(0);
    std::cout<<std::setprecision(10);
    std::cerr<<std::setprecision(10);
  }
} precalc;
// clang-format on
// }}}

#define int long long

using namespace std;

struct Edge {
  int to, cost, time, company;
};
using Graph = vector<vector<Edge>>;

const int INF = std::numeric_limits<int>::max() >> 2;

int dijkstra(const Graph& g, int s, int t, int freec, int H) {
  struct State {
    int cost;
    int time;
    int v;
    State(int cost, int time, int v) : cost(cost), time(time), v(v) {}
    bool operator<(const State& rhs) const {
      if (cost != rhs.cost) return cost > rhs.cost;
      if (time != rhs.time) return time > rhs.time;
      return v < rhs.v;
    }
  };
  const int V = g.size();
  int vis[128][32] = {};
  priority_queue<State> pq;
  pq.emplace(0, 0, s);
  while (not pq.empty()) {
    State st = pq.top();
    pq.pop();
    if (st.v == t) return st.cost;
    if (vis[st.v][st.time]++) continue;
    for (let& e : g[st.v]) {
      if (st.time + e.time > H) continue;
      if (freec & (1 << e.company)) {
        // if (chmin(minic[e.to][st.time + e.time], st.cost))
        pq.emplace(st.cost, st.time + e.time, e.to);
      } else {
        // if (chmin(minic[e.to][st.time + e.time], st.cost + e.cost))
        pq.emplace(st.cost + e.cost, st.time + e.time, e.to);
      }
    }
  }
  return INF;
}

signed main() {
  int N, M, H, K;
  while (N = in(), M = in(), H = in(), K = in(), N || M || H || K) {
    Graph G(N);
    REP(M) {
      int a = in() - 1, b = in() - 1, c = in(), h = in(), r = in() - 1;
      G[a].push_back((Edge){b, c, h, r});
      G[b].push_back((Edge){a, c, h, r});
    }
    int S = in() - 1, T = in() - 1;
    int P = in();
    int bit[512] = {};
    int pcost[512];
    REP(i, P) {
      int L = in();
      pcost[i] = in();
      REP(j, L) {
        int k = in() - 1;
        bit[i] |= 1 << k;
      }
    }
    int dp[512];
    REP(i, 512) dp[i] = INF;
    dp[0] = 0;
    REP(p, P) REP(st, 256) { chmin(dp[st | bit[p]], dp[st] + pcost[p]); }
    int mini = INF;
    REP(st, 1 << K) { chmin(mini, dijkstra(G, S, T, st, H) + dp[st]); }
    if (mini == INF) {
      cout << -1 << endl;
    } else {
      cout << mini << endl;
    }
  }
  return 0;
}