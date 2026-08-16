#include <iostream>
#include <fstream>
#include <cassert>
#include <typeinfo>
#include <vector>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <iomanip>
#include <cctype>
#include <random>
#include <complex>
#define syosu(x) fixed<<setprecision(x)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;
typedef pair<double,double> pdd;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<P> vp;
typedef vector<vp> vvp;
typedef vector<pll> vpll;
typedef pair<int,P> pip;
typedef vector<pip> vip;
const int inf=1<<29;
const ll INF=1ll<<58;
const double pi=acos(-1);
const double eps=1e-7;
const ll mod=1e9+7;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};

struct edge{
	int to,cap,rev;
};

int n,m;
vector<vector<edge> > g;

void add_edge(int u,int v){
	g[u].push_back({v,1,(int)g[v].size()});
	g[v].push_back({u,1,(int)g[u].size()-1});
}

int dfs(int v,vi& used){
	used[v]=1;
	for(int i=0;i<g[v].size();i++){
		edge &e=g[v][i];
		if(e.cap==1||e.cap==2&&!used[e.to]&&dfs(e.to,used)){
			e.cap=0;
			g[e.to][e.rev].cap=2;
			return 1;
		}
	}
	return 0;
}

int main(){
	while(1){
		cin>>n>>m;
		if(!n) break;
		g=vector<vector<edge> >(n);
		for(int i=0;i<m;i++){
			int u,v;
			cin>>u>>v;
			u--;v--;
			add_edge(u,v);
		}
		vi a(n);
		for(int i=0;i<n;i++) for(int j=0;j<n;j++){
			vi used(n);
			a[j]+=dfs(j,used);
		}
		int mn=inf,mx=0;
		for(int i=0;i<n;i++){
			mn=min(mn,a[i]);
			mx=max(mx,a[i]);
		}
		cout<<mn<<' '<<mx<<endl;
	}
}