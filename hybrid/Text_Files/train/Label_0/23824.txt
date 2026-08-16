#include<bits/stdc++.h>
using namespace std;
const int N=1e3+2;
const int mod=1e9+7;
int dp[N],c[N][N],ar[N],ndp[N];
void add(int &x,int y){
	x+=y;
	if(x>=mod){
		x-=mod;
	}
}
int mul(int x,int y){
	return (1ll*x*y)%mod;
}
signed main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n,i,j,k,l,num;
	cin>>n>>num;
	for(i=1;i<=num;i++){
		cin>>ar[i];
	}
	c[0][0]=dp[0]=1;
	for(i=1;i<=n;i++){
		for(j=0;j<=i;j++){
			c[j][i]=c[j][i-1];
			if(j){
				add(c[j][i],c[j-1][i-1]);
			}
		}
	}
	for(i=1;i<=num;i++){
		for(k=n;k>-1;k--){
			for(l=min(ar[i],n-k);l>-1;l--){
				add(ndp[k+l],mul(mul(dp[k],c[l][n-k]),c[ar[i]-l][n-l]));
			}
		}
		for(j=0;j<=n;j++){
			dp[j]=ndp[j];
			ndp[j]=0;
		}
	}
	cout<<dp[n];
}