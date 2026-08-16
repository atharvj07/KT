#include<bits/stdc++.h>
#define int long long
using namespace std;
int n,ans,P;
int a[1000001],g[100001],ni=0,gg[100001],nt;
signed main(){
	cin>>n>>a[1]>>P;
	int np=a[1],lp=np;
	while(!g[np]){
		ans+=np;gg[np]=ans;
		g[np]=++ni;if(ni>=n)break;lp=np;np=np*np%P;
	}
	if(ni>=n){
		printf("%lld\n",ans);
		return 0;
	}
	
	ni++;nt=ans-gg[np]+np;
	int nn=(n-g[lp])%(ni-g[np]);ans+=(n-g[lp])/(ni-g[np])*nt;
	for(int i=np,ni=1;ni<=nn;ni++,i=i*i%P)ans+=i;
	printf("%lld\n",ans);
	return 0;
}
/*
100 4 17
10 4 7
*/