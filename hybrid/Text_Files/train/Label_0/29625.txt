#include <bits/stdc++.h>
using namespace std;
#define N 200005
int n,m,ans,a[N],s[N];
int max(int x,int y) {return x>y?x:y;}
int main()
{
	scanf("%d %d",&n,&m);
	for(int i=1;i<=n;++i) scanf("%d",&a[i]),s[i]=s[i-1]+a[i];
	for(int i=m;i<=n;++i) ans=max(ans,s[i]-s[i-m]);
	ans+=m;printf("%d",ans>>1);if(ans&1) puts(".5");
	return 0;
}