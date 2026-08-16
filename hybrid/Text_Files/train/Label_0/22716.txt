#include <cstring>
#include <cassert>
#include <utility>
#include <iostream>
#include <cstdio>
#include <iomanip>
#include <bitset>
#include <chrono>
#include <cstdlib>
#include <functional>
#include <tuple>
#include <climits>
#include <limits>
#include <deque>
#include <list>
#include <array>
#include <stack>
#include <queue>
#include <random>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
 
#define init ios::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
#define setpr(x) cout << setprecision((x))
#define PI atan(1)*4
#define fi first
#define se second
#define pb push_back
#define eb emplace_back
#define lb lower_bound
#define ub upper_bound
#define mk(a , b) { min((a) , (b)) , max((a) , (b)) }
#define flush cout.flush()
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define endc "\n"
#define meme(x) memset((x), 0, sizeof((x)))
#define memo(x) memset((x),-1, sizeof((x)))
 
using namespace std;

void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pld;

// #define int ll
#define MOD 998244353

ll egcd(ll a, ll b, ll &x, ll &y){
    if (a == 0LL){  
        x = 0LL;  
        y = 1LL;  
        return b;  
    }
    ll xx, yy;
    ll val = egcd(b % a, a, xx, yy);  
    x = yy - (b / a) * xx;  
    y = xx;  
    return val;
}

ll gcd(ll a, ll b){
    while(true){
        if(a>b)
            swap(a,b);
        if (a == 0) 
            return b; 
        ll p = b % a, q = a;
        a = p;
        b = q;
    }
}
 
ll powerMod(ll x,ll y){
    ll res = 1LL;
    x %= MOD;
    while(y > 0){
        if(y & 1)res = (res * x) % MOD;
        y = y >> 1;
        x = (x * x) % MOD;
    }
    return res % MOD;
}

//  ==========      //\\       //||     ||====//||
//      ||         //  \\        ||     ||   // ||
//      ||        //====\\       ||     ||  //  ||
//      ||       //      \\      ||     || //   ||
//  ==========  //        \\  ========  ||//====|| 
//  code

void solve() {
    int n,i,j,k,l,p;
    cin >> n;
    vector<pii> a(n);
    for(auto &i : a) cin >> i.fi;
    for(auto &i : a) cin >> i.se;

    sort(all(a));
    if(a[0].fi == 1) {
        a.erase(a.begin());
        n--;
    }

    if(n == 0) {
        cout << 0 << endc;
        return;
    }

    debug(a);

    int ans = 0;

    int lr, lc;
    lr = lc = 1;
    for(auto i : a) {
        if(i.fi == i.se) {
            ans += i.se - lr;
        } else {
            if(lr == 1) {
                lr = 2;
                if(lr == i.fi) continue;
            }
            if(lc == i.se) {
                if((lc + lr) % 2) {
                    p = i.fi - lr;
                    ans += (p + 1) / 2;
                } else {
                    p = i.fi - lr;
                    ans += p / 2;
                }
            } else {
                // lc < i.se
                if((lc + lr) % 2) {
                    lr = lr + i.se - lc;
                    lc = i.se;
                    p = i.fi - lr;
                    ans += (p + 1) / 2;
                } else {
                    if(i.fi - lr == i.se - lc) 
                        ans += i.se - lc;
                    else {
                        lr++;
                        lr = lr + i.se - lc;
                        lc = i.se;
                        p = i.fi - lr;
                        ans += (p + 1) / 2;
                    }
                }
            }
        }
        lr = i.fi;
        lc = i.se;
        debug(ans);
    }

    cout << ans << endc;
}

int32_t main(){
    init;
    int t = 1;
    cin >> t;
    for(int tt = 1; tt <= t; tt++) solve();
    return 0;
}