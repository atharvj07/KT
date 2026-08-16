#include <bits/stdc++.h>
using namespace std;

using ll=long long;
#define rng(i,l,r) for(int i=int(l);i<int(r);i++)
#define rep(i,r) rng(i,0,r)
#define rrng(i,l,r) for(int i=int(r)-1;i>=int(l);i--)
#define rrep(i,r) rrng(i,0,r)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define F first
#define S second
#define bg begin()
#define ed end()
#define all(x) x.bg,x.ed
#define si(x) int(x.size())
#define inf INT_MAX/2-100
#define infl LLONG_MAX/3
#ifdef LOCAL
#define dmp(x) cerr<<__LINE__<<' '<<#x<<' '<<x<<endl
#else
#define dmp(x) void(0)
#endif

template<class t,class u>bool chmax(t&a,u b){if(a<b)a=b;return a<b;}
template<class t,class u>bool chmin(t&a,u b){if(b<a)a=b;return b<a;}

template<class t>using vc=vector<t>;
template<class t>using vvc=vector<vector<t>>;

using pi=pair<int,int>;
using pl=pair<ll,ll>;
using vi=vc<int>;
using vl=vc<ll>;


ll readl(void){
	ll x;
	cin>>x;
	return x;
}
int readi(void){
	int x;
	cin>>x;
	return x;
}

string readstr(){
	string s;
	cin>>s;
	return s;
}
vi readvi(int n,int off=0){
	vi v(n);
	rep(i,n)v[i]=readi(),v[i]+=off;
	return v;
}

vl readvl(int n,int off=0){
	vl v(n);
	rep(i,n)v[i]=readl(),v[i]+=off;
	return v;
}

template<class t>
void print(t x,int suc=1){
	cout<<x;
	if(suc==1)cout<<"\n";
	if(suc==2)cout<<" ";
}

template<class t>
void print(const vc<t>&v,int suc=1){
	rep(i,si(v))print(v[i],i==int(si(v))-1?1:suc);
}

template<class t>
bool inc(t a,t b,t c){
	return !(c<b||b<a);
}

template<class t>
void compress(vc<t>&v){
	sort(all(v));
	v.erase(unique(all(v)),v.ed);
}

template<class t>
int lwb(const vc<t>&v,const t&a){
	return lower_bound(all(v),a)-v.bg;
}

template<class t>
struct Compress{
	vc<t>v;
	Compress()=default;
	Compress(const vc<t>&x){
		add(x);
	}
	Compress(const initializer_list<vc<t> >&x){
		for(auto &p:x)add(p);
	}
	void add(const t&x){
		v.eb(x);
	}
	void add(const vc<t>&x){
		copy(all(x),back_inserter(v));
	}
	void build(){
		compress(v);
	}
	int get(const t&x)const{
		return lwb(v,x);
	}
	vc<t>get(const vc<t>&x)const{
		vc<t>res(x);
		for(auto &p:res)p=get(p);
		return res;
	}
	const t &operator[](int x)const{
		return v[x];
	}
	int size(){
		return v.size();
	}
};
void Yes(bool ex=true){
	cout<<"Yes\n";
	if(ex)exit(0);
}
void YES(bool ex=true){
	cout<<"YES\n";
	if(ex)exit(0);
}
void No(bool ex=true){
	cout<<"No\n";
	if(ex)exit(0);
}
void NO(bool ex=true){
	cout<<"NO\n";
	if(ex)exit(0);
}
void orYes(bool x,bool ex=true){
	if(x)Yes(ex);
	else No(ex);
}
void orYES(bool x,bool ex=true){
	if(x)YES(ex);
	else NO(ex);
}
void Possible(bool ex=true){
	cout<<"Possible\n";
	if(ex)exit(0);
}
void POSSIBLE(bool ex=true){
	cout<<"POSSIBLE\n";
	if(ex)exit(0);
}
void Impossible(bool ex=true){
	cout<<"Impossible\n";
	if(ex)exit(0);
}
void IMPOSSIBLE(bool ex=true){
	cout<<"IMPOSSIBLE\n";
	if(ex)exit(0);
}
void orPossible(bool x,bool ex=true){
	if(x)Possible(ex);
	else Impossible(ex);
}
void orPOSSIBLE(bool x,bool ex=true){
	if(x)POSSIBLE(ex);
	else IMPOSSIBLE(ex);
}

