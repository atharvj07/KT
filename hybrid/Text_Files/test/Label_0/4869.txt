#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define x first
#define y second
#define mp make_pair
#define pb push_back
#define enum(i,x,y) for(int i=(x);i<=(y);++i)
#define try(i,x,y) for(int i=(x);i>=(y);--i)
template <typename TYPE> inline void chkmax(TYPE &x,TYPE y){x<y?x=y:0;}
template <typename TYPE> inline void chkmin(TYPE &x,TYPE y){y<x?x=y:0;}
template <typename TYPE> void readint(TYPE &x)
{
    x=0;int f=1;char c;
    for(c=getchar();!isdigit(c);c=getchar())if(c=='-')f=-1;
    for(;isdigit(c);c=getchar())x=x*10+c-'0';
    x*=f;
}
const int MAXN=105;
const double pi=atan(1)*4;

int n;
double x[MAXN],y[MAXN];
double ang[MAXN];
double solve(int cur)
{
//cerr<<cur<<":";
	enum(i,1,n)
	{
		if(i==cur){ang[i]=0;continue;}
		double x0=x[i]-x[cur],y0=y[i]-y[cur];
		if(fabs(x0)<1e-8)ang[i]=y0>0?pi/2:-pi/2;
		else ang[i]=atan(y0/x0)+(x0<0?pi:0);
		if(ang[i]<0)ang[i]+=2*pi;
//cerr<<ang[i]/pi*180<<" ";
	}
//cerr<<endl;
	sort(ang+1,ang+n+1);
	ang[1]=ang[n]-2*pi;
	double ans=0;
	enum(i,2,n)
		chkmax(ans,ang[i]-ang[i-1]);
	return ans<pi?0:(ans/pi-1)*0.5;
}

int main()
{
	readint(n);
	enum(i,1,n)scanf("%lf%lf",&x[i],&y[i]);
	enum(i,1,n)printf("%.10lf\n",solve(i));
    return 0;
}