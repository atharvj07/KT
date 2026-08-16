#include <bits/stdc++.h>
#define ll long long
#define maxn 100005
int n,k,a[maxn];
ll sum[maxn],pst[maxn],ans;
int main(){
	scanf("%d%d",&n,&k);
	for(int i=1;i<=n;++i)scanf("%d",&a[i]);
	for(int i=1;i<=n;++i){
		sum[i]=sum[i-1]+a[i];
		pst[i]=pst[i-1]+std::max(a[i],0);
	}
	for(int l=1;l<=n-k+1;++l){
		int r=l+k-1;
		ans=std::max(ans,pst[l-1]+pst[n]-pst[r]);
		ans=std::max(ans,pst[l-1]+sum[r]-sum[l-1]+pst[n]-pst[r]);
	}printf("%lld",ans);
	return 0;
}