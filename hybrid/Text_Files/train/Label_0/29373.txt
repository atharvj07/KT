#include <bits/stdc++.h>
using namespace std;

int fa[100001];

struct edge
{
	int u;
	int v;
}e[100001];

long long ans[100001],len[100001];

int findfa(int x)
{
	if(x!=fa[x]) fa[x]=findfa(fa[x]);
	return fa[x];
}

int main()
{
	int n,m;
	cin>>n>>m;
	
	for(int i=1;i<=m;i++)
		cin>>e[i].u>>e[i].v;
	
	for(int i=1;i<=n;i++)
	{
		fa[i]=i;
		len[i]=1;
	}
	
	ans[m]=(long long)n*(n-1)/2;
	
	int f1,f2;
	for(int i=m;i>=1;i--)
	{
		f1=findfa(e[i].u);
		f2=findfa(e[i].v);
		if(f1==f2)
			ans[i-1]=ans[i];
		else
		{
			ans[i-1]=ans[i]-len[f2]*len[f1];
			len[f2]+=len[f1];
			fa[f1]=f2;
		}
	}
	
	for(int i=1;i<=m;i++)
		cout<<ans[i]<<endl;
	return 0;
}