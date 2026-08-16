#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cassert>
using namespace std;

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define fr(i,c) for(__typeof(c.begin()) i=c.begin();i!=c.end();i++)
#define pb push_back
#define mp make_pair
#define all(c) c.begin(),c.end()
#define dbg(x) cerr<<#x<<" = "<<(x)<<endl

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef long long ll;
const int inf=(int)1e9;
const double EPS=1e-9, INF=1e12;

typedef int Weight;
struct Edge {
  int src, dst;
  Weight weight;
  Edge(int src, int dst, Weight weight) :
    src(src), dst(dst), weight(weight) { }
};
bool operator < (const Edge &e, const Edge &f) {
  return e.weight != f.weight ? e.weight > f.weight : // !!INVERSE!!
    e.src != f.src ? e.src < f.src : e.dst < f.dst;
}
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;
typedef vector<Weight> Array;
typedef vector<Array> Matrix;

vi k_shortestPath(const Graph &g, int s, int t, int k,int *h) {
  int n=g.size();
  vi dist[n];
  priority_queue<Edge> Q; Q.push(Edge(-1, s, 0));
  while (!Q.empty()) {
    Edge e = Q.top(); Q.pop();
    if (dist[e.dst].size() >= k) continue;
    dist[e.dst].push_back(e.weight);
    fr(f, g[e.dst]) Q.push(Edge(f->src, f->dst, f->weight+e.weight+h[f->src]-h[f->dst]));
  }
  rep(i,dist[t].size())dist[t][i]+=h[t]-h[s];
  return dist[t];
}
int *buildFail(char *p) {
  int m = strlen(p);
  int *fail = new int[m+1];
  int j = fail[0] = -1;
  for (int i = 1; i <= m; ++i) {
    while (j >= 0 && p[j] != p[i-1]) j = fail[j];
    fail[i] = ++j;
  }
  return fail;
}

int n,col[100],m,a[1000],b[1000],c[1000],k;
char ptn[20];
int V,s,t,h[1111];
Graph G,rG;

bool v[1111],rv[1111];
void dfs(int c,const Graph &g,bool *v){
	v[c]=1;
	fr(i,g[c])if(!v[i->dst])dfs(i->dst,g,v);
}
bool calc_potential(){
	fill(h,h+V+1,0);
	rep(k,V)rep(i,V)if(v[i]&&rv[i])fr(e,G[i]){
		if(h[e->dst]>h[e->src]+e->weight){
			h[e->dst]=h[e->src]+e->weight;
			if(k==V-1)return 0;
		}
	}
	return 1;
}
inline void push(Graph &g,int src,int dst,int weight){
	g[src].pb(Edge(src,dst,weight));
}
bool make_graph(){
	int *fail=buildFail(ptn), len=strlen(ptn);
	G.clear(); rG.clear();
	V=n*(len+1)+1;
	s=0; t=V-1;
	while(s>=0&&ptn[s]-'0'!=col[0])s=fail[s];
	if(++s>=len)return 0;
	G.resize(V); rG.resize(V);
	
	vector<vector<pi> > e(n);
	rep(i,m)e[a[i]-1].pb(mp(b[i]-1,c[i]));
	
	rep(i,n)rep(j,len+1){
		fr(k,e[i]){
			int to=j;
			while(to>=0&&ptn[to]-'0'!=col[k->first])to=fail[to];
			if(++to>=len)continue;
			push(G,i*(len+1)+j,k->first*(len+1)+to,k->second);
			push(rG,k->first*(len+1)+to,i*(len+1)+j,0);
		}
	}
	rep(j,len){
		push(G,(n-1)*(len+1)+j,t,0);
		push(rG,t,(n-1)*(len+1)+j,0);
	}
	rep(i,V)v[i]=rv[i]=0;
	dfs(s,G,v); dfs(t,rG,rv);
	return v[t]&&rv[s];
}

int main(){
	while(cin>>n,n){
		rep(i,n)cin>>col[i];
		cin>>m;
		rep(i,m)cin>>a[i]>>b[i]>>c[i];
		cin>>k>>ptn;
		
		if(!make_graph()){
			cout<<"0 0"<<endl; continue;
		}
		if(!calc_potential()){
			cout<<-1<<endl; continue;
		}
		vi ans=k_shortestPath(G,s,t,k,h);
		int sum=0;
		rep(i,ans.size())sum+=ans[i];
		cout<<ans.size()<<" "<<sum<<endl;
	}
	return 0;
}