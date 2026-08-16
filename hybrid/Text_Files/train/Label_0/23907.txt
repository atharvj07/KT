#include<bits/stdc++.h>
#define X first
#define Y second
#define pb push_back
#define eb pb
#define rep(X,Y) for(int X=0;X<(Y);++X)
#define reps(X,O,Y) for(int X=O;X<(Y);++X)
#define all(X) (X).begin(),(X).end()
using namespace std;
using ll=long long;
const ll MOD=1e9+7;

map<int,int> dp[112345];

int main(){
	int n;
	cin>>n;
	vector<int> a(n);
	rep(i,n) cin>>a[i];
	dp[0][-MOD]=dp[0][MOD]=0;
	auto upd=[&](map<int,int> &nxt,int a,int b){
						 if(nxt.count(a)==0 || nxt[a]>b) nxt[a]=b;
					 };
	auto ok=[](int a,int b,int c){ return(a<b)!=(b<c);};
	rep(i,n-1){
		assert(dp[i].size()<10);
		for(auto p:dp[i]){
			if(ok(p.X,a[i],a[i+1])){
				upd(dp[i+1],a[i],p.Y);
			}
			if((p.X<a[i])==(p.X<a[i+1]) && ok(p.X,a[i+1],a[i])){
				if(i+2==n || ok(a[i+1],a[i],a[i+2])) upd(dp[i+2],a[i],p.Y+1);
			}
			if(i+2<n && ok(p.X,a[i],a[i+2]) && ok(a[i],a[i+2],a[i+1])){
				if(i+3==n || ok(a[i+2],a[i+1],a[i+3])) upd(dp[i+3],a[i+1],p.Y+1);
			}
		}
	}
	int re=MOD;
	for(auto p:dp[n-1]) re=min(re,p.Y);
	for(auto p:dp[n]) re=min(re,p.Y);
	cout<<re<<endl;
}

