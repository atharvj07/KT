#include  <bits/stdc++.h>
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)
using namespace std;

const int nmax=100010;

vector<int> graph[nmax];
int parent[nmax][20]; // all is -1
int depth[nmax];

void dfs(int v,int p,int d){
	parent[v][0]=p;
	depth[v]=d;
	for(auto &v2:graph[v]) if(v2!=p) dfs(v2,v,d+1);
}

int lca(int u,int v){
	if(depth[u] < depth[v]) swap(u,v);
	for(int i=19;i>=0;--i) if((depth[u]-depth[v])>>i&1) u=parent[u][i];
	if(u==v) return u;
	for(int i=19;i>=0;--i){
		if(parent[u][i]!=parent[v][i]){
			u=parent[u][i];
			v=parent[v][i];
		}
	}
	return parent[u][0];
}

int main(void){
	int n; cin >> n;
	rep(i,n){
		int k; cin >> k;
		rep(j,k){
			int v; cin >> v;
			graph[i].push_back(v);
		}
	}

	// rep(i,n)rep(j,20) parent[i][j]=-1;
	dfs(0,-1,0);
	rep(j,19)rep(i,n){
		if(parent[i][j]==-1)
			parent[i][j+1]=-1;
		else
			parent[i][j+1]=parent[parent[i][j]][j];
	}

	int q; cin >> q;
	rep(i,q){
		int u,v; cin >> u >> v;
		cout << lca(u,v) << endl;
	}
	return 0;
}