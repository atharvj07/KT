#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair < int , int > pii;
typedef pair < LL , int > pli;
typedef pair < int , LL > pil;
typedef pair < LL , LL > pll;
#define mpr make_pair
#define FS first
#define SC second
#define PB push_back
template < typename T > T MAX(T a,T b){return (a>b)?a:b;}
template < typename T > T MIN(T a,T b){return (a<b)?a:b;}
template < typename T > void UMAX(T &a,T b){a=(a>b?a:b);}
template < typename T > void UMIN(T &a,T b){a=(a<b?a:b);}
LL readint(){
	char c=getchar();
	LL ret=0ll;
	while(!(c>='0' && c<='9')) c=getchar();
	while(c>='0' && c<='9'){
		ret=ret*10ll+(LL)(c-'0');
		c=getchar();
	}
	return ret;
}
void putint(LL v){
	if(!v){
		putchar('0');
		return;
	}
	if(v>=10ll) putint(v/10ll);
	putchar('0'+(v%10ll));
}
const LL MOD=1000000007ll;
int n,th[100005],tl[100005];
LL gh[100005],dh[100005],dl[100005];
LL mymod(LL a,LL b){
	if(!b) return a;
	if(b<0ll) b=-b;
	return (a<0ll?(b-((-a)%b))%b:(a%b));
}
LL iter(LL a,LL b){
	if(!b) return 0ll;
	if(b<0ll) return iter(-a,-b);
	return (a<0ll?(-((-a+b-1)/b)):(a/b));
}
int vis[100005];
vector < pil > stk;
struct grf{
	pil out[100005];
	vector < pil > in[100005],cycs[100005];
	vector < LL > prsum[100005];
	vector < int > srs;
	int cyccnt,compcnt,incomp[100005],top[100005],udep[100005];
	bool oncyc[100005];
	LL dep[100005],cyctot[100005];
	void adde(int u,int v,LL w){
		out[u]=mpr(v,w);
		in[v].push_back(mpr(u,w));
	}
	void dfs(int v){
		vis[v]=1;
		int u=out[v].FS;
		LL w=out[v].SC;
		if(u==n || u==-1){
			srs.push_back(v);
			vis[v]=2;
			return;
		}
		stk.push_back(mpr(v,w));
		if(vis[u]==1){
			vector < pil > &tar=cycs[cyccnt];
			vector < LL > &tarsum=prsum[cyccnt];
			int i;
			for(i=(int)stk.size()-1;i>=0;--i){
				oncyc[stk[i].FS]=1;;
				if(stk[i].FS==u) break;
			}
//			if(i<0){
//				printf("forkyou!\n");
//				for(int j=0;j<(int)stk.size();++j){
//					printf("%d ",stk[j].FS);
//				}
//				printf("\nexp %d\n",u);
//			}
//			if(i<0) printf("fuckyou\n");
//			assert(i>=0);
			tar=vector < pil >(stk.begin()+i,stk.end());
			tarsum.resize(tar.size(),0ll);
			for(i=1;i<(int)tarsum.size();++i){
				tarsum[i]=tar[i-1].SC+tarsum[i-1];
			}
			cyctot[cyccnt++]=tarsum.back()+tar.back().SC;
		}
		else if(!vis[u]) dfs(u);
		stk.pop_back();
		vis[v]=2;
	}
	void dfs2(int v,LL d,int ud,int tp,int compid){
		int i;
		top[v]=tp;
		dep[v]=d;
		udep[v]=ud;
		incomp[v]=compid;
		for(i=0;i<(int)in[v].size();++i){
			int u=in[v][i].FS;
			LL w=in[v][i].SC;
			if(!oncyc[u])
				dfs2(u,d+w,ud+1,tp,compid);
		}
	}
	void build(){
		int i,j,k;
		memset(vis,0,sizeof(vis));
		for(i=0;i<n;++i){
			if(!vis[i]) dfs(i);
		}
		for(i=0;i<(int)srs.size();++i){
			dfs2(srs[i],0ll,0,srs[i],compcnt++);
		}
		for(i=0;i<cyccnt;++i){
			int cc=compcnt++;
			for(j=0;j<(int)cycs[i].size();++j){
				dfs2(cycs[i][j].FS,0ll,0,cycs[i][j].FS,cc);
			}
		}
	}
	void print(){
		int i,j,k;
		printf("Graph:\n");
		for(i=0;i<n;++i){
			printf("%d->%d [label=%lld];\n",i,out[i].FS,out[i].SC);
		}
		printf("cyccnt=%d compcnt=%d srcnt=%d\n",cyccnt,compcnt,(int)srs.size());
		for(i=0;i<n;++i){
			printf("node %d: incomp %d dep %lld udep %d oncyc %d top %d\n",i,incomp[i],dep[i],udep[i],oncyc[i],top[i]);
		}
		printf("\n");
	}
}He,Li;
map < LL , pii > qrs[100005];
map < LL , set < pli > > mp1[100005];
map < LL , set < int > > mp2[100005];
int cycid[100005],cycrk[100005];
pii ansforcyc(int cd,int ent,LL v){
	LL bas=v-Li.prsum[cd][ent],itr=iter(bas,Li.cyctot[cd]),dlt=mymod(bas,Li.cyctot[cd]);
	set < int >::iterator it2=mp2[cd][bas].lower_bound(ent);
	if(it2!=mp2[cd][bas].end()){
		int td=*it2;
		return mpr(Li.cycs[cd][td].FS,td-ent);
	}
	if(!Li.cyctot[cd]){
		set < pli >::iterator it1=mp1[cd][dlt].lower_bound(mpr(0ll,-1));
		if(it1!=mp1[cd][dlt].end()){
			int td=it1->SC;
			LL itc=it1->FS-itr+1ll;
			return mpr(Li.cycs[cd][td].FS,(itc%MOD*(LL)Li.cycs[cd].size()+(LL)(td-ent)+MOD)%MOD);
		}
	}
	else{
		set < pli >::iterator it1=mp1[cd][dlt].lower_bound(mpr(itr+1ll,-1));
		if(it1!=mp1[cd][dlt].end()){
			int td=it1->SC;
			LL itc=it1->FS-itr;
			return mpr(Li.cycs[cd][td].FS,(itc%MOD*(LL)Li.cycs[cd].size()+(LL)(td-ent)+MOD)%MOD);
		}
	}
	return mpr(-1,0);
}
void precalcyc(int cd,vector < pil > lst,vector < LL > sfts,LL sum){
	int i,len=(int)lst.size();
	for(i=0;i<len;++i){
		int u=lst[i].FS;
		LL w=gh[u]-sfts[i];
		mp1[cd][mymod(w,sum)].insert(mpr(iter(w,sum),i));
		mp2[cd][w].insert(i);
		cycid[u]=cd;
		cycrk[u]=i;
	}
}
set < pair < LL , pii > > curstk;
void dfs(int v){
	pair < LL , pii > cur=mpr(gh[v]+Li.dep[v],mpr(-Li.udep[v],v));
	curstk.insert(cur);
	int i;
	for(i=0;i<(int)Li.in[v].size();++i){
		int u=Li.in[v][i].FS;
		if(cycid[u]==-1) dfs(u);
	}
	map < LL , pii >::iterator it;
	for(it=qrs[v].begin();it!=qrs[v].end();++it){
		LL cv=it->FS+Li.dep[v];
		set < pair < LL , pii > >::iterator lb=curstk.lower_bound(mpr(cv,mpr(-n,-1)));
		if(lb!=curstk.end() && lb->FS==cv){
			it->SC.FS=lb->SC.SC;
			it->SC.SC=Li.udep[v]-Li.udep[lb->SC.SC];
		}
	}
	curstk.erase(curstk.find(cur));
}
int main(){
	int i,j,k;
	scanf("%d%lld",&n,gh);
	++n;
	th[0]=1;
	Li.adde(0,1,0ll);
	qrs[1][gh[0]+dh[0]]=mpr(-1,0);
	for(i=1;i<n;++i){
		scanf("%lld%lld%d%lld%d",gh+i,dh+i,th+i,dl+i,tl+i);
		Li.adde(i,tl[i],dl[i]);
		qrs[th[i]][gh[i]+dh[i]]=mpr(-1,0);
	}
	Li.build();
	memset(cycid,-1,sizeof(cycid));
	for(i=0;i<Li.cyccnt;++i){
		precalcyc(i,Li.cycs[i],Li.prsum[i],Li.cyctot[i]);
	}
	for(i=0;i<(int)Li.srs.size();++i){
		cycid[Li.srs[i]]=-2;
	}
	for(i=0;i<n;++i){
		if(cycid[i]!=-1){
			dfs(i);
		}
	}
	for(i=0;i<n;++i){
		map < LL , pii >::iterator it;
		for(it=qrs[i].begin();it!=qrs[i].end();++it){
			if(it->SC.FS==-1){
				if(cycid[Li.top[i]]==-2){
					it->SC.FS=n;
					it->SC.SC=Li.udep[i]+1;
				}
				else{
					it->SC=ansforcyc(cycid[Li.top[i]],cycrk[Li.top[i]],it->FS+Li.dep[i]);
					(it->SC.SC+=Li.udep[i])%=MOD;
				}
			}
		}
	}
	for(i=0;i<n;++i){
		int v=th[i];
		LL nx=gh[i]+dh[i];
		pii pt=qrs[v][nx];
//		printf("heavier outer of %d = (%d,%d)  %d %lld\n",i,pt.FS,pt.SC,v,nx);
		if(v==n)
			He.adde(i,n,1ll);
		else
			He.adde(i,pt.FS,(pt.SC+1)%MOD);
	}
	He.build();
	int tp=He.top[0],tdis=(He.dep[0]+He.out[tp].SC)%MOD;
	if(He.out[tp].FS==n)
		printf("%d\n",(int)((tdis+MOD-1ll)%MOD));
	else
		printf("-1\n");
//	Li.print();
//	He.print();
	return 0;
}
/*
 * 代码框架
 * 0. 实现负数取模（除数取abs）
 * 0. 将重边终点处的权值按点组织，用map存储。稍后修改此map。
 * 1. 实现带权基环树森林struct，无前驱可记为-1或n
 * 		实现加边、标记环点、拆出环vecs和根集合、标记连通块编号、计算每个点带权/不带权深度、计算每个点上方环点
 * 2. 将轻边建出基环树森林，预处理每个环点的校准值。
 * 		实现map<ll,set<pli>>维护初值到循环、编号二元组的映射
 * 		实现map<pll,set<int>>维护循环、初值二元组到编号集合的映射
 * 2. 实现函数，给定环编号、进入点、进入值，返回终止点和经过步数（取模，exclusive）
 * 3. 建立重边基环树森林，稍作判定
 * 4. 初始时建新点。别忘记特判n+1。
*/
