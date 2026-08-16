#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef double db; 
typedef string str; 

typedef pair<int,int> pi;
typedef pair<ll,ll> pl; 
typedef pair<db,db> pd; 

typedef vector<int> vi; 
typedef vector<ll> vl; 
typedef vector<db> vd; 
typedef vector<str> vs; 
typedef vector<pi> vpi;
typedef vector<pl> vpl; 
typedef vector<pd> vpd; 

#define mp make_pair
#define f first
#define s second
#define sz(x) (int)x.size()
#define all(x) begin(x), end(x)
#define rall(x) (x).rbegin(), (x).rend() 
#define rsz resize
#define ins insert 
#define ft front() 
#define bk back()
#define pf push_front 
#define pb push_back
#define eb emplace_back 
#define lb lower_bound 
#define ub upper_bound 

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i,a) ROF(i,0,a)
#define trav(a,x) for (auto& a: x)

const int MOD = 1e9+7; // 998244353;
const int MX = 2e5+5; 
const ll INF = 1e18; 
const ld PI = acos((ld)-1);
const int xd[4] = {1,0,-1,0}, yd[4] = {0,1,0,-1}; 

template<class T> bool ckmin(T& a, const T& b) { 
	return b < a ? a = b, 1 : 0; }
template<class T> bool ckmax(T& a, const T& b) { 
	return a < b ? a = b, 1 : 0; } 
int pct(int x) { return __builtin_popcount(x); } 
int bit(int x) { return 31-__builtin_clz(x); } // floor(log2(x)) 
int cdiv(int a, int b) { return a/b+!(a<0||a%b == 0); } // division of a by b rounded up, assumes b > 0 

// INPUT
template<class A> void re(complex<A>& c);
template<class A, class B> void re(pair<A,B>& p);
template<class A> void re(vector<A>& v);
template<class A, size_t SZ> void re(array<A,SZ>& a);

template<class T> void re(T& x) { cin >> x; }
void re(db& d) { str t; re(t); d = stod(t); }
void re(ld& d) { str t; re(t); d = stold(t); }
template<class H, class... T> void re(H& h, T&... t) { re(h); re(t...); }

template<class A> void re(complex<A>& c) { A a,b; re(a,b); c = {a,b}; }
template<class A, class B> void re(pair<A,B>& p) { re(p.f,p.s); }
template<class A> void re(vector<A>& x) { trav(a,x) re(a); }
template<class A, size_t SZ> void re(array<A,SZ>& x) { trav(a,x) re(a); }

// TO_STRING
#define ts to_string
template<class A, class B> str ts(pair<A,B> p);
template<class A> str ts(complex<A> c) { return ts(mp(c.real(),c.imag())); }
str ts(bool b) { return b ? "true" : "false"; }
str ts(char c) { str s = ""; s += c; return s; }
str ts(str s) { return s; }
str ts(const char* s) { return (str)s; }
str ts(vector<bool> v) { 
	bool fst = 1; str res = "{";
	F0R(i,sz(v)) {
		if (!fst) res += ", ";
		fst = 0; res += ts(v[i]);
	}
	res += "}"; return res;
}
template<size_t SZ> str ts(bitset<SZ> b) {
	str res = ""; F0R(i,SZ) res += char('0'+b[i]);
	return res; }
template<class T> str ts(T v) {
	bool fst = 1; str res = "{";
	for (const auto& x: v) {
		if (!fst) res += ", ";
		fst = 0; res += ts(x);
	}
	res += "}"; return res;
}
template<class A, class B> str ts(pair<A,B> p) {
	return "("+ts(p.f)+", "+ts(p.s)+")"; }

// OUTPUT
template<class A> void pr(A x) { cout << ts(x); }
template<class H, class... T> void pr(const H& h, const T&... t) { 
	pr(h); pr(t...); }
void ps() { pr("\n"); } // print w/ spaces
template<class H, class... T> void ps(const H& h, const T&... t) { 
	pr(h); if (sizeof...(t)) pr(" "); ps(t...); }

// DEBUG
void DBG() { cerr << "]" << endl; }
template<class H, class... T> void DBG(H h, T... t) {
	cerr << to_string(h); if (sizeof...(t)) cerr << ", ";
	DBG(t...); }
