#include<bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int,int> pii;

const int maxn=10;
#define getcode(i,j) (((i)>>(j))&1)
int n,c,l[maxn],ord[maxn];

int f[311][311][1<<5];
double calc()
{
	memset(f,0,sizeof(f));f[0][l[n]*n][0]=1;
	for(int i=0;i<c*n;i++)for(int j=0;j<=c*n;j++)for(int k=0;k<(1<<n-1);k++)if(f[i][j][k])
	{
//		printf("i= %d j= %d k= %d dp= %d\n",i,j,k,f[i][j][k]);
		if(i<j)f[i+1][j][k]+=f[i][j][k];
		int val=i%n;
		if(val==0||getcode(k,val-1))continue;
		f[i+1][min(c*n,max(j,i+l[ord[val]]*n))][k|(1<<val-1)]+=f[i][j][k];
	}
	
	double ret=f[c*n][c*n][(1<<n-1)-1];
	for(int i=1;i<n;i++)ret/=c;
	return ret;
}

int main()
{
	scanf("%d%d",&n,&c);
	for(int i=1;i<=n;i++)scanf("%d",l+i);
	sort(l+1,l+n+1);
	for(int i=1;i<n;i++)ord[i]=i;
	
	int tot=0;double ans=0.0;
	do{
		ans+=calc();
		tot++;
	}while(next_permutation(ord+1,ord+n));
	printf("%.12lf\n",ans/tot);
	return 0;
}