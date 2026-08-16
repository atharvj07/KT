#include<iostream>
#include<cstdio>
#define ll long long
using namespace std;
const ll mod=1e9 +7;
int n,k;
ll f[2020][2020],jc[4040404],jc_n[4040404];
ll C(int x,int y)
{
	if (y<0 || y>x) return 0;
	if (y==0 || x==y) return 1;
	ll sss=jc[x];
	sss=sss*jc_n[x-y]%mod*jc_n[y]%mod;
	return sss;
}
int main()
{
	jc[1]=1;
	jc_n[1]=1;
	for (int i=2;i<=4000010;++i)
	{
		jc[i]=jc[i-1]*i%mod;
		jc_n[i]=(mod-mod/i)*jc_n[mod%i]%mod;
	}
	for (int i=2;i<=4000010;++i)
		jc_n[i]=jc_n[i]*jc_n[i-1]%mod;

	//printf("%lld\n",C(5,1));
	scanf("%d%d",&n,&k);
	if (k==1)
	{
		printf("1\n");
		return 0;
	}
	f[0][0]=1;
	for (int i=0;i<=n;++i)
		for (int j=n;j>=0;--j)
		if (f[i][j])
		{
			if (j) f[i][j-1]=(f[i][j-1]+f[i][j])%mod;
			f[i+1][j+1]=(f[i+1][j+1]+C(i*k-j+k-2,k-2)*f[i][j]%mod)%mod;
		}
	printf("%lld\n",f[n][0]*jc[n]%mod);
	return 0;
}