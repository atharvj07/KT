#include<stdio.h>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
int ABS(int a){
	return max(a,-a);
}
int dp1[1<<7][7];
int dist[1<<7];
long long dp2[8][10100];
long long val[1<<7];
long long dp3[11000];
char in[20];
int v[20];
int p[20];
int x[20];
int y[20];
int g[20][20];
int main(){
	int a,b,c,d;
	scanf("%d%d%d%d",&a,&b,&c,&d);
	map<string,int> m;
	for(int i=0;i<b;i++){
		scanf("%s%d%d",in,v+i,p+i);
		string tmp=in;
		m[tmp]=i;
	}
	for(int i=0;i<a;i++)for(int j=0;j<b;j++)
		g[i][j]=-1;
	for(int i=0;i<a;i++){
		int q;
		scanf("%d%d%d",&q,x+i,y+i);
		for(int j=0;j<q;j++){
			int r;
			scanf("%s%d",in,&r);
			string tmp=in;
			int num=m[tmp];
			if(p[num]>r)g[i][num]=p[num]-r;
		}
	}
	for(int i=0;i<(1<<a);i++)for(int j=0;j<a;j++)
		dp1[i][j]=999999999;
	for(int i=0;i<a;i++)dp1[1<<i][i]=ABS(x[i])+ABS(y[i]);
	for(int i=0;i<(1<<a);i++)for(int j=0;j<a;j++){
		for(int k=0;k<a;k++){
			dp1[i|(1<<k)][k]=min(dp1[i|(1<<k)][k],dp1[i][j]+ABS(x[j]-x[k])+ABS(y[j]-y[k]));
		}
	}
	for(int i=0;i<(1<<a);i++){
		dist[i]=999999999;
		for(int j=0;j<a;j++)dist[i]=min(dist[i],dp1[i][j]+ABS(x[j])+ABS(y[j]));
	}
	for(int i=0;i<(1<<a);i++){
		for(int j=0;j<=a;j++)for(int k=0;k<=c;k++)dp2[j][k]=-999999999;
		dp2[0][0]=0;
		for(int j=0;j<a;j++)for(int k=0;k<=c;k++){
			dp2[j+1][k]=max(dp2[j+1][k],dp2[j][k]);
			if(!(i&(1<<j)))continue;
			for(int l=0;l<b;l++)if(~g[j][l]&&k+v[l]<=c)dp2[j][k+v[l]]=max(dp2[j][k+v[l]],dp2[j][k]+g[j][l]);
		}
		for(int j=0;j<=c;j++)val[i]=max(val[i],dp2[a][j]);
	}
	for(int i=0;i<d;i++){
		for(int j=0;j<(1<<a);j++){
			if(i+dist[j]<=d)dp3[i+dist[j]]=max(dp3[i+dist[j]],dp3[i]+val[j]);
		}
	}
	long long ret=0;
	for(int i=0;i<=d;i++)ret=max(ret,dp3[i]);
	printf("%lld\n",ret);
}