#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;
using lint=long long;

int memo[51][51][51];

bool check(int x,int y,int k){
	int& res=memo[x][y][k];
	if(res!=-1) return res;

	if(x==y) return res=true;
	if(k==0) return res=false;
	return res=check(x,y,k-1)||check(x%k,y,k-1);
}

int main(){
	memset(memo,-1,sizeof memo);

	int n; scanf("%d",&n);
	vector<int> a(n),b(n);
	rep(i,n) scanf("%d",&a[i]);
	rep(i,n) scanf("%d",&b[i]);

	{
		bool ok=true;
		rep(i,n) if(!check(a[i],b[i],50)) ok=false;
		if(!ok){
			puts("-1");
			return 0;
		}
	}

	vector<lint> S(n);
	rep(i,n) S[i]=1LL<<a[i];

	lint ans=0;
	for(int k=50;k>0;k--){
		vector<bool> ok(n,true);
		rep(i,n){
			bool ok2=false;
			rep(x,51) if(S[i]>>x&1) {
				if(check(x,b[i],k-1)) ok2=true;
			}
			if(!ok2) ok[i]=false;
		}

		if(count(ok.begin(),ok.end(),false)>0){
			ans|=1LL<<k;
			rep(i,n){
				lint next=(ok[i]?S[i]:0);
				rep(x,51) if(S[i]>>x&1) next|=1LL<<x%k;
				S[i]=next;
			}
		}
	}
	printf("%lld\n",ans);

	return 0;
}
