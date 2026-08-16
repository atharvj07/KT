#include <bits/stdc++.h>
using namespace std;
const int MAXN=3e2+7;
const int inf=1e9+7;
struct po {
	int from,to,w,nxt;
} edge[MAXN*MAXN*15];
int head[MAXN*MAXN+MAXN*6],num=-1,n,m,s,t,b[MAXN],dep[MAXN*MAXN+MAXN*6],cur[MAXN*MAXN+MAXN*6];
int U[MAXN],L[MAXN],R[MAXN],D[MAXN],id[MAXN][MAXN],I;
int us[MAXN][MAXN],vis[MAXN][MAXN];
char a[MAXN][MAXN];
inline void add_edge(int from,int to,int w) {
	edge[++num].nxt=head[from];
	edge[num].to=to;
	edge[num].w=w;
	head[from]=num;
}
inline void add(int from,int to,int w) {
	add_edge(from,to,w);
	add_edge(to,from,0);
}
inline bool bfs() {
	queue<int> q;
	memset(dep,0,sizeof(dep));
	while(!q.empty()) q.pop();
	q.push(s);
	dep[s]=1;
	while(!q.empty()) {
		int u=q.front();
		q.pop();
		for(int i=head[u]; i!=-1; i=edge[i].nxt) {
			int v=edge[i].to;
			if(edge[i].w&&!dep[v]) {
				q.push(v);
				dep[v]=dep[u]+1;
				if(v==t) return 1;
			}
		}
	}
	return 0;
}
inline int dfs(int u,int low) {
	if(u==t) return low;
	int diss=0;
	for(int &i=cur[u]; i!=-1; i=edge[i].nxt) {
		int v=edge[i].to;
		if(edge[i].w&&dep[v]==dep[u]+1) {
			int check=dfs(v,min(edge[i].w,low));
			if(check) {
				low-=check;
				diss+=check;
				edge[i].w-=check;
				edge[i^1].w+=check;
				if(low==0) break;
			}
		}
	}
	return diss;
}
inline int dinic() {
	int ans=0;
	while(bfs()) {
		for(int i=0; i<=t; i++) cur[i]=head[i];
		while(int d=dfs(s,inf)) ans+=d;
	}
	return ans;
}
int dfs1(int x,int y) {
	if(us[x][y]) {
		us[x][y]=0;
		return 1;
	}
	us[x][y]=1;
	if(a[x][y]=='L') {
		for(int i=1; i<y; i++) {
			if(!vis[x][i]&&dfs1(x,i)) {
				a[x][i]='L';
				if(us[x][y]) {
					us[x][y]=0;
					return 1;
				} else return dfs1(x,y);
			}
		}
	} else if(a[x][y]=='R') {
		for(int i=y+1; i<=n; i++) {
			if(!vis[x][i]&&dfs1(x,i)) {
				a[x][i]='R';
				if(us[x][y]) {
					us[x][y]=0;
					return 1;
				}else return dfs1(x,y);
			}
		}
	} else if(a[x][y]=='U') {
		for(int i=1; i<x; i++) {
			if(!vis[i][y]&&dfs1(i,y)) {
				a[i][y]='U';
				if(us[x][y]) {
					us[x][y]=0;
					return 1;
				}else return dfs1(x,y);
			}
		}
	} else {
		for(int i=x+1; i<=n; i++) {
			if(!vis[i][y]&&dfs1(i,y)) {
				a[i][y]='D';
				if(us[x][y]) {
					us[x][y]=0;
					return 1;
				}else return dfs1(x,y);
			}
		}
	}
	vis[x][y]=1;
	cout<<a[x][y];
	if(a[x][y]=='L'||a[x][y]=='R') cout<<x<<endl;
	else cout<<y<<endl;
	return 0;
}
int main() {
	memset(head,-1,sizeof(head));
	cin>>n;
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++) id[i][j]=++I;
	for(int i=1; i<=n; i++) cin>>U[i];
	for(int i=1; i<=n; i++) cin>>D[i];
	for(int i=1; i<=n; i++) cin>>L[i];
	for(int i=1; i<=n; i++) cin>>R[i];
	s=0,t=n*n+n+n+n+n+1;
	for(int i=1; i<=n; i++) {
		add(s,n*n+i,U[i]);
		add(s,n*n+n+i,D[i]);
		add(s,n*n+n+n+i,L[i]);
		add(s,n*n+n+n+n+i,R[i]);
		for(int j=1; j<=n; j++) add(n*n+i,id[j][i],1),add(n*n+n+i,id[j][i],1);
		for(int j=1; j<=n; j++) add(n*n+n+n+i,id[i][j],1),add(n*n+n+n+n+i,id[i][j],1);
	}
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++) add(id[i][j],t,1);
	int d=dinic();
	if(d<n*n) {
		cout<<"NO"<<endl;
		return 0;
	}
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++) {
			int u=id[i][j];
			for(int k=head[u]; k!=-1; k=edge[k].nxt) {
				int v=edge[k].to;
				if(v==t||edge[k].w==0) continue;
				v=v-n*n-1;
				if(v/n==0) a[i][j]='U';
				if(v/n==1) a[i][j]='D';
				if(v/n==2) a[i][j]='L';
				if(v/n==3) a[i][j]='R';
				break;
			}
		}
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++) {
			if(!vis[i][j]) dfs1(i,j);
		}
}