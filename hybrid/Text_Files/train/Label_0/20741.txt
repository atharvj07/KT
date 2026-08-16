#include<bits/stdc++.h>
#define N 200005
using namespace std;
int n,m,a[N],b[N];
int check(int x)
{
	for (int i=1;i<=m;i++)
		b[i]=a[i]>=x;
	if (b[n]==b[n-1]||b[n]==b[n+1]) return b[n];
	int l=n,r=n;
	while(l>1&&b[l-1]!=b[l])l--;
	while(r<m&&b[r+1]!=b[r])r++;
	if (l==1&&r==n) return b[1];
	if ((r^l)&1) return (l+r>>1)>=n?b[l]:b[r];
	return (l+r>>1)>=n?b[l]:b[r];
}
int main()
{
	scanf("%d",&n);
	m=n*2-1;
	for (int i=1;i<=m;i++)
		scanf("%d",&a[i]);
	int l=1,r=m,mid,ans;
	while(l<=r)
	{
		mid=l+r>>1;
		if (check(mid)) l=mid+1,ans=mid;
		else r=mid-1;
	}
	printf("%d\n",ans);
}