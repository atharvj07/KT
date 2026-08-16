#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;
#define rep2(x,from,to) for(long long x=(from);(x)<(to);(x)++)
#define rep(x,to) rep2(x,0,to)
#define INF 1000000000
#define N 1111
long long dp[N+4];
long long n;
long long ans;
int main()
{
	rep(i,N)
	{
		dp[i]=i*i*i;
	}
	while(1)
	{
		cin>>n;
		if(n==0)break;
		long long k=n*n*n;
		ans=0;
		rep2(i,1,n)
		{
			long long t=(long long)(lower_bound(dp,dp+N,k-i*i*i)-dp);
			//cout<<t<<"sss"<<endl;
			ans=max(ans,dp[t-1]+i*i*i);
		}
		cout<<k-ans<<endl;
	}
	return 0;
}