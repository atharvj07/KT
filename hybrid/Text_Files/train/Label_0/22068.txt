#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<assert.h>
#include<set>
#include<cmath>
#include<queue>
#include<cstdlib>
#include<iostream>
#include<bitset>
#define pii pair<int,int>
#define fi first
#define se second
#define pb push_back
#define rep(i,j,k) for(int i=(int)(j);i<=(int)(k);i++)
#define per(i,j,k) for(int i=(int)(j);i>=(int)(k);i--)
using namespace std;
typedef long long LL;
typedef double db;
const int inf=1e9;
namespace h{
	const int N=43*43*4;
	int head[N],np[N*20],p[N*20],flow[N*20],tot;
	int S,T;
	void init(int n){
		S=n+1;
		T=n+2;
		rep(i,1,T)head[i]=0;
		rep(i,1,tot){
			p[i]=np[i]=flow[i]=0;
		}
		tot=1;
	}
	void add(int a ,int b,int c){
		++tot;p[tot]=b;np[tot]=head[a];head[a]=tot;flow[tot]=c;
		++tot;p[tot]=a;np[tot]=head[b];head[b]=tot;flow[tot]=0;
	}
	void ax(int x,int a){
		//贡献 ax
		add(S,x,a);
	}
	void a1_x(int x,int a){
		//贡献 a(1-x)
		add(x,T,a);
	}
	void cx1_y(int x,int y,int c){
		//贡献 cx(1-y)
		add(y,x,c);
	}
	int q[N],dis[N];
	int bfs(){
		rep(i,1,T)dis[i]=-1;
		q[q[0]=1]=S;
		dis[S]=0;
		rep(i,1,q[0]){
			int x=q[i];
			for(int u=head[x];u;u=np[u])if(dis[p[u]]==-1)if(flow[u]){
				dis[p[u]]=dis[x]+1;
				q[++q[0]]=p[u];
			}
		}
		return dis[T];
	}
	int dinic(int x,int ff){
		int res=0;
		if(x==T)return ff;
		for(int u=head[x];u;u=np[u])if(dis[p[u]]==dis[x]+1)if(flow[u]){
			int ret=dinic(p[u],min(ff,flow[u]));
			flow[u]-=ret;
			flow[u^1]+=ret;
			ff-=ret;
			res+=ret;
			if(!ff)break;
		}
		if(!res)dis[x]=-1;
		return res;
	}
	int calc(){
		int ans=0;
		while(bfs()!=-1)ans+=dinic(S,1e9);
		return ans;
	}
};
const int N=45;
int n,m,ca,cb,cc;
char s[N][N];
int bh[N][N],_wh[N][N],_bv[N][N],wv[N][N];
int t;
void Main(){
	scanf("%d%d%d%d%d",&n,&m,&ca,&cb,&cc);
	rep(i,1,n)scanf("%s",s[i]+1);
	t=0;
	rep(i,1,n)rep(j,1,m){
		bh[i][j]=++t;
		wv[i][j]=++t;
		_wh[i][j]=++t;
		_bv[i][j]=++t;
	}
	h::init(t);
	//cost of paint h or v
	rep(i,1,n)rep(j,1,m){
		h::ax(bh[i][j],ca);
		h::ax(wv[i][j],ca);
		h::a1_x(_wh[i][j],ca);
		h::a1_x(_bv[i][j],ca);

		if(j+1<=m){
			h::cx1_y(bh[i][j],bh[i][j+1],cb);
			h::cx1_y(_wh[i][j+1],_wh[i][j],cb);
		}
		else{
			h::ax(bh[i][j],cb);
			h::a1_x(_wh[i][j],cb);
		}

		if(i+1<=n){
			h::cx1_y(wv[i][j],wv[i+1][j],cb);
			h::cx1_y(_bv[i+1][j],_bv[i][j],cb);
		}
		else{
			h::ax(wv[i][j],cb);
			h::a1_x(_bv[i][j],cb);
		}
	}
	//cost of paint single dot
	rep(i,1,n)rep(j,1,m){
		if(s[i][j]=='#'){
			//black
			
			//前面不能往这里涂白，只要涂白就是inf
			h::ax(wv[i][j],inf);
			h::a1_x(_wh[i][j],inf);
			//如果没被涂过，就要 c 的代价
			h::cx1_y(_bv[i][j],bh[i][j],cc);
		}
		else{
			//white

			//涂了黑且没涂白就要 c 的代价，因为同一个格子不可能被hh,vv，所以只有两种情况
			h::cx1_y(bh[i][j],wv[i][j],cc);
			h::cx1_y(_wh[i][j],_bv[i][j],cc);
			//涂了两次黑，就是inf
			h::cx1_y(bh[i][j],_bv[i][j],inf);
		}
	}
	printf("%d\n",h::calc());
}
int main(){
	int t=1;
	while(t--)Main();
	return 0;
}






