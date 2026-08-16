#include<cstdio>
#include<map>
#include<algorithm>

using namespace std;

long long c[10];

const long long INF=2e18;

map<long long,long long> dp;

long long dfs(long long x)
{
	if(!x)return 0;
	if(dp.count(x))return dp[x];
	long long tmp[6]={x/2,x/2+1,x/3,x/3+1,x/5,x/5+1},t[6]={2,2,3,3,5,5};
	long long ans=INF;for(int i=0;i<6;i++)if(tmp[i]<x)ans=min(ans,dfs(tmp[i])+(long long)min((long double)abs(tmp[i]-x)*c[0],abs(tmp[i]*t[i]-x)*(long double)c[0]+c[t[i]]));
	return dp[x]=ans;
}

int main()
{
	int T=0;scanf("%d",&T);
	while(T--)
	{
		long long x=0;scanf("%lld%lld%lld%lld%lld",&x,&c[2],&c[3],&c[5],&c[0]);
		printf("%lld\n",dfs(x));
		dp.clear();
	}
}