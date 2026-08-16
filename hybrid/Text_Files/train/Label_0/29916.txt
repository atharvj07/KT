#include <cstdio>
#include <algorithm>

int n,m,k,P;
int f[201][201],C[201][201],_mul[201],invmul[201];
inline int mul(const int &a,const int &b){return 1ll*a*b%P;}
inline int add(int a,const int &b){a+=b;return(a>=P)?a-P:a;}
int calc(int n,int m,int k){
	if(n>k+1||m>k)return 0;
	--n;
	for(int i=1;i<=n;i++)
		for(int j=0;j<=m;j++)
			f[i][j]=-1;
	for(int i=1;i<=n;i++)
		for(int j=std::max(0,i+m-k);j<=k-n+i&&j<=m;j++){ 
			f[i][j]=0;
		}
	for(int i=0;i<=m;i++)f[0][i]=0;
	f[0][0]=1;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++)f[i-1][j]=add(f[i-1][j],f[i-1][j-1]);
		for(int j=0;j<=m;j++)
			if(!f[i][j]){
				f[i][j]=f[i-1][j];
			}
			else f[i][j]=0;
	}
	int cnt=0;
	for(int i=1;i<=m;i++)cnt=add(cnt,f[n][i]);
//	printf("%d %d %d %d\n",n,m,k,cnt);
	return cnt;
}
int g(int n,int k){
	int tot=0;
	for(int i=2;i<n;i++)
		tot=add(tot,mul(mul(mul(C[n-1][i-1],_mul[i-1]),_mul[n-i]),calc(i,n-i,k)));
//	printf("g %d %d %d\n",n,k,tot);
	return tot;
}
int main(){
	scanf("%d%d%d",&n,&k,&P);
	for(int i=0;i<=n;i++){
		C[i][0]=1;
		for(int j=1;j<=i;j++)
			C[i][j]=add(C[i-1][j],C[i-1][j-1]);
	}
	_mul[0]=_mul[1]=invmul[0]=invmul[1]=1;
	for(int i=2;i<=n;i++)_mul[i]=mul(_mul[i-1],i);
	for(int i=2;i<=n;i++)invmul[i]=mul(P-P/i,invmul[P%i]);
	for(int i=2;i<=n;i++)invmul[i]=mul(invmul[i],invmul[i-1]);
	int ans=(k==n-1)?_mul[n]:0;
	for(int i=3;i<=n;i++){
		ans=add(ans,mul(C[n][i],mul(_mul[n-i],g(i,k-n+i))));
	}
	printf("%d\n",ans);
}