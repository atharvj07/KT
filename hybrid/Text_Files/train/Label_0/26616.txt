#include <bits/stdc++.h>
using namespace std;
#define ref(i,x,y)for(int i=x;i<=y;++i)
#define def(i,x,y)for(int i=x;i>=y;--i)
#define pb push_back
#define SZ(x) ((int)x.size())
#define mp make_pair
#define fi first
#define se second
typedef vector<int> vint;
typedef long long LL;
typedef pair<int,int> PII;
const int N=500010;
int read(){
	char c=getchar();int d=0,f=1;
	for(;c<'0'||c>'9';c=getchar())if(c=='-')f=-1;
	for(;c>='0'&&c<='9';d=d*10+c-48,c=getchar());
	return d*f;
}
int n,q,m,cnt,s[N],res[N];
int a[N];
multiset<PII> S;
vector<PII> p,px,py,pz,rd;int Rd[N];
bool cmpse(PII a,PII b){return a.se<b.se;}
void upd(int x,int s){	
	for(;x<=m;x+=x&-x)a[x]+=s;
}
int ask(int x){int s=0;
	for(;x;x-=x&-x)s+=a[x];return s;
}
int main(){
	n=read();
	ref(i,1,n*3+1)rd.pb(mp(read(),i));
	q=read();
	ref(i,1,q*2)rd.pb(mp(read(),n*3+1+i));
	sort(rd.begin(),rd.end());
	for(int i=0,la=-1;i<SZ(rd);++i){
		m+=rd[i].fi!=la;la=rd[i].fi;
		Rd[rd[i].se]=m;
	}
	ref(i,1,n){
		int a=Rd[++cnt],b=Rd[++cnt];
		s[a]++;if(b<a)p.pb(mp(b,a-1));
	}
	ref(i,1,n+1)s[Rd[++cnt]]--;
	ref(i,1,m)if(s[i])upd(i,s[i]);
	px=py=p;
	ref(i,0,SZ(px)-1)swap(px[i].fi,px[i].se);
	sort(px.begin(),px.end(),cmpse);
	sort(py.begin(),py.end(),cmpse);
	S.clear();S.insert(mp(1e9,1e9));
	bool flag=1;
	int rs=n;
	for(int i=m,cntb=SZ(py)-1;i>=1;--i){
		int s=ask(i);if(s>=-1)continue;s=-1-s;
		while(cntb>=0&&py[cntb].se>=i)S.insert(py[cntb--]);
		while(s){
			multiset<PII>::iterator it=S.lower_bound(mp(0,0));
			PII w=*it;
			if(w.fi>i){flag=0;break;}
			upd(w.se+1,-1);
			upd(w.fi,1);
			S.erase(it);
			pz.pb(mp(w.se,w.fi));
			rs--;s--;
		}
		if(!flag)break;
	}
	sort(pz.begin(),pz.end(),cmpse);
	if(!flag){
		ref(i,1,q)puts("-1");
		return 0;
	}
	S.clear();S.insert(mp(1e9,1e9));S.insert(mp(0,0));
	ref(i,1,m)res[i]=-1e9;
	for(int i=1,cnta=0,cntb=0;i<=m;++i){
		res[i]=rs;
		int s=ask(i);if(s>=0)continue;s=-s;
		while(cnta<SZ(px)&&px[cnta].se<=i)S.insert(px[cnta++]);
		while(cntb<SZ(pz)&&pz[cntb].se<=i)S.erase(S.lower_bound(pz[cntb++]));
		while(s){
			multiset<PII>::iterator it=--S.lower_bound(mp(1e9,1e9));
			PII w=*it;
			if(w.fi<i){flag=0;break;}
			upd(w.fi+1,-1);
			upd(w.se,1);
			S.erase(it);
			rs--;s--;
		}
		if(!flag)break;
	}
	ref(i,1,q){
		int a=Rd[++cnt],b=Rd[++cnt];
		int ans=max(res[a]+1,res[b]);
		if(ans<0)ans=-1;
		printf("%d\n",ans);
	}
}