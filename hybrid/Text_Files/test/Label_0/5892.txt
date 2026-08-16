#include <iostream>
#include <cstdio>
 
using namespace std;
 
const int P=1000000007;
const int N=2000000;
 
int fact[N+5],invf[N+5];
int f[4][3],g[4][3];
int X1,X2,X3,X4,X5,X6,Y1,Y2,Y3,Y4,Y5,Y6,ans;
 
inline int C(int n,int m){return 1ll*fact[n+m]*invf[n]%P*invf[m]%P;}
 
inline void add(int &x,int y){(x+=y)%=P;}
 
int quick_power(int x,int y)
{
	int ret=1;
	for (;y;y>>=1,x=1ll*x*x%P) if (y&1) ret=1ll*ret*x%P;
	return ret;
}
 
void pre()
{
	fact[0]=1;
	for (int i=1;i<=N;++i) fact[i]=1ll*fact[i-1]*i%P;
	invf[N]=quick_power(fact[N],P-2);
	for (int i=N;i>=1;--i) invf[i-1]=1ll*invf[i]*i%P;
}
 
int calc(int x1,int y1,int sig1,int x2,int y2,int sig2)
{
	int ret=0;
	for(int x=X3;x<=X4;++x)
		add(ret,P-1ll*C(x-x1,Y3-1-y1)*(x+Y3)%P*C(x2-x,y2-Y3)%P),add(ret,1ll*C(x2-x,y2-Y4-1)*(x+Y4+1)%P*C(x-x1,Y4-y1)%P);
	for(int y=Y3;y<=Y4;++y)
		add(ret,P-1ll*C(y-y1,X3-1-x1)*(y+X3)%P*C(y2-y,x2-X3)%P),add(ret,1ll*C(y2-y,x2-X4-1)*(y+X4+1)%P*C(y-y1,X4-x1)%P);
	return ((ret*=sig1*sig2)+=P)%=P;
}
 
int main()
{
	pre();
	scanf("%d%d%d%d%d%d",&X1,&X2,&X3,&X4,&X5,&X6),scanf("%d%d%d%d%d%d",&Y1,&Y2,&Y3,&Y4,&Y5,&Y6),ans=0;
	f[0][0]=1,f[0][1]=X1-1,f[0][2]=Y1-1;
	f[1][0]=-1,f[1][1]=X1-1,f[1][2]=Y2;
	f[2][0]=-1,f[2][1]=X2,f[2][2]=Y1-1;
	f[3][0]=1,f[3][1]=X2,f[3][2]=Y2;
	g[0][0]=1,g[0][1]=X6+1,g[0][2]=Y6+1;
	g[1][0]=-1,g[1][1]=X6+1,g[1][2]=Y5;
	g[2][0]=-1,g[2][1]=X5,g[2][2]=Y6+1;
	g[3][0]=1,g[3][1]=X5,g[3][2]=Y5;
	for (int i=0;i<4;++i)
		for (int j=0;j<4;++j)
			add(ans,calc(f[i][1],f[i][2],f[i][0],g[j][1],g[j][2],g[j][0]));
	printf("%d\n",ans);
	fclose(stdin),fclose(stdout);
	return 0;
}