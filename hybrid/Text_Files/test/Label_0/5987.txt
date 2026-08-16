#include<map>
#include<string>
#include<vector>
#include<iostream>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

typedef vector< vector<int> > vvi;

const int INF=1<<29;

void GabowDFS(int u,vector<bool> &visited,vector<int> &nodes,const vvi &adj){
	if(visited[u]) return;
	visited[u]=true;
	rep(i,adj[u].size()){
		int v=adj[u][i];
		if(!visited[v]) GabowDFS(v,visited,nodes,adj);
	}
	nodes.push_back(u);
}

vvi GabowSCC(const vvi &adj){
	int n=adj.size();
	vector<int> ord;
	vector<bool> visited(n);
	rep(u,n) GabowDFS(u,visited,ord,adj);

	vvi radj(n);
	rep(u,n) rep(i,adj[u].size()) radj[adj[u][i]].push_back(u);

	vvi sccs;
	rep(u,n) visited[u]=false;
	for(int i=n-1;i>=0;i--){
		int u=ord[i];
		vector<int> scc;
		GabowDFS(u,visited,scc,radj);
		if(scc.size()>0) sccs.push_back(scc);
	}
	return sccs;
}

int main(){
	for(int n;cin>>n,n;){
		int m=0;
		map<string,int> f;

		vvi adj(n);
		int day1[1000],day2[1000];
		rep(i,n){
			string s1,s2;
			int d1,d2; cin>>s1>>d1>>s2>>d2;
			if(f.count(s1)==0) f[s1]=m++;
			if(f.count(s2)==0) f[s2]=m++;

			int u=f[s2],v=f[s1];
			adj[u].push_back(v);
			day1[v]=d1;
			day2[v]=d2;
		}

		vvi scc=GabowSCC(adj);

		int ans=0;
		bool tool[1000]={};
		rep(i,scc.size()){
			int dif=INF;
			bool start=true;
			rep(j,scc[i].size()){
				int u=scc[i][j];
				ans+=day2[u];
				dif=min(dif,day1[u]-day2[u]);
				if(tool[u]) start=false;
			}
			if(start) ans+=dif;

			rep(j,scc[i].size()){
				int u=scc[i][j];
				rep(k,adj[u].size()) tool[adj[u][k]]=true;
			}
		}

		printf("%d\n",ans);
	}

	return 0;
}