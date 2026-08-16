#include<cstdio>
#include<algorithm>
#include<cstring>
#define ll long long
using namespace std;
const ll MOD=1e9+7;
ll n,a[200005],b[200005],f[4005][4005],c[4005][4005],ans;
ll quick_pow(ll x,ll a)
{
	ll ans=1;
	while(a)
	{
		if(a&1)ans=ans*x%MOD;
		x=x*x%MOD;
		a>>=1;
	}
	return ans;
}
int main()
{
	scanf("%lld",&n);
	for(int i=1;i<=n;i++)
	{
		scanf("%lld%lld",&a[i],&b[i]);
		f[-a[i]+2000][-b[i]+2000]++;
	}
	c[0][0]=1;
	for(int i=0;i<=4000;i++)
	for(int j=0;j<=4000;j++)
	{
		c[i][j]%=MOD;
		c[i+1][j]+=c[i][j];
		c[i][j+1]+=c[i][j];
	}
	for(int i=0;i<=4000;i++)
	for(int j=0;j<=4000;j++)
	{
		f[i][j]%=MOD;
		f[i+1][j]+=f[i][j];
		f[i][j+1]+=f[i][j];
	}
	for(int i=1;i<=n;i++)
	  ans+=f[a[i]+2000][b[i]+2000];
	ans%=MOD;
	for(int i=1;i<=n;i++)
	  ans=(ans-c[a[i]*2][b[i]*2]+MOD)%MOD;
	printf("%lld\n",ans*quick_pow(2,MOD-2)%MOD);
	return 0;
}