#include<cstdio>
#include<algorithm>
using namespace std;
int n,cnt,mp[300005],del[300005],siz[300005];
long long ans[300005];
int main()
{
	scanf("%d",&n);
	for(int i=1,a;i<=n;i++)
	{
		scanf("%d",&a);
		if(!mp[a])mp[a]=++cnt;
		siz[mp[a]]++;
	}
	sort(siz+1,siz+1+cnt);
	for(int i=1;i<=cnt;i++)del[1]++,del[siz[i]+1]--;
	for(int i=1,nw=0;i<=n;i++)nw+=del[i],ans[i]=ans[i-1]+nw;
	for(int k=1;k<=n;k++)
	{
		int l=0,r=n,mid,ans1;
		while(l<=r)
		{
			mid=(l+r)/2;
			if(ans[mid]>=1ll*mid*k)ans1=mid,l=mid+1;
			else r=mid-1;
		}
		printf("%d\n",ans1);
	}
}