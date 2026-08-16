#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define db double
#define pint pair<int,int>
#define mk(x,y) make_pair(x,y)
#define fir first
#define sec second
#define Rep(x,y,z) for(int x=y;x<=z;x++)
#define Red(x,y,z) for(int x=y;x>=z;x--)
using namespace std;
const int MAXN=2e5+5;
char buf[1<<12],*pp1=buf,*pp2=buf,nc;int ny;
inline char gc() {return pp1==pp2&&(pp2=(pp1=buf)+fread(buf,1,1<<12,stdin),pp1==pp2)?EOF:*pp1++;}
//inline char gc(){return getchar();}
inline int read(){
	int x=0;for(ny=1;nc=gc(),(nc<48||nc>57)&&nc!=EOF;)if(nc==45)ny=-1;if(nc<0)return nc;
	for(x=nc-48;nc=gc(),47<nc&&nc<58&&nc!=EOF;x=(x<<3)+(x<<1)+(nc^48));return x*ny;
}
priority_queue<pint,vector<pint>,greater<pint> >q;
int n,L,l[MAXN],r[MAXN];ll lf[MAXN],rf[MAXN],f1[MAXN],f2[MAXN];
vector<int>S1,S2;
inline void add(int x,int y){r[l[y]=x]=y;}
inline ll Solve(int x){
	ll res=0,tmp=0;int len=S2.size(),lb=l[S2[0]],rb=r[S2[len-1]];
	for(int i=0;i<len;i++)(i-L+1>=0?tmp+=lf[S2[i-L+1]]:0),res+=rf[S2[i]]*tmp;
	for(int i=0;i<len;i++)f1[S2[i]]=lf[S2[i]],f2[S2[i]]=rf[S2[i]],lf[S2[i]]=rf[S2[i]]=0;
	int cnt=len/L;
	if(cnt){
		for(int i=L-1;i<len;i++){int t=(i+1)/L-1;rf[S2[t]]+=f2[S2[i]];}
		for(int i=len-L;i>=0;i--){int t=cnt-(len-i)/L;lf[S2[t]]+=f1[S2[i]];}
		for(int i=1;i<cnt;i++)add(S2[i-1],S2[i]);add(lb,S2[0]),add(S2[cnt-1],rb);
		for(int i=0;i<cnt;i++)q.push(mk(x+1,S2[i]));tmp=0;
		for(int i=0;i<cnt;i++)(i-L+1>=0?tmp+=lf[S2[i-L+1]]:0),res-=rf[S2[i]]*tmp;
	}else r[lb]=n+1,l[rb]=0;S2.clear();
	return res;
}
int main(){
//	freopen("std.in","r",stdin);
//	freopen("std.out","w",stdout);
	n=read(),L=read();
	Rep(i,1,n){int x=read();q.push(mk(x,i)),add(i,i+1),lf[i]=rf[i]=1;}
	add(0,1);ll ans=0;
	for(;!q.empty();){
		int x=q.top().fir;S1.clear();
		for(;!q.empty()&&q.top().fir==x;q.pop())S1.push_back(q.top().sec);
		S2.clear();S2.push_back(S1[0]);
		for(int i=1,len=S1.size();i<len;i++){if(r[S1[i-1]]!=S1[i])ans+=Solve(x);S2.push_back(S1[i]);}
		ans+=Solve(x);
	}cout<<ans+n<<'\n';
	return 0;
}


