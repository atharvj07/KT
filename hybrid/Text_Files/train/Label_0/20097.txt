#include <iostream>
#include <fstream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define EPS 1e-9
#define INF MOD
#define MOD 1000000007LL
#define fir first
#define iss istringstream
#define sst stringstream
#define ite iterator
#define ll long long
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<n;i++)
#define pi pair<int,int>
#define pb push_back
#define sec second
#define sh(i) (1LL<<i)
#define sz size()
#define vi vector<int>
#define vc vector
#define vl vector<ll>
#define vs vector<string>

#define FOR(t,i,c) for(t::const_iterator i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()

struct E{
	int to,w;
	E(int a,int b):to(a),w(b){}
};

typedef vc<E> Es;
typedef vc<Es> Gr;

bool visit(const Gr& g,int v,vi& order,vi& color){
	color[v]=1;
	FOR(Es,e,g[v]){
		if(color[e->to]==2)continue;
		if(color[e->to]==1)return 0;
		if(!visit(g,e->to,order,color))return 0;
	}
	order.pb(v);color[v]=2;
	return 1;
}

bool topo(const Gr& g,vi& order){
	int n=g.sz;
	vi color(n);
	rep(u,n)if(!color[u]&&!visit(g,u,order,color))return 0;
	reverse(ALL(order));
	return 1;
}

int n,xs,ys,xt,yt,X,Y,R,ax[1010],ay[1010],ar[1010],bx[1010],by[1010],br[1010],dpa[1010],dpb[1010];
Gr ga,gb;

int sq(int x){return x*x;}

int d2(int x,int y,int xx,int yy){
	return sq(x-xx)+sq(y-yy);
}

int main(){
	while(cin>>n,n){
		cin>>xs>>ys>>xt>>yt;
		int A=0,B=0;
		rep(i,n){
			cin>>X>>Y>>R;
			int a=d2(xs,ys,X,Y),b=d2(xt,yt,X,Y);
			if(a<R*R&&b>R*R)ax[A]=X,ay[A]=Y,ar[A++]=R;
			if(a>R*R&&b<R*R)bx[B]=X,by[B]=Y,br[B++]=R;
		}
		ga.clear(),ga.resize(A),gb.clear(),gb.resize(B);
		rep(i,A)rep(j,A)if(ar[i]<ar[j]&&d2(ax[i],ay[i],ax[j],ay[j])<sq(ar[i]-ar[j]))ga[i].pb(E(j,0));
		rep(i,B)rep(j,B)if(br[i]<br[j]&&d2(bx[i],by[i],bx[j],by[j])<sq(br[i]-br[j]))gb[i].pb(E(j,0));
		vi va,vb;
		topo(ga,va),topo(gb,vb);
		fill(dpa,dpa+1010,A>0),fill(dpb,dpb+1010,B>0);
		rep(i,A)rep(j,ga[va[i]].sz)dpa[ga[va[i]][j].to]=max(dpa[ga[va[i]][j].to],dpa[va[i]]+1);
		rep(i,B)rep(j,gb[vb[i]].sz)dpb[gb[vb[i]][j].to]=max(dpb[gb[vb[i]][j].to],dpb[vb[i]]+1);
		int a=max(*max_element(dpa,dpa+A),*max_element(dpb,dpb+B));
		rep(i,A)rep(j,B)if(d2(ax[i],ay[i],bx[j],by[j])>sq(ar[i]+br[j]))a=max(a,dpa[i]+dpb[j]);
		cout<<a<<endl;
	}
}