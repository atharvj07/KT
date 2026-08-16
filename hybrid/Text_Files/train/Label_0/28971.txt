#include<bits/stdc++.h>
#define INF 0x3f3f3f3f
#define ll long long
#define PII pair<int,int>
#define All(a) a.begin(),a.end()
using namespace std;
const int mx=2e5+5;
const int mxn=(1<<17)+5;
int n,k,pos[17][mx],dp[mxn];
char s[mx];
bool check(int mid) {
	for(int i=0;i<k;i++) {
		int cnt=0;
		for(int j=n;j>=1;j--) {
			cnt=(s[j]=='a'+i||s[j]=='?')?cnt+1:0;
			if(cnt>=mid) pos[i][j]=j+mid-1;
			else pos[i][j]=pos[i][j+1];
		}
	}
	dp[0]=0;
	for(int i=1;i<(1<<k);i++) {
		dp[i]=INF;
		for(int j=0;j<k;j++) {
			if((i>>j)&1 && dp[i-(1<<j)]!=INF && pos[j][dp[i-(1<<j)]+1]) {
				dp[i]=min(dp[i],pos[j][dp[i-(1<<j)]+1]);
			}
		}
	}
	return dp[(1<<k)-1]!=INF;
}
int main() {
	scanf("%d%d%s",&n,&k,s+1);
	int l=1,r=n/k,res=0;
	while(l<=r) {
		int mid=(l+r)>>1;
		if(check(mid)) res=mid,l=mid+1;
		else r=mid-1;
	}
	printf("%d",res);
} 