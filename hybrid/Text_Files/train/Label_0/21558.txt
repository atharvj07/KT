#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <cstring>
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <cassert>
#include <ctime>
#include <climits>
using namespace std;  
 
#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;
typedef unsigned long long ull;
ll gcd(ll a,ll b) { return b==0?a:gcd(b,a%b); }
 
const int MAXN=400000;
const int MAXQ=50000;
const int MAXEMP=MAXN+MAXQ;
const int SZ=400;
const int MAXB=(MAXEMP+SZ-1)/SZ;
 
int n,nq,nemp;
int par[MAXEMP],oval[MAXEMP]; bool alive[MAXEMP];
int qt[MAXQ],qemp[MAXQ],qd[MAXQ],qby[MAXQ];
 
int chead[MAXEMP],cnxt[MAXEMP];
int d[MAXEMP],lid[MAXEMP],rid[MAXEMP],emp[MAXEMP],nid;
void dfs(int at) {
	d[at]=par[at]==-1?0:d[par[at]]+1; emp[nid]=at,lid[at]=nid++;
	for(int to=chead[at];to!=-1;to=cnxt[to]) dfs(to);
	rid[at]=nid-1;
}
 
int pos[MAXEMP];
int sd[MAXEMP];

typedef struct S {
	ll sval[4*SZ]; int slazy[4*SZ]; int scnt[4*SZ];
	void clear() {
		memset(sval,0,sizeof(sval)); memset(slazy,0,sizeof(slazy)); memset(scnt,0,sizeof(scnt));
	}
	void spush(int x) {
		if(slazy[x]==0) return;
		sval[2*x+1]+=slazy[x]*scnt[2*x+1]; slazy[2*x+1]+=slazy[x];
		sval[2*x+2]+=slazy[x]*scnt[2*x+2]; slazy[2*x+2]+=slazy[x];
		slazy[x]=0;
	}
	void scalc(int x) { scnt[x]=scnt[2*x+1]+scnt[2*x+2]; sval[x]=sval[2*x+1]+sval[2*x+2]; }
	void sborn(int x,int l,int r,int IDX,int VAL) {
		if(l==r) {
			sval[x]=VAL,slazy[x]=0,scnt[x]=1;
		} else {
			spush(x);
			int m=l+(r-l)/2;
			if(IDX<=m) sborn(2*x+1,l,m,IDX,VAL); else sborn(2*x+2,m+1,r,IDX,VAL);
			scalc(x);
		}
		//printf("sborn(%d,%d,%d,%d,%d) -> %d %lld\n",x,l,r,IDX,VAL,scnt[x],sval[x]);
	}
	void smod(int x,int l,int r,int L,int R,int BY) {
		if(L<=l&&r<=R) {
			sval[x]+=(ll)scnt[x]*BY;
			slazy[x]+=BY;
		} else {
			spush(x);
			int m=l+(r-l)/2;
			if(L<=m) smod(2*x+1,l,m,L,R,BY);
			if(m+1<=R) smod(2*x+2,m+1,r,L,R,BY);
			scalc(x);
		}
		//printf("smod(%d,%d,%d,%d,%d,%d) -> %d %lld %d\n",x,l,r,L,R,BY,scnt[x],sval[x],slazy[x]);
	}
	ll sget(int x,int l,int r,int L,int R) {
		if(L<=l&&r<=R) {
			return sval[x];
		} else {
			spush(x);
			int m=l+(r-l)/2; ll ret=0;
			if(L<=m) ret+=sget(2*x+1,l,m,L,R);
			if(m+1<=R) ret+=sget(2*x+2,m+1,r,L,R);
			return ret;
		}
	}
	void save(int x,int l,int r,ll *val,int *cnt) {
		if(l==r) {
			val[l]=sval[x]; cnt[l]=scnt[x];
		} else {
			spush(x);
			int m=l+(r-l)/2; save(2*x+1,l,m,val,cnt); save(2*x+2,m+1,r,val,cnt);
		}
	}
	void load(int x,int l,int r,ll *val,int *cnt) {
		if(l==r) {
			sval[x]=val[l],scnt[x]=cnt[l];
		} else {
			int m=l+(r-l)/2; load(2*x+1,l,m,val,cnt); load(2*x+2,m+1,r,val,cnt);
			scalc(x);
		}
	}
} S;
S s[MAXB];


int nb;
pair<int,int> tmp[SZ];
void build() {
	for(int i=0;i<nemp;i+=SZ) {
		int cnt=min(SZ,nemp-i);
		REP(j,cnt) tmp[j]=MP(d[emp[i+j]],emp[i+j]);
		sort(tmp,tmp+cnt);
		REP(j,cnt) sd[i+j]=tmp[j].first,pos[tmp[j].second]=i+j;
	}
	nb=(nemp+SZ-1)/SZ;
	REP(i,nb) s[i].clear();
	REP(i,nemp) if(alive[i]) s[pos[i]/SZ].sborn(0,0,SZ-1,pos[i]%SZ,oval[i]);
	//REP(i,nemp) printf("%d: emp=%d d=%d pos=%d oval=%d\n",i,emp[i],d[emp[i]],pos[emp[i]],oval[emp[i]]);
	//REP(i,nemp) printf(" %d",sd[i]); puts("");
}

ll tval[SZ]; int tcnt[SZ];
ll query1(int idx,int ld,int rd) {
	//printf("query1(%d,%d,%d)\n",idx,ld,rd);
	if(!alive[idx]||d[idx]<ld||d[idx]>=rd) return 0;
	//return s[pos[idx]/SZ].sget(0,0,SZ-1,pos[idx]%SZ,pos[idx]%SZ);
	return tval[pos[idx]%SZ];
}
 
