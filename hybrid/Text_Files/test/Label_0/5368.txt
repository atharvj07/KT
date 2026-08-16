// #define _GLIBCXX_DEBUG // for STL debug (optional)
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>
#include <set>
#include <complex>
#include <cmath>
#include <limits>
#include <cfloat>
#include <climits>
#include <ctime>
#include <cassert>
#include <numeric>
#include <fstream>
#include <functional>
#include <bitset>
using namespace std;

#define debug(...) fprintf(stderr, __VA_ARGS__)
#define int long long int
 
template<typename T> void chmax(T &a, T b) {a = max(a, b);}
template<typename T> void chmin(T &a, T b) {a = min(a, b);}
template<typename T> void chadd(T &a, T b) {a = a + b;}
 
typedef pair<int, int> pii;
typedef long long ll;
 
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
const ll INF = 1001001001001001LL;
const ll MOD = 1000000007LL;

// Dinic を信じろ

template <typename T>
struct Edge {
    int to; T cap, cost; int rev;
    Edge(int t, T c, int r) : to(t), cap(c), rev(r) {}
    Edge(int t, T ca, T co, int r) : to(t), cap(ca), cost(co), rev(r) {}
};

template <typename T>
using Graph = vector< vector< Edge<T> > >;

template<typename T>
struct Dinic {
    int N, M;
    Graph<T> G;
    vector<int> level, iter;
    Dinic(int n, int m = 0) : N(n), M(m) {
        G.resize(N);
        level.resize(N);
        iter.resize(N);
    }
    void add_edge(int from, int to, T cost) {
        G[from].push_back(Edge<T>(to  , cost, G[to  ].size()    ));
        G[to  ].push_back(Edge<T>(from, 0.0 , G[from].size() - 1));
    }
    void readGraph() {
        for(int i=0; i<M; i++) {
            int a, b; T c;
            cin >> a >> b >> c;
            // a--; b--;
            add_edge(a, b, c);
        }
    }
    void bfs(int s) {
        fill(level.begin(), level.end(), -1);
        queue<int> que; que.push(s);
        level[s] = 0;
        while(!que.empty()) {
            int temp = que.front(); que.pop();
            for(size_t i=0; i<G[temp].size(); i++) {
                Edge<T> &e = G[temp][i];
                if(e.cap > 0 && level[e.to] < 0) {
                    level[e.to] = level[temp] + 1;
                    que.push(e.to);
                }
            }
        }
    }
    T dfs(int v, int t, T f) {
        if(v == t) return f;
        for(int &i = iter[v]; i<(int)G[v].size(); i++) {
            Edge<T> &e = G[v][i];
            if(e.cap > 0 && level[v] < level[e.to]) {
                T d = dfs(e.to, t, min(f, e.cap));
                if(d > 0) {
                    e.cap -= d;
                    G[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }
    T max_flow(int s, int t) {
        T flow = 0.0, f;
        while(1) {
            bfs(s);
            if(level[t] < 0) return flow;
            fill(iter.begin(), iter.end(), 0);
            while( (f = dfs(s, t, INF)) > 0 ) flow += f;
        }
    }
};

// 最小流量制約付きフロー
// u から v に最小 lb, 最大 ub 流す
template<typename flow_type>
struct Dinic_lr {
    Dinic<flow_type> fl;
    int S, T;
    flow_type sum_lb;

    Dinic_lr() {}
    Dinic_lr(int N) : fl(N+2, 0), S(N), T(N+1), sum_lb(0) {}

    void add_edge(int u, int v, flow_type lb, flow_type ub) {
        assert(0 <= lb && lb <= ub);
        if(u == v || ub == 0) return;
        fl.add_edge(u, v, ub - lb);
        fl.add_edge(S, v, lb);
        fl.add_edge(u, T, lb);
        sum_lb += lb;
    }

    flow_type max_flow(int s, int t) {
        flow_type a = fl.max_flow(S, T);
        flow_type b = fl.max_flow(s, T);
        flow_type c = fl.max_flow(S, t);
        flow_type d = fl.max_flow(s, t);
        return (a + c == sum_lb && a + b == sum_lb) ? b + d : -1;
    }
};

signed main() {
    int N, M; cin >> N >> M;

    vector< pair<int, int> > edges;
    for(int i=0; i<M; i++) {
        int a, b; cin >> a >> b;
        a--; b--;

        Dinic<int> fl(2 + 2 * N);
        int source = 2*N, sink = source + 1;
        fl.add_edge(source, 2*a, 1);
        fl.add_edge(source, 2*b, 1);
        fl.add_edge(1, sink, 2);

        for(int i=0; i<N; i++) {
            fl.add_edge(2*i, 2*i + 1, 1 + (i == 0));
        }
        for(auto e : edges) {
            int u, v; tie(u, v) = e;
            fl.add_edge(2*u + 1, 2*v, 1);
            fl.add_edge(2*v + 1, 2*u, 1);
        }

        edges.emplace_back(a, b);

        int f = fl.max_flow(source, sink);
        if(f == 2) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
    return 0;
}

