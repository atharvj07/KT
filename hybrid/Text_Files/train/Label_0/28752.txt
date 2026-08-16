//Code by 27.
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<math.h>
#include<vector>
#include<queue>
#include<map>
#include<stack>
#include<fstream>
#include<stdlib.h>
#include<set>
#include<climits>
#include<cmath>  
#include<memory.h> 
#include<sstream>
#include<time.h>
#include<iomanip>
using namespace std;
const unsigned long long BIGEST=1000000000000000000+1000000000000000000;
const long long BIGER=1000000000000000000;
const int BIG=1000000000;
const int MOD=1000000007;
const long long LMOD=1000000007;
long long n,d;
long long a[300005];
long long dp[2][300005];
int main()
{
	long long res=0;
	scanf("%lld%lld",&n,&d);
	for(long long i=1;i<=n;i++)
	{
		scanf("%lld",&a[i]);
		res+=a[i];
	}
	res+=d*(n-1);
	dp[0][1]=a[1];
	for(long long i=2;i<=n;i++)
	{
		dp[0][i]=min(dp[0][i-1]+d,a[i]);
	}
	dp[1][n]=a[n];
	for(long long i=n-1;i>=1;i--)
	{
		dp[1][i]=min(dp[1][i+1]+d,a[i]);
	}
	for(long long i=2;i<n;i++)
	{
		res+=min(dp[0][i],dp[1][i]);
		//cout<<dp[0][i]<<" "<<dp[1][i]<<endl;
	}
	cout<<res;
	return 0;
}