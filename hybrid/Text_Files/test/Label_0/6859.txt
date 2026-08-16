#include <bits/stdc++.h>
using namespace std;
#define REP(i,x,y) for(int i=(x);i<(y);++i)
#define MP(a,b) make_pair((a),(b))
#define debug(x) #x << "=" << (x)
 
#ifdef DEBUG
#define _GLIBCXX_DEBUG
#define dump(x) std::cerr << debug(x) << " (L:" << __LINE__ << ")" << std::endl
#else
#define dump(x)
#endif

typedef long long int ll;
typedef pair<int,int> pii;
//template<typename T> using vec=std::vector<T>;

const int INF=1<<30;
const long long int INF_=1LL<<58;
const double EPS=1e-9;
const int dx[]={1,0,-1,0},dy[]={0,1,0,-1};

template <typename T> ostream &operator<<(ostream &os, const vector<T> &vec){
	os << "[";
	for (const auto &v : vec) {
		os << v << ",";
	}
	os << "]";
	return os;
}

ll Extgcd(ll a,ll b,ll &x,ll &y){
	ll d=a;
	if(b!=0){
		d=Extgcd(b,a%b,y,x);
		y-=(a/b)*x;
	} else {
		x=1; y=0;
	}
	return d;
}

ll ModInverse(ll a,ll m){
	ll x,y;
	if(Extgcd(a,m,x,y)==1) return (x+m)%m;
	return 0;
}

ll fact[220001];

void InitFact(ll n,ll m){
	fact[1]=1;
	for(ll i=2; i<=n; ++i) fact[i]=(i*fact[i-1])%m;
}

ll ModFact(ll n,ll p,ll &e){
	e=0;
	if(n==0) return 1;

	ll res=ModFact(n/p,p,e);
	e+=n/p;

	if(n/p%2!=0) return res*(p-fact[n%p])%p;
	return res*fact[n%p]%p;
}

ll ModComb(ll n,ll k,ll p){
	if(n<0||k<0||n<k) return 0;
	ll e1,e2,e3;
	ll a1=ModFact(n,p,e1),a2=ModFact(k,p,e2),a3=ModFact(n-k,p,e3);
	if(e1>e2+e3) return 0;
	return a1*ModInverse(a2*a3%p,p)%p;
}

void Solve(){
	const ll mod=1000000007;
	InitFact(220000,mod);
	ll n,m,k;
	cin >> n >> m >> k;

	ll res=0;
	REP(i,0,k+1){
		ll a=(ModComb(n+2*i,i,mod)-ModComb(n+2*i,i-1,mod)+mod)%mod;
		ll b=(ModComb(m+2*(k-i),k-i,mod)-ModComb(m+2*(k-i),(k-i)-1,mod)+mod)%mod;
		ll c=ModComb(n+m+2*k,n+2*i,mod);
		res+=a*b%mod*c%mod;
		res%=mod;
	}

	cout << res << endl;
}

int main(){
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);
	Solve();
	return 0;
}