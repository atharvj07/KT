#include<bits/stdc++.h>
using namespace std;
#define int long long
const int N=200010;
int size[N],Flag,cnt2[N],pp[N],cc,sd[N];
int cnt[N],col[N],n,m,ne[N],tot,fi[N],zz[N],flag[N],x,y,X,Y;
void jb(int x,int y){
	ne[++tot]=fi[x];
	fi[x]=tot;
	zz[tot]=y;
}
void dfs2(int x){
	cnt2[x]=col[x];flag[x]=1;
	for (int i=fi[x];i;i=ne[i])
		if (!flag[zz[i]]&&!pp[i]){
			dfs2(zz[i]);
			cnt2[x]+=cnt2[zz[i]];
		}
}
int solve(){
	memset(flag,0,sizeof flag);
	dfs2(1);
	int ans=0;
	for (int i=1;i<=n;i++)ans+=abs(size[i]-cnt2[i]-cnt[i]);
	return ans;
}
int check(int x){
	col[X]-=x;col[Y]+=x;
	int k=solve();
	col[X]+=x;col[Y]-=x;
	return k+abs(x);
}
void dfs(int x,int y){
	size[x]=flag[x]=1;cnt[x]=col[x];
	for (int i=fi[x];i;i=ne[i])
		if (i!=y){
			if (flag[zz[i]]&&sd[zz[i]]<sd[x]){
				X=x;cc++;
				Y=zz[i];
				Flag=(sd[x]-sd[zz[i]])&1;
				pp[i]=pp[i^1]=1;
				continue;
			}
			if (flag[zz[i]])continue;
			sd[zz[i]]=sd[x]+1;
			col[zz[i]]=col[x]^1;
			dfs(zz[i],i^1);
			cnt[x]+=cnt[zz[i]];
			size[x]+=size[zz[i]];
		}
}
signed main(){
	scanf("%lld%lld",&n,&m);
	tot=1;
	for (int i=1;i<=m;i++){
		scanf("%lld%lld",&x,&y);
		jb(x,y);jb(y,x);
	}
	col[1]=1;
	dfs(1,0);
	int S=cnt[1],T=n-cnt[1];
	if (m==n-1){
		if (S!=T){
			puts("-1");
			return 0;
		}
		printf("%lld\n",solve());
	}
	else if (Flag){
		if (S!=T){
			puts("-1");
			return 0;
		}
		int l=-n,r=n;
		while (l+5<r){
			int mid1=l+(r-l)/3,mid2=r-(r-l)/3;
			if (check(mid1)>check(mid2))l=mid1;
			else r=mid2;
		}
		int ans=1e18;
		for (int i=l;i<=r;i++)ans=min(ans,check(i));
		printf("%lld\n",ans);
	}
	else {
		if ((S&1)!=(T&1)){
			puts("-1");
			return 0;
		}
		col[X]+=(T-S)/2;
		col[Y]+=(T-S)/2;
		printf("%lld\n",solve()+abs(T-S)/2);
	}
	return 0;
}