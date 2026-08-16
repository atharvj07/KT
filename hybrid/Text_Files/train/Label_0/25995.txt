#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;

#define EACH(i,a) for (auto& i : a)
#define FOR(i,a,b) for (ll i = (a); i < (b); ++i)
#define RFOR(i,a,b) for (ll i = (b)-1; i >= (a); --i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,0,n)
#define pb push_back
#define ALL(a) (a).begin(),(a).end()

const ll linf = 1e18;
const int inf = 1e9;
const double eps = 1e-12;
const double pi = acos(-1);

template<typename T>
istream& operator>>(istream& is, vector<T>& vec) {
    EACH(x,vec)is>>x;
    return is;
}
template<typename T>
ostream& operator<<(ostream& os, vector<T>& vec) {
    REP(i, vec.size()) {
        if(i) os << " ";
        os << vec[i];
    }
    return os;
}

struct Edge {
    ll to, cap, rev;
};
vector< vector<Edge> > G;

void add_edge(ll from, ll to, ll cap) {
    G[from].pb({to, cap, (ll)G[to].size()});
    G[to].pb({from, 0, (ll)G[from].size()-1});
}
ll dfs(ll v, ll t, ll f, const vector<ll>& dist) {
    if (v == t) return f;
    EACH(e, G[v]) {
        if (e.cap > 0 && dist[e.to] == dist[v]+1) {
            ll d = dfs(e.to, t, min(f, e.cap), dist);
            if (d > 0) {
                e.cap -= d;
                G[e.to][e.rev].cap += d;
                return d;
            }
        }
    }
    return 0;
}
vector<ll> bfs(ll s) {
    vector<ll> res(G.size(), linf);
    res[s] = 0;
    queue<ll> Q; Q.push(s);
    while ( !Q.empty() ) {
        ll v = Q.front(); Q.pop();
        EACH(e, G[v]) {
            if (e.cap > 0 && res[e.to] == linf) {
                res[e.to] = res[v]+1;
                Q.push(e.to);
            }
        }
    }
    return res;
}
ll max_flow(ll s, ll t) {
    ll res = 0;
    while (1) {
        vector<ll> dist = bfs(s);
        if (dist[t] == linf) break;
        while (1) {
            ll f = dfs(s, t, linf, dist);
            if (f == 0) break;
            res += f;
        }
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m; cin >> n >> m;
    int v1 = m / n;
    int v2 = v1 + (m % n == 0 ? 0 : 1);
    cout << v2-v1 << endl;
    vector< vector<ll> > H(n, vector<ll>(m)); cin >> H;
    ll ss = n + m, s = ss+1, t = s+1;
    G.resize(t+1);
    REP(i, m) {
        add_edge(n+i, t, 1);
    }
    REP(i, n) {
        add_edge(s, i, v1);
        add_edge(ss, i, 1);
    }
    add_edge(s, ss, m-n*v1);
    map<ll, vector<P>> ev;
    REP(i, n) REP(j, m) {
        ev[H[i][j]].pb({i, j});
    }
    ll f = 0;
    ll ans = linf;
    EACH(dt, ev) {
        EACH(p, dt.second) {
            assert(dt.first == H[p.first][p.second]);
            add_edge(p.first, n+p.second, 1);
        }
        f += max_flow(s, t);
        if (f == m) {
            ans = dt.first;
            break;
        }
    }
    cout << ans << endl;
}