using uint=unsigned;
using ull=unsigned long long; 

template<uint const& MOD>
struct Modular{
	static constexpr uint const &mod=MOD;
	uint v;
	Modular(long long x=0){c(x%mod+mod);}
	Modular& c(uint x){
		v=x<mod?x:x-mod;
		return *this;
	}
	Modular pow(int k)const{
		Modular res(1),tmp(v);
		while(k){
			if(k&1)res*=tmp;
			tmp*=tmp;
			k>>=1;
		}
		return res;
	}

	Modular inv()const{return pow(mod-2);}
	Modular operator-()const{return Modular(mod-v);}

	Modular& operator+=(const Modular &x){return c(v+x.v);}
	Modular& operator-=(const Modular &x){return c(v+mod-x.v);}
	Modular& operator*=(const Modular &x){v=ull(v)*x.v%mod;return *this;}
	Modular& operator/=(const Modular &x){return *this*=x.inv();}

	Modular operator+(const Modular &x)const{return Modular(*this)+=x;}
	Modular operator-(const Modular &x)const{return Modular(*this)-=x;}
	Modular operator*(const Modular &x)const{return Modular(*this)*=x;}
	Modular operator/(const Modular &x)const{return Modular(*this)/=x;}

	friend Modular operator+(long long x,const Modular &y){return Modular(x)+y;}
	friend Modular operator-(long long x,const Modular &y){return Modular(x)-y;}
	friend Modular operator*(long long x,const Modular &y){return Modular(x)*y;}
	friend Modular operator/(long long x,const Modular &y){return Modular(x)/y;}

	friend ostream& operator<<(ostream&os,const Modular&x){
		return os<<x.v;
	}
	friend istream& operator>>(istream&is,Modular&x){
		long long p;
		is>>p;
		x=Modular(p);
		return is;
	}
	bool operator==(const Modular &x)const{return v==x.v;}
	bool operator!=(const Modular &x)const{return v!=x.v;}
	bool operator<(const Modular &x)const{return v<x.v;}
	explicit operator bool()const{return v;}
};

//uint MODULAR=998244353;
uint MODULAR=1000000007;
using Mint=Modular<MODULAR>; 

vector<Mint>fact,finv,invs;
void Initfact(int n=(1<<21)+10){
	fact.resize(n+1),finv.resize(n+1),invs.resize(n+1);
	fact[0]=1;
	for(int i=1;i<=n;i++){
		fact[i]=fact[i-1]*i;
	}
	finv[n]=fact[n].inv();
	for(int i=n-1;i>=0;i--){
		finv[i]=finv[i+1]*(i+1);
	}
	invs[0]=1;
	for(int i=0;i<=n;i++){
		invs[i]=finv[i]*fact[i-1];
	}
}

Mint comb(int n,int k){
	return fact[n]*finv[n-k]*finv[k];
}

ll n,a;
Mint dp[5005][5005][2],ans;
int main(void){
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin>>n>>a;
	Initfact(n);
	if(n==a){
		print(fact[n]);
		return 0;
	}
	dp[1][1][1]=1;
	for(int i=1;i<=a;i++){
		for(int j=0;j<=i;j++){
			dp[i+1][j+1][1]+=(dp[i][j][0]+dp[i][j][1]);
			if(j>0)dp[i+1][j-1][0]+=dp[i][j][1]*Mint(a-i);
			dp[i+1][j][0]+=dp[i][j][0]*Mint(a-i);
			if(i>1&&j>0&&n-a>=j-1)ans+=dp[i][j][1]*fact[a-i]*fact[n-a]*comb(n-a-j+1+i-2,i-2);
			if(i==a&&n-a>=j)ans+=(dp[i][j][0]+dp[i][j][1])*fact[n-a]*comb(n-a-j+i-1,i-1);
		}
	}
	print(ans);
}
