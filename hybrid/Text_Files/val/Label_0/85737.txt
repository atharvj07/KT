#include <bits/stdc++.h>
#pragma GCC optimize(3)
#define int long long
#define ri register
#define mk make_pair
#define fi first
#define se second
#define pb push_back
#define eb emplace_back
#define is insert
#define es erase
using namespace std; const int N=200010;
inline int read()
{
	int s=0, w=1; ri char ch=getchar();
	while(ch<'0'||ch>'9') { if(ch=='-') w=-1; ch=getchar(); }
	while(ch>='0'&&ch<='9') s=(s<<3)+(s<<1)+(ch^48), ch=getchar();
	return s*w;
}
int n,a[N],Ans;
vector<int> g[N];
signed main()
{
	n=read();
	for(ri int i=1;i<=n;i++) a[i]=read();
	for(ri int i=1;i<=n;i++) g[a[i]].eb(i);
	for(ri int i=1;i<=n;i++) g[a[i]].eb(n+1);
	g[0].eb(n+1);
	int p,q; p=q=0;
	for(ri int i=1;i<=n;i++)
	{
		if(a[i]!=p&&a[i]!=q)
		{
			Ans++;
			int np=*lower_bound(g[p].begin(),g[p].end(),i);
			int nq=*lower_bound(g[q].begin(),g[q].end(),i);
			if(np<nq) q=a[i];
			else p=a[i];
		}
		else
		{
			if(a[i]==p) p=a[i];
			else if(a[i]==q) q=a[i];
		}
	}
	printf("%lld\n",Ans);
	return 0;
}