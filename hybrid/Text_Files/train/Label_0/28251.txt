/*
#pragma GCC optimize("O2")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2,sse,sse2,fma")
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int , int> pii;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int maxn = 2e5 + 100;
const ll mod = 1e9+7;
const ld PI = acos((ld)-1);

#define pb push_back
#define endl '\n'
#define dokme(x) cout << x , exit(0)
#define migmig ios::sync_with_stdio(false),cin.tie(0),cout.tie(0)
#define ms(x , y) memset(x , y , sizeof x)
ll pw(ll a, ll b, ll md = mod){ll res = 1;while(b){if(b&1){res=(a*res)%md;}a=(a*a)%md;b>>=1;}return(res);}

int n;
vector < pii > adj[maxn];
int sz[maxn];
bool hide[maxn];
bool fib[maxn];
int bg[maxn];
int par[maxn];
int big , target , tar;

void plant(int v){
	sz[v] = 1;
	for(auto [u , i] : adj[v]){
		if(!hide[i] and u ^ par[v])
			par[u] = v , plant(u) , sz[v] += sz[u];
	}
	if(sz[v] == target or sz[v] == tar)big = v;
}

int fnd(int v , int p){
	return(lower_bound(adj[v].begin() , adj[v].end() , pii(p , 0))->second);
}

void solve(int v, int n){
	if(!fib[n])dokme("NO");
	if(n <= 3)return;
	par[v] = 0;
	target = bg[n];
	tar = n - bg[n];
	big = 0;
	plant(v);
	v = big;
	if(!v)dokme("NO");
	hide[fnd(v , par[v])] = 1;
	int siz = sz[v];
	solve(par[v] , n-sz[v]);
	solve(v , siz);
}

int32_t main(){
	migmig;
	int a = 1 , b = 1;
	while(b < maxn){
		fib[a] = fib[b] = 1;
		b = a + b;
		a = b - a;
		if(b < maxn)bg[b] = a;
	}
	cin >> n;
	for(int i = 1 ; i < n ; i ++){
		int u , v;
		cin >> u >> v;
		adj[u].pb({v , i});
		adj[v].pb({u , i});
	}
	for(int i = 1 ; i <= n ; i ++)
		sort(adj[i].begin() , adj[i].end());
	solve(1 , n);
	cout << "YES";
	return(0);
}
