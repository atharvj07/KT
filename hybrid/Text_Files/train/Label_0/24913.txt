#include<cstdio>
#include<algorithm>
using namespace std;
#define MAXN 100010
#define LL long long
int n,L,T,a[MAXN],x,op;
LL c;
int main()
{
	scanf("%d%d%d",&n,&L,&T);
	for(int i=1;i<=n;i++)
	{
		scanf("%d%d",&x,&op);
		if(op==1)
		{
			int p=x+T;
			if(p>0) (c+=p/L)%=n;
			a[i]=p%L;
		}
		else
		{
			int p=x-T;
			if(p<0) (c+=(p+1)/L-1)%=n;
			a[i]=(p%L+L)%L;
		}
	}
	sort(a+1,a+1+n);
	c=(c%n+n)%n;
	for(int i=c+1;i<=n;i++) printf("%d\n",a[i]);
	for(int i=1;i<=c;i++) printf("%d\n",a[i]);
}