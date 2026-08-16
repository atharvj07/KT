#include<cstdio>
#include<iostream>
#include<string>
#include<map>
#include<stack>
#include<vector>
#include<algorithm>

using namespace std;

const int inf=1e8;

template<class T> void chMax(T &a,T b){
	a=max(a,b);
}

map<string,int> elements;

int m,head[110],to[10100],nxt[10100];
int pre[110];
int comp[110];
int num_comp=0;
int c=0;
int N,M;

void init_edge();
void add_edge(int u,int v);

void init_edge(){
	for(int i=0;i<N;i++) head[i]=-1;
}

void add_edge(int u,int v){
	nxt[m]=head[u];to[m]=v;head[u]=m;m++;
	nxt[m]=head[v];to[m]=u;head[v]=m;m++;
}

void visit(int v,int p,stack<int> &roots,stack<int> &s){
	pre[v]=c++;
	s.push(v);
	roots.push(v);
	for(int e=head[v];e!=-1;e=nxt[e]){
		int u=to[e];
		if(u==p) continue;
		else if(pre[u]==-1){
			visit(u,v,roots,s);
		}else{
			while(pre[roots.top()]>pre[u]){
				roots.pop();
			}
		}
	}
	if(v==roots.top()){
		while(true){
			int w=s.top();
			s.pop();
			comp[w]=num_comp;
			if(w==v) break;
		}
		num_comp++;
		roots.pop();
	}
}

void bridge(){
	for(int i=0;i<N;i++) pre[i]=-1;
	stack<int> roots,s;
	for(int v=0;v<N;v++){
		if(pre[v]==-1){
			visit(v,-1,roots,s);
		}
	}
}

vector<int> G[110];
int weight[110];
int par[110];
int dp[2][110][110];
int res[110][110][110];
int sz[110];
int V;

void get_tree(){
	for(int v=0;v<N;v++){
		for(int e=head[v];e!=-1;e=nxt[e]){
			int u=to[e];
			int nv=comp[v],nu=comp[u];
			if(nv==nu) continue;
			G[nv].push_back(nu);
		}
	}
	V=num_comp;
	for(int i=0;i<N;i++) weight[i]=0;
	for(int v=0;v<N;v++){
		weight[comp[v]]++;
	}
}

void solve(int v,int p){
	sz[v]=weight[v];
	for(int i=0;i<G[v].size();i++){
		int u=G[v][i];
		if(u==p) continue;
		solve(u,v);
		sz[v]+=sz[u];
	}
	for(int i=0;i<=sz[v];i++) for(int j=0;j<=sz[v];j++){
		res[v][i][j]=-inf;
	}
	if(sz[v]==weight[v]){
		res[v][sz[v]][sz[v]]=0;
		return;
	}
	for(int i=0;i<=sz[v];i++) for(int j=0;j<=sz[v];j++){
		for(int t=0;t<2;t++) dp[t][i][j]=-inf;
	}
	dp[0][0][0]=0;
	int t=0;
//	int ad=0;
	for(int id=0;id<G[v].size();id++){
		int u=G[v][id];
		if(u==p) continue;
//		ad+=weight[v]*weight[u];
		for(int i=0;i<=sz[v];i++) for(int j=0;j<=sz[v];j++){
			dp[t^1][i][j]=-inf;
		}
		for(int i=0;i<=sz[v]-weight[v]-sz[u];i++) for(int j=0;j<=sz[v]-weight[v]-sz[u];j++){
			for(int k=0;k<=sz[u];k++) for(int l=0;l<=sz[u];l++){
				if(res[u][k][l]<0) continue;
				chMax(dp[t^1][i+k][j],dp[t][i][j]+res[u][k][l]+k*j+k*weight[v]);
				chMax(dp[t^1][i][j+l],dp[t][i][j]+res[u][k][l]+i*l+l*weight[v]);
			}
		}
		t^=1;
	}
	for(int i=0;i<=sz[v];i++) for(int j=0;j<=sz[v];j++){
		res[v][i][j]=-inf;
	}
	for(int i=0;i<=sz[v]-weight[v];i++) for(int j=0;j<=sz[v]-weight[v];j++){
		if(dp[t][i][j]>=0) res[v][i+weight[v]][j+weight[v]]=dp[t][i][j];
	}
}

int main(){
	cin>>N>>M;
	for(int i=0;i<N;i++){
		string str;
		cin>>str;
		elements[str]=i;
	}
	init_edge();
	for(int i=0;i<M;i++){
		string str1,str2;
		cin>>str1>>str2;
		int u=elements[str1];
		int v=elements[str2];
		add_edge(u,v);
	}
	bridge();
	get_tree();
/*	for(int i=0;i<V;i++){
		printf("weight[%d]=%d\n",i,weight[i]);
	}*/
/*	for(int i=0;i<V;i++){
		printf("%d- ",i);
		for(int j=0;j<G[i].size();j++){
			printf("%d ",G[i][j]);
		}
		printf("\n");
	}*/
	solve(0,-1);
	int ans=0;
	for(int i=0;i<V;i++){
		ans+=weight[i]*weight[i];
	}
	int Ma=-1;
	for(int i=0;i<=N;i++) for(int j=0;j<=N;j++){
		chMax(Ma,res[0][i][j]);
	}
	printf("%d\n",ans+Ma);
	return 0;
}