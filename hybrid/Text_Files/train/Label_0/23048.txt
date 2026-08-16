//zxggtxdy!
#include<bits/stdc++.h>
using namespace std;
#define LL long long
const int N=1e6,Q=1e6+7;
int n,m,k,q,a[Q],b[Q],pos[Q];
multiset<int>f1,f2;
struct Seg{
	LL f1[Q<<2],f2[Q<<2];
	inline void covex(int u,LL A,LL B){
		u=pos[u],f1[u]+=A,f2[u]+=B,u=u>>1;
		while(u>0) f1[u]=f1[u<<1]+f1[u<<1|1],f2[u]=f2[u<<1]+f2[u<<1|1],u=u>>1;
	}
	inline pair<LL,LL> getsum(int l,int r,int t,int ql,int qr){
		if(l==ql&&r==qr) return make_pair(f1[t],f2[t]); int d=(l+r)>>1; LL A=0,B=0;
		if(ql<=d){
			pair<LL,LL>T=getsum(l,d,t<<1,ql,min(d,qr)); A+=T.first,B+=T.second;
		}
		if(d+1<=qr){
			pair<LL,LL>T=getsum(d+1,r,t<<1|1,max(d+1,ql),qr); A+=T.first,B+=T.second;
		}
		return make_pair(A,B);
	}
}T1,T2;
inline void build(int l,int r,int t){
	if(l==r) {pos[l]=t; return;} int d=(l+r)>>1; build(l,d,t<<1),build(d+1,r,t<<1|1);
}
inline int read(){
	int num=0; char g=getchar(); while(g<48||57<g) g=getchar();
	while(47<g&&g<58) num=(num<<1)+(num<<3)+g-48,g=getchar(); return num;
}
inline long long getans1(int u){
	long long ans=0; int D=u-k; T1.covex(u,-1,-u);
	if(D<=N){
		pair<LL,LL>T=T2.getsum(0,N,1,max(D,0),N);
		ans=ans-T.second+T.first*D;
	}
	D=min(min((*f1.begin()),(*f2.begin())),D);
	if(D<=N){
		pair<LL,LL>T=T1.getsum(0,N,1,max(D,0),N);
		ans=ans+T.second-T.first*D;
	}
	T1.covex(u,1,u); return ans+k;
}
inline long long getans2(int u){
	long long ans=0; int D=u-k; T2.covex(u,-1,-u);
	if(D<=N){
		pair<LL,LL>T=T2.getsum(0,N,1,max(D,0),N);
		ans=ans-T.second+T.first*D;
	}
	D=min(min((*f1.begin()),(*f2.begin())),D);
	if(D<=N){
		pair<LL,LL>T=T1.getsum(0,N,1,max(D,0),N);
		ans=ans+T.second-T.first*D;
	}
	T2.covex(u,1,u); return ans-k;
}
int main(){
	n=read(),m=read(),q=read(); build(0,N,1);
	for(int i=1;i<=n;i++) a[i]=read(),T1.covex(a[i],1,a[i]),f1.insert(a[i]);
	for(int i=1;i<=m;i++) b[i]=read(),T2.covex(b[i],1,b[i]),f2.insert(b[i]);
	while(q--){
		int op=read();
		if(op==1){
			int u=read(),v=read(); T1.covex(a[u],-1,-a[u]),f1.erase(f1.find(a[u]));
			a[u]=v,T1.covex(a[u],1,a[u]),f1.insert(a[u]);
		}
		if(op==2){
			int u=read(),v=read(); T2.covex(b[u],-1,-b[u]),f2.erase(f2.find(b[u]));
			b[u]=v,T2.covex(b[u],1,b[u]),f2.insert(b[u]);
		}
		multiset<int>::iterator zxak;
		if(op==3){
			long long ans=-1e18; k=read();
			ans=max(ans,getans1((*f1.begin())));
			ans=max(ans,getans2((*f2.begin())));
			ans=max(ans,getans1((*f1.rbegin())));
			ans=max(ans,getans2((*f2.rbegin())));
			zxak=f1.lower_bound(k-min(*f1.begin(),*f2.begin()));
			if(zxak!=f1.end()) ans=max(ans,getans1(*zxak));
			if(zxak!=f1.begin()) ans=max(ans,getans1(*(--zxak)));
			zxak=f1.lower_bound(*f2.rbegin()+k);
			if(zxak!=f1.end()) ans=max(ans,getans1(*zxak));
			if(zxak!=f1.begin()) ans=max(ans,getans1(*(--zxak)));
			zxak=f2.lower_bound(k-min(*f1.begin(),*f2.begin()));
			if(zxak!=f2.end()) ans=max(ans,getans2(*zxak));
			if(zxak!=f2.begin()) ans=max(ans,getans2(*(--zxak)));
			zxak=f2.lower_bound(*f1.rbegin()+k);
			if(zxak!=f2.end()) ans=max(ans,getans2(*zxak));
			if(zxak!=f2.begin()) ans=max(ans,getans2(*(--zxak)));
			printf("%lld\n",ans);
		}
	}
	return 0;
}