ll queryb(int idx,int ld,int rd) {
	//printf("queryb(%d,%d,%d)\n",idx,ld,rd);
	int bl=idx*SZ,br=min(nemp,(idx+1)*SZ);
	int l=lower_bound(sd+bl,sd+br,ld)-sd;
	if(l>=br||sd[l]>=rd) return 0;
	int r=lower_bound(sd+bl,sd+br,rd)-sd;
	//printf("->%d..%d (%d,%d)\n",l,r-1,bl,br);
	return s[idx].sget(0,0,SZ-1,l%SZ,(r-1)%SZ);
}
 
ll query(int lid,int rid,int ld,int rd) {
	//printf("query(%d..%d,%d..%d)\n",lid,rid,ld,rd);
	ll ret=0;
	if(lid<rid&&lid%SZ!=0) {
		int b=lid/SZ;
		s[b].save(0,0,SZ-1,tval,tcnt);
		while(lid<rid&&lid%SZ!=0) ret+=query1(emp[lid++],ld,rd);
	}
	if(lid<rid&&rid%SZ!=0) {
		int b=rid/SZ;
		s[b].save(0,0,SZ-1,tval,tcnt);
		while(lid<rid&&rid%SZ!=0) ret+=query1(emp[--rid],ld,rd);
	}
	while(lid<rid) ret+=queryb(lid/SZ,ld,rd),lid+=SZ;
	return ret;
}

void update1(int idx,int ld,int rd,int by) {
	if(!alive[idx]||d[idx]<ld||d[idx]>=rd) return;
	//s[pos[idx]/SZ].smod(0,0,SZ-1,pos[idx]%SZ,pos[idx]%SZ,by);
	tval[pos[idx]%SZ]+=by;
}
 
void updateb(int idx,int ld,int rd,int by) {
	int bl=idx*SZ,br=min(nemp,(idx+1)*SZ);
	int l=lower_bound(sd+bl,sd+br,ld)-sd;
	if(l>=br||sd[l]>=rd) return;
	int r=lower_bound(sd+bl,sd+br,rd)-sd;
	return s[idx].smod(0,0,SZ-1,l%SZ,(r-1)%SZ,by);
}
 
void update(int lid,int rid,int ld,int rd,int by) {
	if(lid<rid&&lid%SZ!=0) {
		int b=lid/SZ;
		s[b].save(0,0,SZ-1,tval,tcnt);
		while(lid<rid&&lid%SZ!=0) update1(emp[lid++],ld,rd,by);
		s[b].load(0,0,SZ-1,tval,tcnt);
	}
	if(lid<rid&&rid%SZ!=0) {
		int b=rid/SZ;
		s[b].save(0,0,SZ-1,tval,tcnt);
		while(lid<rid&&rid%SZ!=0) update1(emp[--rid],ld,rd,by);
		s[b].load(0,0,SZ-1,tval,tcnt);
	}
	while(lid<rid) updateb(lid/SZ,ld,rd,by),lid+=SZ;
}
 
void born(int idx) {
	assert(!alive[idx]); alive[idx]=true;
	s[pos[idx]/SZ].sborn(0,0,SZ-1,pos[idx]%SZ,oval[idx]);
}
 
ll ans[MAXQ];
void solve() {
	REP(i,nemp) chead[i]=-1; REP(i,nemp) if(par[i]!=-1) cnxt[i]=chead[par[i]],chead[par[i]]=i;
	nid=0; dfs(0); build();
 
	REP(i,nq) {
		if(qt[i]==1) update(lid[qemp[i]],rid[qemp[i]]+1,d[qemp[i]],d[qemp[i]]+qd[i]+1,qby[i]);
		if(qt[i]==2) ans[i]=query(lid[qemp[i]],rid[qemp[i]]+1,d[qemp[i]],d[qemp[i]]+qd[i]+1);
		if(qt[i]==3) born(qemp[i]);
	}
}
 
void run() {
	scanf("%d%d",&n,&nq); nemp=n;
	REP(i,n) scanf("%d%d",&par[i],&oval[i]),alive[i]=true;
	REP(i,nq) {
		scanf("%d",&qt[i]);
		if(qt[i]==1) scanf("%d%d%d",&qemp[i],&qd[i],&qby[i]);
		if(qt[i]==2) scanf("%d%d",&qemp[i],&qd[i]);
		if(qt[i]==3) scanf("%d%d",&par[nemp],&oval[nemp]),alive[nemp]=false,qemp[i]=nemp++;
	}
	solve();
	REP(i,nq) if(qt[i]==2) printf("%lld\n",ans[i]);
}
 
void stress() {
	REP(x,10) {
		n=MAXN; nq=MAXQ;
		par[0]=-1; FOR(i,1,n) par[i]=i<n/10?i-1:(rand()*1000+rand())%(n/10); REP(i,n) oval[i]=rand()%1000+1,alive[i]=true; nemp=n;
		REP(i,nq) {
			qt[i]=rand()%3+1;
			if(qt[i]==1) qemp[i]=rand()%min(n,10),qd[i]=rand()%(n/10),qby[i]=rand()%1000+1;
			if(qt[i]==2) qemp[i]=rand()%min(n,10),qd[i]=rand()%(n/10);
			if(qt[i]==3) qemp[i]=nemp,par[nemp]=(rand()*1000+rand())%(n/10),oval[nemp]=rand()%1000+1,alive[nemp]=false,++nemp;
		}
		clock_t begin = clock();
		solve();
		//REP(i,nq) if(qt[i]==2) printf("%lld\n",ans[i]); exit(0);
		ll chk=0; REP(i,nq) if(qt[i]==2) chk+=ans[i];
		printf("%.9lf %lld\n",double(clock() - begin) / CLOCKS_PER_SEC,chk);
	}
}
 
int main() {
	//stress();
	run();
	return 0;
}
