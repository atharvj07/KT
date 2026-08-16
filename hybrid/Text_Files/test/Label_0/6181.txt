#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int n;
	int u,v;
	ll ans=0;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		ans+=1ll*i*(n-i+1);//统计有多少个独立的 
	}
	for(int i=1;i<=n-1;i++)
	{
		scanf("%d%d",&u,&v);
		if(u>v) swap(u,v);
		ans-=1ll*u*(n-v+1);
	}
	printf("%lld",ans);
 } 