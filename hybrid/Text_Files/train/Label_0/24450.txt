#include <bits/stdc++.h>
using namespace std;
#define int long long

const int N=2e5+2;
int par[N];

int find(int v){
	if(v==par[v])return v;
	return par[v]=find(par[v]);
}
bool join(int u,int v){
	u=find(u),v=find(v);
	if(rand()%2)swap(u,v);
	par[v]=u;
	return u!=v;
}
int32_t main(){
    ios::sync_with_stdio(0),cin.tie(0);
    iota(par,par+N,0);
    int n,m;
    cin >> n >> m;
    if(m<n*(n-1)/2-n+1){
    	set <int> g[n];
    	vector <pair <int,pair <int,int> > > ed;
    	for(int i=0;i<m;i++){
    		int u,v,w;
    		cin >> u >> v >> w;
    		--u,--v;
    		ed.push_back({w,{u,v}});
    		g[u].insert(v);
    		g[v].insert(u);
    	}
    	set <int> s;
    	for(int i=0;i<n;i++)
    		s.insert(i);
    	for(int i=0;i<n;i++){
    		s.erase(i);
    		queue <int> q;
    		q.push(i);
    		while(!q.empty()){
    			int v=q.front();
    			q.pop();
    			vector <int> ls;
    			for(auto u:s){
    				if(!g[v].count(u)){
    					join(v,u);
    					ls.push_back(u);
    					q.push(u);
    				}
    			}
    			for(auto u:ls)
    				s.erase(u);
    		}
    	}
    	int ans=0;
    	sort(ed.begin(),ed.end());
    	for(auto [w,pi]:ed){
    		auto [u,v]=pi;
    		if(join(u,v))ans+=w;
    	}
    	cout << ans ;
    }
    else{
    	int g[n][n],t=0;
    	memset(g,0,sizeof g);
    	for(int i=0;i<m;i++){
    		int u,v,w;
    		cin >> u >> v >> w;
    		--u,--v;
    		t^=w;
    		g[u][v]=g[v][u]=w;
    	}
    	vector <pair <int,pair <int,int> > > ed,xt;
    	for(int i=0;i<n;i++){
    		for(int j=0;j<i;j++){
    			ed.push_back({g[i][j],{i,j}});
    		}
    	}
    	int ans=0;
    	sort(ed.begin(),ed.end());
    	for(auto [w,pi]:ed){
    		auto [u,v]=pi;
    		if(join(u,v)){
    			ans+=w;
    			if(w)xt.push_back({w,{u,v}});
    		}
    	}
    	iota(par,par+N,0);
    	for(auto [w,pi]:xt){
    		auto [u,v]=pi;
    		join(u,v);
    	}
    	for(auto [w,pi]:ed){
    		if(!w)continue;
    		auto [u,v]=pi;
    		if(join(u,v)){
    			ans+=min(w,t);
    			break;
    		}
    	}
    	cout << ans ;
    }
}