#ifdef LOCAL // compile with -DLOCAL
#define dbg(...) cerr << "[" << #__VA_ARGS__ << "]: [", DBG(__VA_ARGS__)
#else
#define dbg(...) 42
#endif

// FILE I/O
void setIn(string s) { freopen(s.c_str(),"r",stdin); }
void setOut(string s) { freopen(s.c_str(),"w",stdout); }
void unsyncIO() { ios_base::sync_with_stdio(0); cin.tie(0); }
void setIO(string s = "") {
	unsyncIO();
	// cin.exceptions(cin.failbit); 
	// throws exception when do smth illegal
	// ex. try to read letter into int
	if (sz(s)) { setIn(s+".in"), setOut(s+".out"); } // for USACO
}

mt19937 rng((uint32_t)chrono::steady_clock::now().time_since_epoch().count()); 

const ll pri = (ll)1e10+19;

int R,B,K;

__int128 atMost(ll a, ll b, ll mid) {
	__int128 ans = 0;
	F0R(x,2000) {
		ll dif = mid-a*x; if (dif < 0) break;
		ll hi = dif/b;
		ans += hi+1;
	}
	F0R(y,2000) {
		ll dif = mid-b*y; if (dif < 0) break;
		ll hi = dif/a; if (hi < 2000) break;
		ans += hi+1-2000;
	}
	return ans;
}

ll ari(ll lo, ll hi) {
	return (hi+lo)*(hi-lo+1)/2;
}

pl getMost(ll a, ll b, ll mid) {
	pl ans = {0,0}; ll num = 0;
	vpl extra;
	F0R(x,2000) {
		ll dif = mid-a*x; if (dif < 0) break;
		ll hi = dif/b;
		num += hi+1;
		ans.f += (hi+1)*x; ans.s += ari(0,hi);
		dbg("??",x,hi,ans);
		if ((mid+1-a*x)%b == 0)
			extra.pb({x,(mid+1-a*x)/b});
	}
	F0R(y,2000) {
		ll dif = mid-b*y; if (dif < 0) break;
		ll hi = dif/a; if (hi < 2000) break;
		num += hi+1-2000;
		ans.f += ari(2000,hi); ans.s += (hi+1-2000)*y;
		if ((mid+1-b*y)%a == 0)
			extra.pb({(mid+1-b*y)/a,y});
	}
	sort(all(extra)); extra.erase(unique(all(extra)),end(extra));
	assert(num <= K && num+sz(extra) >= K);
	F0R(i,K-num) {
		ans.f += extra[i].f;
		ans.s += extra[i].s;
	}
	// dbg("HUH",num,K,sz(extra),ans);
	return ans;
}

pl getK(ll a) {
	ll b = pri-a;
	ll lo = 0, hi = 1e18;
	while (lo < hi) {
		ll mid = (lo+hi+1)/2;
		__int128 z = atMost(a,b,mid); 
		if (z <= K) lo = mid;
		else hi = mid-1;
	}
	// dbg(a,K,atMost(a,b,lo),atMost(a,b,lo+1)); // exit(0);
	return getMost(a,b,lo);
}

bool ok() {
	__int128 lo = 1, hi = pri-1;
	while (lo <= hi) {
		__int128 mid = (lo+hi)/2;
		pl p = getK(mid);
		if (p.f*mid+p.s*(pri-mid) > R*mid+(ld)B*(pri-mid)) return 0;
		if (R >= p.f && B >= p.s) return 1;
		if (R > p.f) hi = mid-1;
		else lo = mid+1;
	}
	return 1;
}

int solve() {
	int lo = 1, hi = 4000000;
	while (lo < hi) {
		K = (lo+hi+1)/2;
		if (ok()) lo = K;
		else hi = K-1;
	}
	return lo;
}

int main() {
	dbg(pri);
	setIO(); re(R,B);
	//K = 7;
	//dbg("OK",ok()); exit(0);
	ps(solve()-1);
	// you should actually read the stuff at the bottom
}

/* stuff you should look for
	* int overflow, array bounds
	* special cases (n=1?)
	* do smth instead of nothing and stay organized
	* WRITE STUFF DOWN
*/

