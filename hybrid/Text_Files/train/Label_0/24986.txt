#include <bits/stdc++.h>
using namespace std;
#define ll		long long
#define ln 		"\n"
#define pb 		push_back
#define pll 	pair<ll,ll>
#define ppll 	pair<ll , pll>
#define vll 	vector<ll>
#define vs 		vector<string>
#define vpll 	vector<pll>
#define vvll 	vector<vector<ll>>
#define vvpll 	vector<vpll>
#define f 		first
#define s 		second
#define bs 		binary_search
#define lb 		lower_bound
#define ub 		upper_bound
#define Test 	ll T;cin>>T; for(ll tc = 1 ; tc <= T ; tc++)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define all(x) 	x.begin(),x.end()
#define allr(x) x.rbegin(),x.rend()
#define pi 		3.14159265358979323846
#define MAXX 	LLONG_MAX
const int MOD = 1e9 + 7 , MAX = INT_MAX , MAXN = 2e6 + 5;

template <typename T> istream& operator >> (istream &in , vector<T> &v) { for(auto &i: v) cin>>i; return in; }
template <typename T> istream& operator >> (istream &in , pair<T , T> &p) { cin>>p.f>>p.s; return in; }
template <typename T> ostream& operator << (ostream &out , vector<T> &v) { for(auto &i: v) cout<<i<<" "; return out; }
template <typename T> ostream& operator << (ostream &out , pair<T , T> &p) { cout<<p.f<<" "<<p.s<<" "; return out; }

vll prime(MAXN);
void primes() {
	for(ll i = 1 ; i < MAXN ; i++) prime[i] = i;
    for(ll i = 2 ; i <= sqrt(MAXN) ; i++) {
    	if(prime[i] == i) {
    		for(ll j = i * i ; j < MAXN ; j += i) {
    			if(prime[j] == j) prime[j] = i;
    		}
    	}
    }
}
void solve() {
    ll n , ans0 = 0 , ans1 = 0 , q , w;
    cin>>n;
    vll a(n);
    map <ll , ll> mp;
    for(auto &k: a) {
    	cin>>k;
    	map <ll , ll> factors;
    	while(k > 1) {
    		ll f = prime[k];
    		factors[f]++;
    		k /= f;
    	}
    	ll p = 1;
    	for(auto f : factors) if(f.s % 2) p *= f.f;
    	mp[p]++;
    }
    for(auto k: mp) {
    	ans0 = max(ans0 , k.s);
    	if((k.s % 2 == 0) or (k.f == 1)) ans1 += k.s; 
    }
    ans1 = max(ans1 , ans0);
	cin>>q;
	while(q--) {
		cin>>w;
		if(w == 0) cout<<ans0<<ln;
		else cout<<ans1<<ln;
	}
}
int main() {
    fast_io;
    #ifndef ONLINE_JUDGE
        freopen("input.txt" , "r" , stdin);
        freopen("output.txt" , "w" , stdout);
    #endif

    primes();
    Test
    solve();

    return 0;
}