#include<bits/stdc++.h>
using namespace std;
const int twx=1000000007;
long long n,m,a,dp[100010];
bool pan[100010];
int main() {
	scanf("%lld %lld",&n,&m);
	for(int i=1;i<=m;i++) {
		scanf("%lld",&a);
		pan[a]=1;
	}
	dp[0]=1;
	for(int i=1;i<=n;i++)
	if(!pan[i])
		if(i==1) 
		    dp[i]=dp[0];
		else
			dp[i]=((dp[i]+dp[i-1])%twx+dp[i-2])%twx;
	printf("%d\n",dp[n]);
}