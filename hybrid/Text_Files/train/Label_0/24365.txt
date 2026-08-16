#include <bits/stdc++.h>
using namespace std;

#define dump(...) cout<<"# "<<#__VA_ARGS__<<'='<<(__VA_ARGS__)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;

constexpr int INF=1e9;
constexpr int MOD=1e9+7;
constexpr double EPS=1e-9;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}
template<typename Ch,typename Tr,typename C,typename=decltype(begin(C()))>
basic_ostream<Ch,Tr>& operator<<(basic_ostream<Ch,Tr>& os,const C& c){
	os<<'[';
	for(auto i=begin(c);i!=end(c);++i)
		os<<(i==begin(c)?"":" ")<<*i;
	return os<<']';
}

int main()
{
	for(int n;cin>>n && n;){
		vvi a(n,vi(4));
		rep(i,n) rep(j,4) cin>>a[i][j];
		sort(all(a),[](const vi& a,const vi& b){
			if(a[2]!=b[2]) return a[2]>b[2];
			if(a[3]!=b[3]) return a[3]<b[3];
			return a[0]<b[0];
		});
		
		map<int,int> f;
		vi res;
		for(int i=0;i<n && res.size()<26;i++)
			if(res.size()<10){
				if(f[a[i][1]]<3){
					res.push_back(a[i][0]);
					f[a[i][1]]++;
				}
			}
			else if(res.size()<20){
				if(f[a[i][1]]<2){
					res.push_back(a[i][0]);
					f[a[i][1]]++;
				}
			}
			else if(res.size()<26){
				if(f[a[i][1]]==0){
					res.push_back(a[i][0]);
					f[a[i][1]]++;
				}
			}
		for(int x:res) cout<<x<<endl;
	}
}