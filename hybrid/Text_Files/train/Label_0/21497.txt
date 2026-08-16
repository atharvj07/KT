#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<bitset>

using namespace std;

typedef long long LL;

const int N=2e5,M=1e7;

int gi() {
	int w=0;bool q=1;char c=getchar();
	while ((c<'0'||c>'9') && c!='-') c=getchar();
	if (c=='-') q=0,c=getchar();
	while (c>='0'&&c <= '9') w=w*10+c-'0',c=getchar();
	return q? w:-w;
}

pair<int,int>p[N];
int s[N],nd[N],id[N],node;
int head[N],nxt[M],to[M],tot;
int dfn[N],low[N],st[N],rt[N],top,cnt,scc;bool in[N];

inline void link(int a,int b) { to[++tot]=b,nxt[tot]=head[a],head[a]=tot; }

inline void dfs(int k) {
	dfn[k]=low[k]=++cnt;
	in[st[++top]=k]=true;
	for (int i=head[k];i;i=nxt[i])
		if (!dfn[to[i]])
			dfs(to[i]),low[k]=min(low[k],low[to[i]]);
		else if (in[to[i]]) low[k]=min(low[k],dfn[to[i]]);
	if (low[k]==dfn[k]) {
		rt[k]=++scc;in[k]=false;
		while (st[top]!=k) rt[st[top]]=scc,in[st[top--]]=false;
		top--;
	}
}

#define lc (i<<1)
#define rc (lc|1)
inline void build(int i,int l,int r) {
	nd[i]=++node;
	if (l==r) id[s[p[l].second]^l]=node;
	else {
		int mid=(l+r)>>1;
		build(lc,l,mid);
		build(rc,mid+1,r);
	}
}
inline void init(int i,int l,int r) {
	if (l==r) return;
	int mid=(l+r)>>1;
	link(nd[i],nd[lc]);
	link(nd[i],nd[rc]);
	init(lc,l,mid);
	init(rc,mid+1,r);
}
inline void add(int i,int l,int r,int L,int R,int k) {
	if (L<=l&&r<=R) link(k,nd[i]);
	else {
		int mid=(l+r)>>1;
		if (L<=mid) add(lc,l,mid,L,R,k);
		if (mid<R) add(rc,mid+1,r,L,R,k);
	}
}
int main()
{
	int n=gi(),i,m=0,l,r,mid,L,R;
	for (i=1;i<=n;i++)
		p[++m]=make_pair(gi(),i),p[++m]=make_pair(gi(),i);
	sort(p+1,p+1+m);
	for (i=1;i<=m;i++) s[p[i].second]^=i;
	l=0,r=p[m].first-p[1].first;

	build(1,1,m);
	while (l!=r) {
		mid=(l+r+1)>>1;
		
		tot=cnt=scc=0;
		for (i=1;i<=node;i++) head[i]=dfn[i]=0;

		init(1,1,m);
		for (i=1,L=R=1;i<=m;i++) {
			while (p[i].first-p[L].first>=mid) L++;
			if (L<i) add(1,1,m,L,i-1,id[i]);
			while (R<m&&p[R+1].first-p[i].first<mid) R++;
			if (i<R) add(1,1,m,i+1,R,id[i]);
		}

		for (i=1;i<=node;i++) if (!dfn[i]) dfs(i);
		for (i=1;i<=m;i++) if (rt[id[i]]==rt[id[s[p[i].second]^i]]) break;
		
		if (i<=m) r=mid-1;
		else l=mid;
	}
	cout<<l<<endl;
	return 0;
}
