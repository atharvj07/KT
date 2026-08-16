/* bit DP, O(n*2^(2n)) */

#include<cstdio>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int main(){
	int sw[1024];
	rep(S,1024){
		sw[S]=0;
		if(S&1) sw[S]^=3;
		for(int i=1;i<9;i++) if(S&(1<<i)) sw[S]^=(7<<(i-1));
		if(S&512) sw[S]^=768;
	}

	int T; scanf("%d",&T);
	while(T--){
		int cell[10]={};
		rep(i,10){
			cell[i]=0;
			rep(j,10){
				int tmp; scanf("%d",&tmp);
				cell[i]|=(tmp<<(9-j));
			}
		}

		static int dp[11][1024];
		// dp[r][stat] : rsÚÌXCb`ðµûstat(bit\»)Åµ½Æ«ÉAr-1sÚª·×Ä0ÉÈéæ¤Èr-1sÚÌXCb`Ìµû
		rep(S,1024) dp[0][S]=0;
		rep(r,10){
			rep(S,1024){
				dp[r+1][S]=-1;
				rep(B,1024){
					if(dp[r][B]==-1) continue;
					if((cell[r]^dp[r][B]^sw[B]^S)==0) dp[r+1][S]=B;
				}
			}
		}

		int ans[10];
		for(int i=0,S=dp[10-i][0];i<10;i++,S=dp[10-i][S]) ans[i]=S;
		for(int i=9;i>=0;i--){
			rep(k,10) printf("%d%c",!!(ans[i]&(1<<(9-k))),k<9?' ':'\n');
		}
	}

	return 0;
}