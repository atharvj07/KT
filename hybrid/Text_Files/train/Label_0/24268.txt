#include <bits/stdc++.h>
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;
typedef pair<int,int>P;

vector<int>E[100000];
int s[100000],t[100000];
int ord[100000],low[100000],k;
bool used[100000];
vector<P>V;

void dfs(int v,int p){
	used[v]=true;
	low[v]=ord[v]=k++;
	for(auto u:E[v]){
		if(!used[u]){
			dfs(u,v);
			low[v]=min(low[v],low[u]);
			if(ord[v]<low[u])V.push_back(P(min(u,v),max(u,v)));
		}
		else if(p!=u){
			low[v]=min(low[v],ord[u]);
		}
	}
}
int main(){
	int v,e;scanf("%d%d",&v,&e);
	rep(i,e){
		scanf("%d%d",&s[i],&t[i]);
		E[s[i]].push_back(t[i]);
		E[t[i]].push_back(s[i]);
	}
	dfs(0,-1);
	sort(V.begin(),V.end());
	for(auto p:V){
		cout<<p.first<<' '<<p.second<<endl;
	}
}