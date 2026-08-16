#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <algorithm>
#include <stack>
#include <map>
#include <set>
#include <climits>
#include <queue>
#include <bitset>
#include <cassert>
#include <math.h>
#include <complex>
#include <iomanip>
#include <unordered_map>
using namespace std;
#define ll long long
#define pb(x) push_back(x)
#ifdef _OLIMPOLOCAL
    #define debug(...) cerr << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
    #define debug(...) 1337
#endif
void debug_out() { cout << "\n";}
template<typename T1, typename... T2> void debug_out(T1 A, T2... B) { cout << " " << A; debug_out(B...); }
int test = 1;
#define out(x) {cout << x << "\n";return;}
#define all(N) N.begin(),N.end()
#define allr(N) N.rbegin(),N.rend()
template<typename T1> 
void pr(vector<T1> V, int add = 0, int start = -1, int end = -1) {
    if (start < 0) start = 0;
    if (end < 0) end = V.size() - 1;
    for (int i = start; i <= end; i++) {
        cout << V[i] + add << ((i == end) ? "\n" : " ");
    }
}
template<typename T1> 
T1 chmin(T1 &x, const T1 v) { return x = min(x,v); }
template<typename T1> 
T1 chmax(T1 &x, const T1 v) { return x = max(x,v); }

#define rep(i, n) for (int i = 0; i < n; i++)
#define reps(i, s, n) for (int i = s; i < n; i++)
#define repr(i, n) for (int i = n-1; i >= 0; i--)
#define repsr(i, s, n) for (int i = n-1; i >= s; i--)
#define PI pair<int,int>
template<typename T1> 
T1 gcd(const T1 &a, const T1 &b) {
    if (a == 0 || b == 0) return a + b;
    return gcd(b, a %b);
}
//-------------------------- ^ DONT TOUCH ^-----------------------------------------------------------------
#define MAX 100001 
#define MOD 1000000007ll
ll f[MAX];
ll n, s;

long long power(long long x, long long n) {
    long long p = x;
    long long s = 1;
    while (n > 0) {
        if (n & 1) s = (s * p) % MOD;
        p = (p * p) % MOD;
        n /= 2;
    }
    return s;
}

ll val(vector<ll> V) {
    sort(all(V));
    ll a = f[V.size()];
    for(int i = 0 ; i < V.size(); i++) {
        int c = 1;
        while(i + 1 < V.size() && V[i+1] == V[i]) {
            c++;
            i++;
        }
        if (c > 1) a *= power(f[c], MOD-2);
        a %= MOD;
    }
    return a;
}

void solve() {
    cin >> n;
    vector<ll> N(n);
    s = 0;
    rep(i,n) {
        cin >> N[i];
        s += N[i];
    }
    if (s % n != 0) out(0);
    s/=n;
    vector<ll> L, H;
    int c = 0;
    ll a = 1;
    rep(i,n) {
        N[i] -= s;
        if (N[i] > 0) {
            H.push_back(N[i]);
        }
        if (N[i] < 0) {
            L.push_back(-N[i]);
        }
        if (N[i] == 0) {
            a *= n;
            a %= MOD;
            c++;
        }
    }
    a = f[n];
    a *= power(f[c], MOD-2);
    a %= MOD;
    a *= power(f[n-c], MOD-2);
    a %= MOD;
    n-=c;


    ll l = val(L);
    ll h = val(H);
    int sl = L.size();
    int sh = H.size();
    ll s = 0;
    ll r = (l * h) % MOD;
    if(sl + sh == 0)out(a);
    if (sl == 1 || sh == 1) {
        out(val(N));   
    }
    s = (2*r) % MOD;
    s = ((s % MOD) + MOD) % MOD;
    debug(l,h);
    out((a * s) % MOD);
}
int main() {
    f[0] = 1;
    reps(i,1,MAX) f[i] = (f[i-1] * (ll)i) % MOD;
    ios_base::sync_with_stdio(0);cin.tie(0);
    //cin >> test;
   
    rep(testCase, test) {
        #ifdef _OLIMPOLOCAL
        cout << "Case #" << testCase + 1 << "\n";
        #endif
        solve();
    }
    return 0;
}