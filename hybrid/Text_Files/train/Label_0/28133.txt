#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
#define N 105

LL n,m,p,mod,ans,f[N][4][N][N],fac[N],ifac[N];

void upd(LL &x,LL y){x=(x+y)%mod;}

LL inv(LL x){return x==1?1:(mod-mod/x)*inv(mod%x)%mod;}

LL C(LL x,LL y){return fac[x]*ifac[y]%mod*ifac[x-y]%mod;}

int main(){
	scanf("%lld%lld%lld%lld",&n,&m,&p,&mod);
	if (n<m) swap(n,m);
	fac[0]=1; for (LL i=1;i<=n;++i) fac[i]=fac[i-1]*i%mod;
	ifac[n]=inv(fac[n]); for (LL i=n-1;~i;--i) ifac[i]=ifac[i+1]*(i+1)%mod;
	f[p+1][3][n][m]=1;
	for (LL i=p;i;--i){
		LL prd1,prd2;
		prd1=prd2=1;
		for (LL j=1;j<=n;++j) prd2=prd2*i%mod;
		for (LL j=0;j<=n;++j){
			LL tmp=1;
			for (LL l=0;l<=m;++l){
				for (LL k=l;k<=m;++k)
					upd(f[i][0][j][k-l],f[i+1][3][j][k]*tmp%mod*ifac[l]);
				tmp=tmp*prd1%mod*prd2%mod;
			}
			prd1=prd1*(p-i+1)%mod;
			prd2=prd2*inv(i)%mod;
		}
		prd1=prd2=1;
		for (LL k=1;k<=m;++k) prd2=prd2*i%mod;
		for (LL k=0;k<=m;++k){
			LL tmp=1;
			for (LL l=0;l<=n;++l){
				for (LL j=l;j<=n;++j)
					upd(f[i][1][j-l][k],f[i][0][j][k]*tmp%mod*ifac[l]);
				tmp=tmp*prd1%mod*prd2%mod;
			}
			prd1=prd1*(p-i+1)%mod;
			prd2=prd2*inv(i)%mod;
		}
		if (i>1){
			prd1=prd2=1;
			for (LL j=1;j<=n;++j) prd2=prd2*(i-1)%mod;
			for (LL j=0;j<=n;++j){
				LL tmp=1;
				for (LL l=0;l<=m;++l){
					for (LL k=l;k<=m;++k)
						upd(f[i][2][j][k-l],f[i][1][j][k]*tmp%mod*ifac[l]);
					tmp=-tmp*prd1%mod*prd2%mod;
				}
				prd1=prd1*(p-i+1)%mod;
				prd2=prd2*inv(i-1)%mod;
			}
			prd1=prd2=1;
			for (LL k=1;k<=m;++k) prd2=prd2*(i-1)%mod;
			for (LL k=0;k<=m;++k){
				LL tmp=1;
				for (LL l=0;l<=n;++l){
					for (LL j=l;j<=n;++j)
						upd(f[i][3][j-l][k],f[i][2][j][k]*tmp%mod*ifac[l]);
					tmp=-tmp*prd1%mod*prd2%mod;
				}
				prd1=prd1*(p-i+1)%mod;
				prd2=prd2*inv(i-1)%mod;
			}
		}
		else{
			memcpy(f[i][2],f[i][1],sizeof f[i][2]);
			memcpy(f[i][3],f[i][2],sizeof f[i][3]);
		}
	}
	ans=(f[1][3][0][0]*fac[n]%mod*fac[m]%mod+mod)%mod;
	printf("%lld\n",ans);
	
	return 0;
}
			