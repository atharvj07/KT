#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

namespace Dinic {
	const int mxn=5000, mxm=500000;
	int S, T;
	int head[mxn];
	int next[mxm], to[mxm], flow[mxm];
	inline void addedge(int idx, int a, int b, int f)
	{
		next[idx]=head[a]; head[a]=idx;
		to[idx]=b; flow[idx]=f;
	}
	int newm;
	inline void add(int a, int b, int f)
	{
		addedge((++newm)<<1, a, b, f);
		addedge(newm<<1|1, b, a, 0);
	}
	inline void init()
	{
		memset(head, 0, sizeof(head));
		newm=0;
	}
	int ch[mxn];
	inline bool tell()
	{
		memset(ch, -1, sizeof(ch));
		ch[S]=1;
		queue<int> q;
		q.push(S);
		while(!q.empty())
		{
			int u=q.front(); q.pop();
			for(int i=head[u]; i; i=next[i])
			{
				const int v=to[i];
			//printf("->%d %d %d\n", v, ch[v], flow[i]);
				if(ch[v]>0 || !flow[i]) continue;
				ch[v]=ch[u]+1;
				q.push(v);
			}
		}
		return ch[T]>0;
	}
	int expand(int a, int b)
	{
		//printf("expanding %d, %d\n", a, b);
		if(a==T) return b;
		int r=0, c;
		for(int i=head[a]; i && r<b; i=next[i])
		{
			int v=to[i];
			if(ch[v]!=ch[a]+1 || !flow[i]) continue;
			c=expand(v, min(b-r, flow[i]));
			r+=c;
			flow[i]-=c, flow[i^1]+=c;
		}
		return r;
	}
	inline int dinic(int sS, int tT)
	{
		S=sS, T=tT;
		int r=0, c;
		while(tell()) while(c=expand(S, 0x3f3f3f3f)) r+=c;
		return r;
	}
}

const int maxn=100+5;
int mx[maxn][maxn];


int main()
{
	int n, m, l; 
	while(scanf("%d%d%d", &n, &m, &l)==3)
	{
		memset(mx, 0x3f, sizeof(mx));
		for(int i=1; i<=n; ++i) mx[i][i]=0;
		for(int i=1; i<=m; ++i)
		{
			int x, y, l; scanf("%d%d%d", &x, &y, &l);
			mx[y][x]=mx[x][y]=min(mx[x][y], l);
		}
		for(int k=1; k<=n; ++k) for(int i=1; i<=n; ++i)
			for(int j=1; j<=n; ++j) mx[i][j]=min(mx[i][j], mx[i][k]+mx[k][j]);
		Dinic::init();
		for(int i=1; i<=n; ++i)
		{
			int x; scanf("%d", &x);
			Dinic::add(1, i+5, x);
		}
		for(int i=1; i<=n; ++i)
		{
			int x; scanf("%d", &x);
			Dinic::add(i+n+10, 2, x);
		}
		for(int i=1; i<=n; ++i) for(int j=1; j<=n; ++j)
		{
			if(mx[i][j]<l) 
			{
				Dinic::add(i+5, j+n+10, 0x3f3f3f3f);
				//printf("adding..%d %d\n", i, j);
			}
		}
		printf("%d\n", Dinic::dinic(1, 2));
	}
	
	return 0;
}