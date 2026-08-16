#include<bits/stdc++.h>
#define ll long long
using namespace std;
const ll maxn=205;
const ll cn0=0;
const ll mod=1e9+7;
ll b[maxn],c[maxn],bp[maxn],bpp[maxn],cp[maxn],dp[maxn][maxn*maxn];
int n;
int main(){
	cin>>n;bp[0]=bpp[0]=cp[0]=0; 
	for(int i=1;i<=n;i++){scanf("%lld",&c[i]);cp[i]=c[i]+cp[i-1];}
	for(int i=1;i<n;i++){scanf("%lld",&b[i]);bp[i]=bp[i-1]+b[i];bpp[i]=bpp[i-1]+bp[i];}
	memset(dp,0,sizeof(dp));int q;cin>>q;int x;cin>>x;
	for(int i=max(0,x);i<=c[1];i++)dp[1][i]=1;
	for(ll i=2;i<=n;i++){
		for(ll j=max(cn0,x*i+bpp[i-1]);j<=cp[i];j++){
			for(ll k=max(cn0,j-c[i]);k<=j;k++){
				dp[i][j]=(dp[i][j]+dp[i-1][k])%mod;
			}
		}
	}
	ll ans=0;
	for(int i=0;i<=cp[n];i++)ans=(ans+dp[n][i])%mod;
	printf("%lld\n",ans);
}
