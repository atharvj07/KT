#include<bits/stdc++.h>
using namespace std;
#define RI register int
int read() {
	int q=0;char ch=' ';
	while(ch<'0'||ch>'9') ch=getchar();
	while(ch>='0'&&ch<='9') q=q*10+ch-'0',ch=getchar();
	return q;
}
const int mod=1e9+7,N=200005,inf=0x3f3f3f3f;
vector<int> orz[N];
int mi=inf,mic,mii,X,Y,ans,js,n,a[N],fac[N],ni[N];
int ksm(int x,int y) {
	int re=1;
	for(;y;y>>=1,x=1LL*x*x%mod) if(y&1) re=1LL*re*x%mod;
	return re;
}
int main()
{
	int c,w;
	n=read(),X=read(),Y=read();
	for(RI i=1;i<=n;++i) {
		c=read(),w=read(),orz[c].push_back(w);
		if(w<=mi) mii=mi,mi=w,mic=c;
		else if(w<mii) mii=w;
	}
	for(RI i=1;i<=n;++i) sort(orz[i].begin(),orz[i].end());
	for(RI i=1;i<=n;++i) {
		if(!(int)(orz[i].size())) continue;
		if(i==mic) {
			a[i]=1,++js;
			for(RI j=1;j<orz[i].size();++j)
				if(orz[i][j]+mii<=Y||orz[i][j]+orz[i][0]<=X) ++a[i],++js;
		}
		else {
			if(orz[i][0]+mi>Y) continue;
			a[i]=1,++js;
			for(RI j=1;j<orz[i].size();++j)
				if(orz[i][j]+mi<=Y||orz[i][j]+orz[i][0]<=X) ++a[i],++js;
		}
	}
	fac[0]=1;for(RI i=1;i<=n;++i) fac[i]=1LL*fac[i-1]*i%mod;
	ni[n]=ksm(fac[n],mod-2);
	for(RI i=n-1;i>=0;--i) ni[i]=1LL*ni[i+1]*(i+1)%mod;
	ans=fac[js];
	for(RI i=1;i<=n;++i) ans=1LL*ans*ni[a[i]]%mod;
	printf("%d\n",ans);
    return 0;
}