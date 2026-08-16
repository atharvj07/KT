#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < n; i++)
#define rep2(i, x, n) for(int i = x; i <= n; i++)
#define rep3(i, x, n) for(int i = x; i >= n; i--)
#define elif else if
#define sp(x) fixed << setprecision(x)
#define pb push_back
#define eb emplace_back
#define all(x) x.begin(), x.end()
#define sz(x) (int)x.size()
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using pil = pair<int, ll>;
using pli = pair<ll, int>;
using pll = pair<ll, ll>;
const ll MOD = 1e9+7;
//const ll MOD = 998244353;
const int inf = (1<<30)-1;
const ll INF = (1LL<<60)-1;
const ld EPS = 1e-10;
template<typename T> bool chmax(T &x, const T &y) {return (x < y)? (x = y, true) : false;};
template<typename T> bool chmin(T &x, const T &y) {return (x > y)? (x = y, true) : false;};

using ull = unsigned long long;

int main(){
    int N;
    cin >> N;
    int s[N], t[N];
    ull U[N], V[N];
    int u[64][N], v[64][N];
    rep(i, N) cin >> s[i];
    rep(i, N) cin >> t[i];
    rep(i, N) cin >> U[i];
    rep(i, N) cin >> V[i];
    rep(i, N){
        rep(j, 64){
            u[j][i] = (U[i]>>j)&1;
            v[j][i] = (V[i]>>j)&1;
        }
    }
    int ans[64][N][N];
    rep(i, 64) rep(j, N) rep(k, N) ans[i][j][k] = -1;
    rep(i, 64){
        vector<int> remr, remc;
        bool row[2], col[2];
        rep(j, 2) row[j] = col[j] = false;
        rep(j, N){
            if(!s[j] && u[i][j]) rep(k, N) ans[i][j][k] = 1, row[1] = true;
            elif(s[j] && !u[i][j]) rep(k, N) ans[i][j][k] = 0, row[0] = true;
            else remr.pb(j);
        }
        rep(k, N){
            if(!t[k] && v[i][k]) rep(j, N) ans[i][j][k] = 1, col[1] = true;
            elif(t[k] && !v[i][k]) rep(j, N) ans[i][j][k] = 0, col[0] = true;
            else remc.pb(k);
        }
        int n = sz(remr), m = sz(remc);
        if(n*m == 0) continue;
        elif(n == 1){
            vector<int> tmp;
            for(auto &e: remc){
                if(!t[e] && !row[0]) ans[i][remr[0]][e] = 0;
                elif(t[e] && !row[1]) ans[i][remr[0]][e] = 1;
                else tmp.pb(e);
            }
            rep(j, sz(tmp)){
                ans[i][remr[0]][tmp[j]] = (j^s[remr[0]])&1;
            }
        }
        elif(m == 1){
            vector<int> tmp;
            for(auto &e: remr){
                if(!s[e] && !col[0]) ans[i][e][remc[0]] = 0;
                elif(s[e] && !col[1]) ans[i][e][remc[0]] = 1;
                else tmp.pb(e);
            }
            rep(j, sz(tmp)){
                ans[i][tmp[j]][remc[0]] = (j^t[remc[0]])&1;
            }
        }
        else{
            rep(j, n){
                rep(k, m){
                    ans[i][remr[j]][remc[k]] = (j^k)&1;
                }
            }
        }
    }
    ull all[N][N];
    rep(i, N) rep(j, N) all[i][j] = 0;
    rep(i, 64){
        rep(j, N){
            rep(k, N){
                all[j][k] |= (ull)ans[i][j][k] << i;
            }
        }
    }
    bool same = true;
    rep(i, N){
        ull res = all[i][0];
        if(!s[i]) rep(j, N) res &= all[i][j];
        else rep(j, N) res |= all[i][j];
        if(res != U[i]) same = false;
    }
    rep(j, N){
        ull res = all[0][j];
        if(!t[j]) rep(i, N) res &= all[i][j];
        else rep(i, N) res |= all[i][j];
        if(res != V[j]) same = false;
    }
    if(!same) cout << -1 << endl;
    else{
        rep(i, N){
            rep(j, N) cout << all[i][j] << ' ';
            cout << endl;
        }
    }
}