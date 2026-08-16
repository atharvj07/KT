#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
typedef double D;
typedef complex<D> P;
typedef pair<P,P> L;
D eps=1e-8;
bool eq(D a, D b) { return abs(a-b)<eps;}
bool eq(P a, P b) { return abs(a-b)<eps;}
int sig(D a){return eq(a,0)?0:(a>0?1:-1);}
D dot(P a,P b){return real(conj(a)*b);}
D cro(P a,P b){return imag(conj(a)*b);}
int ccw (P a, P b, P c){
	if(sig(cro(b-a,c-a))==1) return 1;
	if(sig(cro(b-a,c-a))==-1) return -1;
	if(eq(abs(a-c)+abs(c-b),abs(a-b))) return 0;
	if(eq(abs(a-b)+abs(b-c),abs(a-c))) return -2;
	if(eq(abs(c-a)+abs(a-b),abs(c-b))) return 2;
}
P perp(L l, P p){
	D t=dot(p-l.fs,l.fs-l.sc)/norm(l.fs-l.sc);
	return l.fs+t*(l.fs-l.sc);
}
P refl(L l, P p){
	return p+2.0*(perp(l,p)-p);
}
bool online(L l,P p){
	return abs(ccw(l.fs,l.sc,p))!=1;
}
vector<L> uniq(vector<L> vc){
	int N=vc.size();
	bool gomi[100]={};
	rep(i,N){
		rep(j,i){
			bool same=online(vc[i],vc[j].fs)&&online(vc[i],vc[j].sc);
			if(same) gomi[i]=1;
		}
	}
	vector<L> ret;
	rep(i,N) if(!gomi[i]) ret.pb(vc[i]);
	return ret;
}

typedef pair<int,int> Pii;
typedef vector<int> vi;
typedef vector<vi> vv;
vector<vv> parts;
vv now;
map<vv,int> mp;
int N;
void dfs(int x){
	if(x==N){
		mp[now]=parts.size();
		parts.pb(now);
		return;
	}
	rep(i,now.size()){
		now[i].pb(x);
		dfs(x+1);
		now[i].pop_back();
	}
	now.pb(vi(1,x));
	dfs(x+1);
	now.pop_back();
}

bool same(vv vs,int a,int b){
	int N=vs.size();
	int aa=-1,bb=-1;
	rep(i,N){
		for(int x:vs[i]){
			if(x==a) aa=i;
			if(x==b) bb=i;
		}
	}
	assert(aa>=0&&bb>=0);
	return aa==bb;
}
void showvv(vv vs){
	int N=vs.size();
	rep(i,N){
		cout<<"{";
		for(int x:vs[i]) cout<<x<<",";
		cout<<"}  ";
	}
	puts("");
}
int merge(int j,vector<Pii>& as){
	vv now=parts[j];
	int id[8]={};
	rep(i,now.size()){
		vi v=now[i];
		for(int a:v) id[a]=i;
	}
	for(Pii p:as){
		int u=p.fs,v=p.sc;
		if(id[u]==id[v]) continue;
		if(id[u]>id[v]) swap(u,v);
		int from=id[v],to=id[u];
		for(int a:now[from]) id[a]=to;
		now[to].insert(now[to].end(),all(now[from]));
		now[from].clear();
	}
	vv ret;
	for(vi v:now){
		if(!v.empty()){
			sort(all(v));
			ret.pb(v);
		}
	}
	if(!mp.count(ret)){
		showvv(parts[j]);
		for(Pii p:as) cout<<"("<<p.fs<<"-"<<p.sc<<") ";
			puts("");
		showvv(ret);
	}
	assert(mp.count(ret));
	int rid=mp[ret];
	return rid;
}

vector<P> ps;
vector<L> ls;
int dp[29][4140];
int main(){
	cin>>N;
	rep(i,N){
		int x,y;
		cin>>x>>y;
		ps.pb(P(x,y));
	}
	rep(i,N) rep(j,i){
		P m=(ps[i]+ps[j])/2.0;
		P x=(ps[i]-ps[j])*P(0,1);
		ls.pb(L(m,m+x));
	}
	ls=uniq(ls);
	int K=ls.size();
//	show(K);
	dfs(0);
	int M=parts.size();
//	show(M);
	rep(i,K+1) rep(j,M) dp[i][j]=1e9;
//	showvv(parts[0]);
//	showvv(parts[M-1]);
	dp[0][M-1]=0;
	rep(i,K){
//		show(i);
		vector<Pii> as;
		rep(j,N) rep(k,j){
			if(eq(ps[j],refl(ls[i],ps[k]))) as.pb(Pii(k,j));
		}
		rep(j,M){
			chmin(dp[i+1][j],dp[i][j]);
			int nj=merge(j,as);
			chmin(dp[i+1][nj],dp[i][j]+1);
		}
	}
	cout<<dp[K][0]<<endl;
}