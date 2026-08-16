//ios::sync_with_stdio(false);
#include<bits/stdc++.h>
#define LL long long
#define F(x,y,z) for(int x=y;x<=z;++x)
#define D(x,y,z) for(int x=y;x>=z;--x)
#define ckmax(a,b) (a)=max(a,b)
#define ckmin(a,b) (a)=min(a,b)
#define pb push_back
using namespace std;
const int N=100010;
LL R(){
    LL ans=0,f=1;char c=getchar();
    for(;c<'0'||c>'9';c=getchar()) if (c=='-') f=-1;
    for(;c>='0'&&c<='9';c=getchar()) ans=ans*10+c-'0';
    return ans*f;
}
int n,fa[N],siz[N];
vector<int> v[N];
LL d[N],s,g[N];
map<LL,int> ys,id;
void Err(){
	printf("-1\n");
	exit(0);
}
void dfs(int u,int dep){
	s+=dep;
	for(auto to:v[u])dfs(to,dep+1);
}
int main(){
	//freopen("1.in","r",stdin);freopen("1.out","w",stdout);
	n=R();
	F(i,1,n)d[i]=R(),siz[i]=1,id[d[i]]=i;
	sort(d+1,d+1+n);
	F(i,1,n)ys[d[i]]=i;
	D(i,n,2){
		fa[i]=ys[d[i]+siz[i]*2-n];
		if(fa[i]==0)Err();
		v[fa[i]].pb(i);
		siz[fa[i]]+=siz[i];
	}
	dfs(1,0);
	if(s!=d[1])Err();
	F(i,2,n)printf("%d %d\n",id[d[i]],id[d[fa[i]]]);
    return 0;
}