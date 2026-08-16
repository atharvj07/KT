#include<bits/stdc++.h>
using namespace std;
const int N=2e5+9;
struct graph{
	struct edge{int to,next,f;}e[N<<1];
	int h[N],cur[N],xb;
	inline void addedge(int x,int y,int z){
		e[++xb]=(edge){y,h[x],z};h[x]=xb;
		e[++xb]=(edge){x,h[y],0};h[y]=xb;
	}
	int S,T,d[N],n;
	inline bool bfs(){
		static int q[N];int t=0,w=1;q[1]=S;
		memset(d+1,0,n<<2);d[S]=1;
		for(;t<w;){
			int u=q[++t];
			for(int i=h[u];i;i=e[i].next)if(e[i].f && !d[e[i].to])
				d[e[i].to]=d[u]+1,q[++w]=e[i].to;
		}
		return d[T];
	}
	int dfs(int x,int f){
		if(x==T)return f;
		int ans=0,&i=cur[x],t;
		for(;i;i=e[i].next)if(e[i].f && d[e[i].to]==d[x]+1){
			if(t=dfs(e[i].to,min(f,e[i].f))){
				ans+=t,e[i].f-=t;e[i^1].f+=t;f-=t;
				if(!f)break;
			}
		}
		return ans;
	}
	inline int dinic(int s,int t){
		int ans=0;S=s;T=t;
		for(;bfs();ans+=dfs(s,1<<30))memcpy(cur+1,h+1,n<<2);
		return ans;
	}
}g;
int n,m,i,j,p[N],q[N],belp[N],belq[N],pc,qc,sm;
inline void work(int*p,int*bel,int&c){
	static bool vi[N];memset(vi+1,0,n);
	for(i=1;i<=n;++i)cin>>p[i],++p[i];
	for(i=1;i<=n;++i)if(!vi[i])for(j=i,++c;bel[j]=c,vi[j]=1,!vi[p[j]];j=p[j]);
}
int main(){
	ios::sync_with_stdio(0);cin.tie(0);
	cin>>n;work(p,belp,pc);work(q,belq,qc);g.n=pc+qc+2;g.xb=1;
	for(i=1;i<=n;++i){
		if(p[i]==i && q[i]==i)++sm;
		if(p[i]==i && q[i]!=i)g.addedge(g.n-1,pc+belq[i],1);
		if(p[i]!=i && q[i]==i)g.addedge(belp[i],g.n,1);
		if(p[i]!=i && q[i]!=i){
			g.addedge(belp[i],pc+belq[i],1);
			if(p[i]==q[i])
				g.addedge(pc+belq[i],belp[i],1);
		}		
	}
	cout<<n-g.dinic(g.n-1,g.n)-sm<<endl;
	return 0;
}