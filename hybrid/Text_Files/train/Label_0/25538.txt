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

template<typename Ch,typename Tr,typename C,typename=decltype(begin(C()))>
basic_ostream<Ch,Tr>& operator<<(basic_ostream<Ch,Tr>& os,const C& c){
	os<<'[';
	for(auto i=begin(c);i!=end(c);++i)
		os<<(i==begin(c)?"":" ")<<*i;
	return os<<']';
}

constexpr int INF=1e9;
constexpr int MOD=1e9+7;
constexpr double EPS=1e-9;

bool GaussJordan(const vvd& _a,const vd& b,vd& x)
{
	int n=_a.size();
	vvd a(n,vd(n+1));
	rep(i,n){
		copy(all(_a[i]),begin(a[i]));
		a[i][n]=b[i];
	}
	
	rep(i,n){
		int p=i;
		repi(j,i+1,n) if(abs(a[p][i])<abs(a[j][i])) p=j;
		if(abs(a[p][i])<EPS) return false;
		swap(a[i],a[p]);
		peri(j,i,n+1) a[i][j]/=a[i][i];
		rep(j,n) if(j!=i) peri(k,i,n+1) a[j][k]-=a[j][i]*a[i][k];
	}
	
	rep(i,n) x[i]=a[i][n];
	return true;
}

struct Edge{
	int src,dst;
	double cost;
	int cap,flow;
	Edge(){}
	Edge(int s,int d,double co,int ca=0,int f=0):src(s),dst(d),cost(co),cap(ca),flow(f){}
};
bool operator<(const Edge& a,const Edge& b){return a.cost<b.cost;}
bool operator>(const Edge& a,const Edge& b){return a.cost>b.cost;}
struct Graph{
	vector<Edge> es;
	vi head,next;
	Graph(){}
	Graph(int n):head(n,-1){}
	// コスト:-co,容量:0の逆辺も追加する
	void AddEdge(int u,int v,double co,int ca){
		es.emplace_back(u,v,co,ca); next.push_back(head[u]); head[u]=es.size()-1;
		es.emplace_back(v,u,-co,0); next.push_back(head[v]); head[v]=es.size()-1;
	}
};

double MinCostFlow(Graph& g,int tap,int sink,int flow)
{
	int n=g.head.size();
	
	double res=0;
	vd pots(n);
	while(flow>EPS){
		vd cost(n,INF);
		vi prev(n,-1);
		priority_queue<Edge,vector<Edge>,greater<Edge>> pq;
		pq.emplace(-1,tap,0);
		while(pq.size()){
			Edge cur=pq.top(); pq.pop();
			if(cur.cost>cost[cur.dst]-EPS) continue;
			cost[cur.dst]=cur.cost;
			prev[cur.dst]=cur.src;
			for(int i=g.head[cur.dst];i!=-1;i=g.next[i]){
				Edge e=g.es[i];
				if(e.cap-e.flow==0) continue;
				pq.emplace(i,e.dst,cost[e.src]+e.cost+pots[e.src]-pots[e.dst]);
			}
		}
		
		if(cost[sink]==INF) return -1;
		rep(i,n) pots[i]+=cost[i];
		
		int augment=flow;
		for(int v=sink;v!=tap;v=g.es[prev[v]].src){
			Edge e=g.es[prev[v]];
			augment=min(augment,e.cap-e.flow);
		}
		if(augment<EPS) return -1;
		for(int v=sink;v!=tap;v=g.es[prev[v]].src){
			int i=prev[v];
			g.es[i].flow+=augment;
			g.es[i^1].flow-=augment;
		}
		flow-=augment;
		res+=augment*pots[sink];
	}
	
	return res;
}

void solve()
{
	int n,s,t,f; cin>>n>>s>>t>>f;
	vd cs(n);
	{
		vvd a(n,vd(n));
		vd b(n);
		rep(i,n){
			rep(j,n) cin>>a[i][j];
			cin>>b[i];
		}
		GaussJordan(a,b,cs);
	}
	Graph g(n);
	rep(i,n){
		int m; cin>>m;
		vi ds(m),fs(m);
		rep(j,m) cin>>ds[j];
		rep(j,m) cin>>fs[j];
		rep(j,m) g.AddEdge(i,ds[j],abs(cs[ds[j]]-cs[i]),fs[j]);
	}
	double res=MinCostFlow(g,s,t,f);
	if(res==-1)
		puts("impossible");
	else
		printf("%.10f\n",res);
}

int main()
{
	int tc; cin>>tc;
	rep(_,tc) solve();
}