#include <bits/stdc++.h>
using namespace std;

#define dump(...) cout<<"# "<<#__VA_ARGS__<<'='<<(__VA_ARGS__)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}

template<typename Tuple>
void print_tuple(ostream&,const Tuple&){}
template<typename Car,typename... Cdr,typename Tuple>
void print_tuple(ostream& os,const Tuple& t){
	print_tuple<Cdr...>(os,t);
	os<<(sizeof...(Cdr)?",":"")<<get<sizeof...(Cdr)>(t);
}
template<typename... Args>
ostream& operator<<(ostream& os,const tuple<Args...>& t){
	print_tuple<Args...>(os<<'(',t);
	return os<<')';
}

template<typename Ch,typename Tr,typename C>
basic_ostream<Ch,Tr>& operator<<(basic_ostream<Ch,Tr>& os,const C& c){
	os<<'[';
	for(auto i=begin(c);i!=end(c);++i)
		os<<(i==begin(c)?"":" ")<<*i;
	return os<<']';
}

constexpr int INF=1e9;
constexpr int MOD=1e9+7;
constexpr double EPS=1e-9;

struct Edge{
	int src,dst,weight;
	Edge(){}
	Edge(int s,int d,int w):src(s),dst(d),weight(w){}
};
typedef vector<vector<Edge>> Graph;
bool operator<(const Edge& a,const Edge& b){return a.weight<b.weight;}
bool operator>(const Edge& a,const Edge& b){return a.weight>b.weight;}

ostream& operator<<(ostream& os,const Edge& e){
	return os<<'('<<e.src<<','<<e.dst<<':'<<e.weight<<')';
}
void print(const Graph& g)
{
	rep(i,g.size()){
		cout<<i<<':';
		for(auto e:g[i]) cout<<" ("<<e.dst<<':'<<e.weight<<')';
		cout<<endl;
	}
}


// (頂点,その頂点を含めて禁止パターンにマッチした文字数)でグラフを拡張
Graph extend(const Graph& g,const vi& colors,const vi& forbidden)
{
	vi fail(forbidden.size()+1);
	fail[0]=-1;
	for(int i=0,j=-1;i<forbidden.size();){
		while(j>=0 && forbidden[i]!=forbidden[j])
			j=fail[j];
		i++,j++;
		fail[i]=j;
	}
	
	Graph g2;
	map<pii,int> f;
	queue<tuple<int,int,int,int,int>> q; q.emplace(-1,-1,0,0,0);
	while(q.size()){
		int u,i,v,j,w; tie(u,i,v,j,w)=q.front(); q.pop();
		while(j>=0 && colors[v]!=forbidden[j])
			j=fail[j];
		j++;
		if(j==forbidden.size()) continue;
		bool newv=f.insert(mp(mp(v,j),f.size())).second;
		if(newv) g2.resize(g2.size()+1);
		if(u>=0) g2[f[mp(u,i)]].emplace_back(f[mp(u,i)],f[mp(v,j)],w);
		if(newv)
			for(auto e:g[v])
				q.emplace(v,j,e.dst,j,e.weight);
	}
	
	// 拡張したグラフには，始点が0~1個，終点が0~n個あるので
	// それぞれ1つずつとなるようにまとめる
	int src=g2.size(),dst=g2.size()+1;
	g2.resize(g2.size()+2);
	for(auto p:f){
		int i=p.first.first,v=p.second;
		if(i==0){
			g2[src].emplace_back(src,v,0);
			break;
		}
	}
	for(auto p:f){
		int i=p.first.first,v=p.second;
		if(i==colors.size()-1)
			g2[v].emplace_back(v,dst,0);
	}
	return g2;
}

// V'={v: src ~> v AND v ~> dst}の誘導部分グラフを構築
Graph induce(const Graph& g)
{
	int src=g.size()-2,dst=g.size()-1;
	
	vi vis1(g.size());
	queue<int> q; q.push(src);
	while(q.size()){
		int u=q.front(); q.pop();
		if(vis1[u]) continue;
		vis1[u]=1;
		for(auto e:g[u]) q.push(e.dst);
	}
	
	Graph ig(g.size());
	rep(i,g.size()) for(auto e:g[i])
		ig[e.dst].emplace_back(e.dst,e.src,e.weight);
	
	vi vis2(g.size());
	q.push(dst);
	while(q.size()){
		int u=q.front(); q.pop();
		if(vis2[u]) continue;
		vis2[u]=1;
		for(auto e:ig[u]) q.push(e.dst);
	}
	
	Graph g2(g.size());
	rep(i,g.size()) for(auto e:g[i])
		if(vis1[e.src] && vis2[e.src] && vis1[e.dst] && vis2[e.dst])
			g2[e.src].emplace_back(e.src,e.dst,e.weight);
	return g2;
}

void solve(const Graph& g,int k)
{
	int n=g.size();
	int src=g.size()-2,dst=g.size()-1;
	
	vi pots(n,INF); pots[src]=0;
	rep(i,n){
		bool updated=false;
		rep(j,n) for(auto e:g[j])
			if(pots[e.dst]>pots[e.src]+e.weight){
				pots[e.dst]=pots[e.src]+e.weight;
				updated=true;
			}
		if(i==n-1 && updated){
			cout<<-1<<endl;
			return;
		}
	}
	
	vvi dist(n);
	priority_queue<Edge,vector<Edge>,greater<Edge>> pq; pq.emplace(-1,0,0);
	while(pq.size()){
		Edge cur=pq.top(); pq.pop();
		if(dist[cur.dst].size()==k) continue;
		dist[cur.dst].push_back(cur.weight);
		for(auto e:g[cur.dst])
			pq.emplace(e.src,e.dst,cur.weight+e.weight+pots[e.src]-pots[e.dst]);
	}
	//dump(g);
	//dump(pots);
	//dump(dist);
	//rep(i,n){
	//	rep(j,dist[i].size()) cout<<dist[i][j]+pots[i]<<' ';
	//	cout<<endl;
	//}
	
	int res=0;
	for(int x:dist[dst]) res+=x+pots[dst];
	cout<<dist[dst].size()<<' '<<res<<endl;
}

int main()
{
	for(int n;cin>>n && n;){
		vi colors(n);
		rep(i,n) cin>>colors[i];
		int m; cin>>m;
		Graph g(n);
		rep(i,m){
			int u,v,w; cin>>u>>v>>w; u--,v--;
			g[u].emplace_back(u,v,w);
		}
		int k; cin>>k;
		vi forbidden;
		{
			string s; cin>>s;
			rep(i,s.size()) forbidden.push_back(s[i]-'0');
		}
		
		g=induce(extend(g,colors,forbidden));
		solve(g,k);
	}
}