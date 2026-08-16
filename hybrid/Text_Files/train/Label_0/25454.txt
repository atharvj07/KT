#include<bits/stdc++.h>
#define rg register
using namespace std;
const int mod=1e9+7;
#define _ 2001
int n, k, f[_][_], sum[_*_];
int qp(int x, int y){
	int ans=1;
	while(y){
		if(y&1)ans=1ll*ans*x%mod;
		x=1ll*x*x%mod, y>>=1;
	}return ans;
}
int C(int m, int r){return 1ll*sum[m]*qp(sum[r], mod-2)%mod*qp(sum[m-r], mod-2)%mod;}
int main(){
	sum[0]=sum[1]=1;
	for(int i=2; i<=2000*2000; ++i)
		sum[i]=1ll*sum[i-1]*i%mod;
	
	scanf("%d%d", &n, &k);
	if(k==1){puts("1"); return 0;}
	f[0][0]=1;
	for(int i=1; i<=n; ++i)
		for(int j=0; j<=i; ++j){
			f[i][j]=f[i-1][j];
			if(j)(f[i][j]+=1ll*C((n-j+1)*(k-1)+n-i-1, k-2)*f[i][j-1]%mod)%=mod;
		}
	for(int i=2; i<=n; ++i)
		f[n][n]=1ll*f[n][n]*i%mod;
	printf("%d", f[n][n]);
}
