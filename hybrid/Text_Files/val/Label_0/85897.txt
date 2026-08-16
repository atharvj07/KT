#include<bits/stdc++.h>
using namespace std;
const int N=2e5+10;
map<int,int> dp;
int n,cnt[N][26],state[N];
char s[N];
int main()
{
	scanf("%s",s+1);
	n=strlen(s+1);
	for (int i=1;i<=n;i++){
		for (int j=0;j<26;j++) cnt[i][j]=cnt[i-1][j];
		cnt[i][s[i]-'a']^=1;
		for (int j=0;j<26;j++) state[i]|=(cnt[i][j]<<j);
	}
	dp[0]=0;
	for (int i=1;i<=n;i++){
		int now=state[i];
		if (!dp.count(now)) dp[now]=1e9;
		int v=dp[now]+1;
		for (int j=0;j<26;j++)
			if (dp.count(now^(1<<j))) v=min(v,dp[now^(1<<j)]+1);		
		dp[now]=min(dp[now],v);
		if (i==n) printf("%d\n",v);
	}
	return 0;
}