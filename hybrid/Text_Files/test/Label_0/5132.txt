#include <bits/stdc++.h>

using namespace std;

#define mkp make_pair
#define pb push_back
#define fi first
#define se second
#define lb(x) ((x)&(-(x)))
#define SZ(x) ((int)((x).size())) 
typedef long long ll;
typedef pair<int,int> pii;

const int MAXN=5e3+10; 

int n;
int tag[MAXN],s[MAXN];
ll dp[MAXN];

void solve()
{
	scanf("%d",&n);
	for(int i=1;i<=n;i++) scanf("%d",&tag[i]);
	for(int i=1;i<=n;i++) scanf("%d",&s[i]);
	
	memset(dp,0,sizeof(dp));
	for(int i=1;i<=n;i++)
		for(int j=i-1;j>=1;j--)
		{
			if(tag[i]==tag[j]) continue;
			int x=abs(s[i]-s[j]);
			ll v1=dp[i],v2=dp[j];
			dp[i]=max(dp[i],v2+x);
			dp[j]=max(dp[j],v1+x);
		}
	
	ll ans=0;
	for(int i=1;i<=n;i++)
		ans=max(ans,dp[i]);
	printf("%lld\n",ans);
}

int main()
{
	int T;
	scanf("%d",&T);
	while(T--) solve();
	return 0;
}