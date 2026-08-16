#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#define SIZE 18
#define BT (1<<18)
#define MX 100005
#define MOD 1000000007

using namespace std;
typedef long long int ll;
typedef pair <int,int> P;

ll fac[MX],finv[MX],inv[MX];
int A[SIZE];
ll dp[2][BT];

void make()
{
	fac[0]=fac[1]=1;
	finv[0]=finv[1]=1;
	inv[1]=1;
	for(int i=2;i<MX;i++)
	{
		inv[i]=MOD-inv[MOD%i]*(MOD/i)%MOD;
		fac[i]=fac[i-1]*(ll) i%MOD;
		finv[i]=finv[i-1]*inv[i]%MOD;
	}
}
ll C(int a,int b)
{
	if(a<b) return 0;
	return fac[a]*(finv[b]*finv[a-b]%MOD)%MOD;
}
int main()
{
	make();
	int n,m;
	scanf("%d %d",&n,&m);
	for(int i=0;i<m;i++) scanf("%d",&A[i]);
	int pos=0;
	memset(dp[pos],0,sizeof(dp[pos]));
	dp[pos][0]=1;
	for(int i=m-1;i>=0;i--)
	{
		pos^=1;
		memset(dp[pos],0,sizeof(dp[pos]));
		for(int S=0;S<1<<n;S++)
		{
			if(dp[pos^1][S]==0) continue;
			dp[pos][S]+=dp[pos^1][S];
			if(dp[pos][S]>=MOD) dp[pos][S]-=MOD;
			int zan=(1<<n)-A[i]+1;
			for(int j=0;j<n;j++) if(S>>j&1) zan-=(1<<j);
			for(int j=0;j<n;j++)
			{
				if(!(S>>j&1)&&zan>=(1<<j))
				{
					dp[pos][S|(1<<j)]+=dp[pos^1][S]*C(zan-1,(1<<j)-1)%MOD*fac[1<<j]%MOD;
					if(dp[pos][S|(1<<j)]>=MOD) dp[pos][S|(1<<j)]-=MOD;
				}
			}
		}
	}
	ll all=0;
	for(int S=0;S<1<<n;S++)
	{
		ll way=dp[pos][S];
		int zan=(1<<n)-1;
		int sgn=1;
		for(int i=0;i<n;i++)
		{
			if(S>>i&1)
			{
				zan-=(1<<i);
				sgn*=-1;
			}
		}
		way=way*fac[zan]%MOD;
		//if(way!=0) printf("%d %lld\n",S,way);
		all+=(ll) sgn*way;
		all+=MOD;
		all%=MOD;
	}
	printf("%lld\n",all*(1<<n)%MOD);
	return 0;
}
