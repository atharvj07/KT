#include <bits/stdc++.h>

using namespace std;
#define X first
#define Y second
#define pb push_back
typedef double db;
typedef long long ll;
typedef pair<int,int> P;
const int MAXN=1e5+10;
struct edge{int nxt,to;}e[MAXN<<2];
ll res=0;
int lca,dep[MAXN],sum[MAXN],f[MAXN];
int n,m,fx,fy,head[MAXN],x,y,tot,TOT,cnt,t[MAXN];

void add_edge(int x,int y)
{
	e[++TOT]=(edge){head[x],y};head[x]=TOT;
	e[++TOT]=(edge){head[y],x};head[y]=TOT;
}
void dfs(int x,int anc,int val)
{
	sum[x]=val;tot+=val;
	dep[x]=dep[anc]+1;f[x]=anc;
	for(int i=head[x];i;i=e[i].nxt)
		if(e[i].to!=anc)
		{
			if(dep[e[i].to]) 
			{fx=x;fy=e[i].to;continue;}
			dfs(e[i].to,x,-val),sum[x]+=sum[e[i].to];	
		}
}
int LCA(int x,int y)
{
	if(dep[x]<dep[y]) swap(x,y);
	int t=dep[x]-dep[y];
	for(int i=1;i<=t;i++) x=f[x];
	while(x!=y) x=f[x],y=f[y];
	return x;
}

int main()
{
	scanf("%d%d",&n,&m);
	for(int i=1;i<=m;i++)
		scanf("%d%d",&x,&y),add_edge(x,y);
	dfs(1,0,1);
	
	if(m==n-1)
	{
		if(tot) return puts("-1"),0;
		for(int i=1;i<=n;i++) res+=abs(sum[i]);
	}
	else if((dep[fx]-dep[fy])%2==0)
	{
		if(tot%2) return puts("-1"),0;
		lca=LCA(fx,fy);tot=-tot/2;res+=abs(tot);
		
		for(int k=fx;k;k=f[k]) sum[k]+=tot;
		for(int k=fy;k;k=f[k]) sum[k]+=tot;
		for(int i=1;i<=n;i++) res+=abs(sum[i]);
	}
	else
	{
		if(tot) return puts("-1"),0;
		lca=LCA(fx,fy);
		for(int k=fx;k!=lca;k=f[k]) 
			t[++cnt]=sum[k],dep[k]=-1;
		for(int k=fy;k!=lca;k=f[k])
			t[++cnt]=-sum[k],dep[k]=-1;
		t[++cnt]=0;
		sort(t+1,t+cnt+1);int val=t[cnt/2];
		
		for(int i=1;i<=n;i++)
			if(~dep[i]) res+=abs(sum[i]);
		for(int i=1;i<=cnt;i++)
			res+=abs(t[i]-val);
	}
	printf("%d",res);
	return 0;
}