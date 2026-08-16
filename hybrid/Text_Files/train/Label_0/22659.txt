#include <bits/stdc++.h>
#define ll long long
#define INF (1LL << 60)
#define MOD 1000000007
#define EPS 1e-10
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;--i)
#define srep(i,s,t) for(int i=(int)(s);i<(int)(t);++i)
#define each(a,b) for(auto& (a): (b))
#define all(v) (v).begin(),(v).end()
#define len(v) (int)(v).size()
#define zip(v) sort(all(v)),v.erase(unique(all(v)),v.end())
#define cmx(x,y) x=max(x,y)
#define cmn(x,y) x=min(x,y)
#define fi first
#define se second
#define pb push_back
#define show(x) cout<<#x<<" = "<<(x)<<endl
#define spair(p) cout<<#p<<": "<<p.fi<<" "<<p.se<<endl
#define sar(a,n) cout<<#a<<":";rep(pachico,n)cout<<" "<<a[pachico];cout<<endl
#define svec(v) cout<<#v<<":";rep(pachico,v.size())cout<<" "<<v[pachico];cout<<endl
#define svecp(v) cout<<#v<<":";each(pachico,v)cout<<" {"<<pachico.first<<":"<<pachico.second<<"}";cout<<endl
#define sset(s) cout<<#s<<":";each(pachico,s)cout<<" "<<pachico;cout<<endl
#define smap(m) cout<<#m<<":";each(pachico,m)cout<<" {"<<pachico.first<<":"<<pachico.second<<"}";cout<<endl

using namespace std;

typedef pair<int,int> P;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<P> vp;
typedef vector<string> vs;

const int MAX_N = 2005;

int dp[MAX_N][MAX_N];
ll cnt[MAX_N][MAX_N];

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    string s;
    cin >> s;
    int n = len(s);
    rep(i,n+1){
        rep(j,n+1){
            dp[i][j] = MOD;
        }
    }
    rep(i,n+1){
        dp[i][i] = dp[i][i+1] = 0;
        cnt[i][i] = cnt[i][i+1] = 1;
    }
    ll K;
    cin >> K;
    for(int i=2;i<=(int)n;i++){
        rep(j,n-i+1){
            int k = i+j;
            if(s[j] == s[k-1]){
                dp[j][k] = dp[j+1][k-1];
                cnt[j][k] = cnt[j+1][k-1];
            }else{
                if(dp[j][k-1] < dp[j+1][k]){
                    cnt[j][k] = cnt[j][k-1];
                }else if(dp[j][k-1] > dp[j+1][k]){
                    cnt[j][k] = cnt[j+1][k];
                }else{
                    if((double)(cnt[j][k-1]+cnt[j+1][k]) > INF){
                        cnt[j][k] = INF;
                    }else{
                        cnt[j][k] = cnt[j][k-1]+cnt[j+1][k];
                    }
                }
                dp[j][k] = min(dp[j][k-1],dp[j+1][k])+1;
            }
        }
    }
    if(K > cnt[0][n]){
        cout << "NONE\n";
        return 0;
    }
    int ni = 0, nj = n;
    string res;
    while(nj-ni > 1){
        if(s[ni] == s[nj-1]){
            res.pb(s[ni]);
            ni++, nj--;
            continue;
        }
        if(dp[ni+1][nj] < dp[ni][nj-1]){
            res.pb(s[ni]);
            ni++;
        }else if(dp[ni+1][nj] > dp[ni][nj-1]){
            res.pb(s[nj-1]);
            nj--;
        }else{
            if(s[ni] < s[nj-1]){
                if(cnt[ni+1][nj] >= K){
                    res.pb(s[ni]);
                    ni++;
                }else{
                    K -= cnt[ni+1][nj];
                    res.pb(s[nj-1]);
                    nj--;
                }
            }else{
                if(cnt[ni][nj-1] >= K){
                    res.pb(s[nj-1]);
                    nj--;
                }else{
                    K -= cnt[ni][nj-1];
                    res.pb(s[ni]);
                    ni++;
                }
            }
        }
    }
    if(nj - ni){
        string tmp = res;
        res.pb(s[ni]);
        reverse(all(tmp));
        res += tmp;
    }else{
        string tmp = res;
        reverse(all(tmp));
        res += tmp;
    }
    cout << res << "\n";
    return 0;
}

