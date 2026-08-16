#include <bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define pb push_back
#define reset(a,b) memset(a,b,sizeof a);
#define ALL(x) x.begin(),x.end()
 
template <typename T>
void cetak(T t){cout << t << ')' << endl;}
template <typename T, typename... V>
void cetak(T t, V... v) {cout << t; if (sizeof...(v)) cerr << ", "; cetak(v...);}
 
#define debug(x...) cout<< '(' << #x << ") = ("; cetak(x) 
#define sz(x) (int)(x.size())
#define lt(x) (int)(x.length())

const int MOD = 1e9 + 7;
const int mx = 1e5 + 10;

int n, m, u, v;
int sudah[mx], disc[mx], idx, low[mx];
set<pair<int, int>> bridge;
set<int> g[mx];
vector<int> G[mx];
set<pair<int, int>> tipe;
void dfs(int now, int par){
    sudah[now] = 1;
    low[now] = disc[now] = ++idx;
    for(int i : g[now]){
        if(!sudah[i]){
            dfs(i, now);
            low[now] = min(low[now], low[i]);
            if(low[i] > disc[now]){
                bridge.insert({i, now});
            }
            tipe.insert({now, i});
            // debug(now, i);
        }
        else if(par != i && disc[i] < disc[now]){
            low[now] = min(low[now], disc[i]);
            tipe.insert({now, i});
            // debug(now, i);
        }
    }
}

int di[mx];

void cari_komponen(int now){
    di[now] = idx;
    for(int i : g[now]){
        if(bridge.count({now, i}) || bridge.count({i, now})) continue;
        if(di[i]) continue;
        cari_komponen(i);
    }
}

int P[mx][22];
int level[mx];
void DFS(int now, int par, int lev = 0){
    level[now] = lev;
    P[now][0] = par;
    for(int i = 1; i <= 20; i++) P[now][i] = P[P[now][i - 1]][i - 1];
    for(int i : G[now]){
        if(i != par)
            DFS(i, now, lev + 1);
    }
}

int findLCA(int p, int q){
    if(level[p] > level[q]) swap(p, q);
    for(int i = 20; i >= 0; i--){
        if(level[q] - level[p] >= (1 << i)){
            q = P[q][i];
        }
    }
    if(q == p) return p;
    for(int i = 20; i >= 0; i--){
        if(P[q][i] != P[p][i]){
            p = P[p][i];
            q = P[q][i];
        }
    }
    return P[p][0];
}

int pref1[mx], pref2[mx];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    for(int i = 1; i <= m; i++){
        cin >> u >> v;
        g[u].insert(v);
        g[v].insert(u);
    }
    dfs(1, 0);
    idx = 0;
    for(int i = 1; i <= n; i++){
        if(!di[i]){
            ++idx;
            cari_komponen(i);
        }
    }
    for(auto i : bridge){
        G[di[i.f]].pb(di[i.s]);
        G[di[i.s]].pb(di[i.f]);
    }
    DFS(1, 0);
    int k;
    cin >> k;
    for(int i = 1; i <= k; i++){
        cin >> u >> v;
        u = di[u];
        v = di[v];
        if(u == v) continue;
        int par = findLCA(u, v);
        // debug(u, v, par);
        pref1[u] += 1;
        pref2[v] += 1;
        pref1[par] -= 1;
        pref2[par] -= 1;
    }
    vector<int> ve(idx);
    iota(ALL(ve), 1);
    sort(ALL(ve), [&](int x, int y){
        return level[x] > level[y];
    });
    for(int i : ve){
        for(int j : G[i]){
            if(P[i][0] == j) continue;
            pref1[i] += pref1[j];
            pref2[i] += pref2[j];
        }
        // debug(i, pref1[i], pref2[i]);
        if(pref1[i] > 0 && pref2[i] > 0){
            cout << "No\n";
            return 0;
        }
    }
    cout << "Yes\n";
    for(int i = 1; i <= n; i++){
        for(int j : g[i]){
            if(bridge.count({i, j}) || bridge.count({j, i})) continue;
            if(tipe.count({i, j})){
                cout << i << ' ' << j << '\n';
            }
        }
    }
    for(auto i : bridge){
        if(di[i.f] == P[di[i.s]][0]){
            if(pref1[di[i.s]] == 0){
                cout << i.f << ' ' << i.s << '\n';
            }
            else{
                cout << i.s << ' ' << i.f << '\n';
            }
        }
        else{
            if(pref1[di[i.f]] == 0){
                cout << i.s << ' ' << i.f << '\n';
            }
            else{
                cout << i.f << ' ' << i.s << '\n';
            }
        }
    }
}
