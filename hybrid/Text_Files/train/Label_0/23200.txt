#include<bits/stdc++.h>
using namespace std;

int a[200010],b[200010],n,val[200010],l,r,mid,ans,fp,nwp;
long long nw,sum[200010],nww,fa,fb,nwa,nwb;

long long gcd(long long a,long long b) {return (!b)?a:gcd(b,a%b);}

int main()
{
	scanf("%d",&n);
	for (int i=1; i<=n; i++) scanf("%d%d",&a[i],&b[i]),val[i]=max(a[i],b[i]),nw+=min(a[i]-b[i],0);
	sort(val+1,val+1+n),sum[0]=0,fp=0,fa=0,fb=1;
	for (int i=1; i<=n; i++) sum[i]=sum[i-1]+val[i];
	for (int i=1; i<=n; i++)
	{
		l=1,r=n,ans=0,nww=(a[i]<b[i]?nw:nw+a[i]-b[i]);
		while (l<=r)
		{
			mid=(l+r)>>1;
			if (sum[mid]-(max(a[i],b[i])<=val[mid]?max(a[i],b[i]):0)+nww<=0) ans=mid,l=mid+1; else r=mid-1;
		}
		nww=nww-(a[i]-b[i])+sum[ans]-(max(a[i],b[i])<=val[ans]?max(a[i],b[i]):0);
		nwp=ans-(max(a[i],b[i])<=val[ans]);
		nwa=b[i]-(a[i]+nww),nwb=b[i];
		if (nwp>fp||nwp==fp&&nwa*fb>nwb*fa) fp=nwp,fa=nwa,fb=nwb;
	}
	fa+=fp*fb,fb*=n;
	long long g=gcd(fa,fb);
	printf("%lld %lld\n",fa/g,fb/g);
	return 0;
}