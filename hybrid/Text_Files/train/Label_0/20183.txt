//Love and Freedom.
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#define ll long long
#define inf 20021225
#define N 100100
using namespace std;
int read()
{
	int s=0,f=1; char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-') f=-1; ch=getchar();}
	while(ch>='0'&&ch<='9') s=s*10+ch-'0',ch=getchar();
	return f*s;
}
ll f[N],mn; int t,e,n,p[N];
int main()
{
	n=read(),e=read(),t=read();
	int l=0; mn=1e18;
	for(int i=1;i<=n;i++)	p[i]=read();
	for(int i=1;i<=n;i++)
	{
		while(l<=i && 2*(p[i]-p[l+1])>t)
			mn=min(mn,f[l]-2*p[l+1]), l++;
		if(l<i)	f[i]=f[l]+t;
		f[i]=min(f[i],mn+2*p[i]);
	}
	printf("%lld\n",f[n]+e);
	return 0;
}