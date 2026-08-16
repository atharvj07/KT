#include<bits/stdc++.h>
#define N 2005
#define LL long long
using namespace std;
const int mo=1e9+7;
int n,k,f[N][N],s[N][N],ans;
LL fpm(LL x,LL y){ LL s=1; while(y){ if(y&1) s=(s*x)%mo; y>>=1,x=(x*x)%mo;} return s;}
void inc(int &x,int y){ x=x+y>=mo ? x+y-mo : x+y;}
int main()
{
	int i,j;
	cin>>n>>k;
	f[n+1][0]=s[n+1][0]=1;
	for(i=n;i>=1;i--)
		for(j=n;j>=0;j--){
			if(i!=1) f[i][j]=f[i][j+1];
			inc(f[i][j],s[i+1][j]);
			s[i][j]=s[i+1][j-1];
			inc(s[i][j],f[i][j]);
		  }
	ans=1LL*f[1][n-k]*fpm(2,max(n-k-1,0))%mo;
	cout<<ans;
	return 0;
}
