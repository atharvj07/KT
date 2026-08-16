#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int maxn=2000+10;
const int p=1e9+7;
int n,k,f[maxn][maxn],farc[maxn*maxn],inv[maxn*maxn];

int C(int n,int m){
	return (ll)farc[n]*inv[m]%p*(ll)inv[n-m]%p;
}

int main()
{
	scanf("%d%d",&n,&k);k--;
	if(!k){printf("1\n");return 0;}
	farc[0]=farc[1]=inv[0]=inv[1]=1;
	for(int i=2;i<=n*k+n+k;i++){
		farc[i]=(ll)farc[i-1]*i%p;
		inv[i]=(ll)(p-p/i)*inv[p%i]%p;
	}
	for(int i=2;i<=n*k+n+k;i++) inv[i]=(ll)inv[i]*inv[i-1]%p;
	f[0][0]=1;
	for(int i=0;i<=n;i++)
		for(int j=i;j<=n;j++){
			if(i>0) f[i][j]=(f[i][j]+f[i-1][j])%p;
			if(j>0) f[i][j]=(f[i][j]+(ll)f[i][j-1]*C(i+(j-1)*k+k-1,k-1)%p)%p;
		}
	printf("%d\n",(ll)f[n][n]*farc[n]%p);
	return 0;
}