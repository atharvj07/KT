#include<iostream>
#include<bitset>
#include<algorithm>
using namespace std;
int H,W;
int T[88][88],A[88][88],B[88][88];
bitset<25600>dp[81][81];
int main()
{
	cin>>H>>W;
	for(int i=0;i<H;i++)for(int j=0;j<W;j++)cin>>A[i][j];
	for(int i=0;i<H;i++)for(int j=0;j<W;j++)cin>>B[i][j];
	for(int i=0;i<H;i++)for(int j=0;j<W;j++)T[i][j]=abs(A[i][j]-B[i][j]);
	dp[0][0][12800+T[0][0]]=1;
	for(int i=0;i<H;i++)for(int j=0;j<W;j++)
	{
		if(i+1<H)dp[i+1][j]|=dp[i][j]<<T[i+1][j]|dp[i][j]>>T[i+1][j];
		if(j+1<W)dp[i][j+1]|=dp[i][j]<<T[i][j+1]|dp[i][j]>>T[i][j+1];
	}
	int ans=0;
	while(!dp[H-1][W-1][12800+ans]&&!dp[H-1][W-1][12800-ans])ans++;
	cout<<ans<<endl;
}
