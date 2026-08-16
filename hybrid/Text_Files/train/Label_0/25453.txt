#include<bits/stdc++.h>
using namespace std;
const int mo=1000000007;
const int N=2005;
int fac[N*N],inv[N*N];
int n,k,m,f[N][N];
int C(int x,int y){
	return 1ll*fac[x]*inv[y]%mo*inv[x-y]%mo;
}
int main(){
	scanf("%d%d",&n,&k);
	m=n*k; fac[0]=inv[0]=inv[1]=1;
	for (int i=2;i<=m;i++)
		inv[i]=1ll*(mo-mo/i)*inv[mo%i]%mo;
	for (int i=1;i<=m;i++)
		fac[i]=1ll*fac[i-1]*i%mo,
		inv[i]=1ll*inv[i-1]*inv[i]%mo;
	if (k==1) return puts("1"),0;
	f[0][0]=1; k-=2;
	for (int i=0;i<=n;i++)
		for (int j=0;j<=i;j++){
			if (i!=j)
				f[i][j+1]=(f[i][j+1]+1ll*C((n-i)+(n-j-1)+(n-j)*k,k)*f[i][j]%mo*(n-j))%mo;
			if (i<n) f[i+1][j]=(f[i+1][j]+f[i][j])%mo;
		}
	printf("%d\n",f[n][n]);
}