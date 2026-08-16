#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
typedef long long ll;
const int mod=998244353;
inline int addmod(int x)
{
	return x>=mod?x-mod:x;
}
inline int submod(int x)
{
	return x<0?x+mod:x;
}
int fpow(int x,int y)
{
	int ans=1;
	while(y)
	{
		if(y&1) ans=1ll*ans*x%mod;
		x=1ll*x*x%mod;
		y/=2;
	}
	return ans;
}
struct pt
{
	int a,b;
	pt(int a=0,int b=0):a(a),b(b){}
};
pt operator+(const pt x,const pt y)
{
	return pt(addmod(x.a+y.a),addmod(x.b+y.b));
}
pt operator-(const pt x,const pt y)
{
	return pt(submod(x.a-y.a),submod(x.b-y.b));
}
pt operator*(const pt x,const pt y)
{
	return pt(addmod(1ll*x.a*y.a%mod+5ll*x.b*y.b%mod),addmod(1ll*x.a*y.b%mod+1ll*x.b*y.a%mod));
}
pt getinv(pt x)
{
	int nw=submod(1ll*x.a*x.a%mod-5ll*x.b*x.b%mod);
	nw=fpow(nw,mod-2);
//	printf("nw=%d\n",nw);
	return pt(1ll*x.a*nw%mod,addmod(mod-1ll*x.b*nw%mod));
}
pt pfpow(pt x,ll y)
{
	pt ans=pt(1);
	while(y)
	{
		if(y&1) ans=ans*x;
		x=x*x;
		y/=2;
	}
	return ans;
}
int n,inv2,c[1000005],pn=2e5;
ll m;
pt p,q,invp,invq,dp[200005],ans;
void print(pt x)
{
	printf("(%d,%d) ",x.a,x.b);
}
int main()
{
	inv2=fpow(2,mod-2);
	scanf("%d%lld",&n,&m);
	c[0]=1;
	for(int i=1;i<=pn;i++)
		c[i]=1ll*c[i-1]*((m+i)%mod)%mod*fpow(i,mod-2)%mod;
	p=pt(inv2,inv2);
	q=pt(inv2,mod-inv2);
	invp=getinv(p-pt(1));
	invq=getinv(q-pt(1));
//	print(p),print(q),print(invp),print(invq);
//	printf("\n");
	//print((p-pt(1)));
//	print((p-pt(1))*invp),print((q-pt(1))*invq);
	dp[1]=pfpow(p,m);
	for(int i=2;i<=n;i++)
		dp[i]=(dp[i-1]*p-pt(c[i-2]))*invp;
	ans=dp[n];
	dp[1]=pfpow(q,m);
	for(int i=2;i<=n;i++)
		dp[i]=(dp[i-1]*q-pt(c[i-2]))*invq;
	ans=ans-dp[n];
	ans=ans*getinv(pt(0,1));
	//print(ans);
	printf("%d\n",ans.a);
	return 0;
}