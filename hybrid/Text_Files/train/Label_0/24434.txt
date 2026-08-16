// do a test
using namespace std;
#include <bits/stdc++.h>
#define N 25005
#define M 100005
int n,m;
int a[N];
int lmin[N],rmax[N];
int suc[N][2],pre[N][2];
int ans;
void work(int l,int r){
	for (int i=l;i<=r;++i){
		for (int &j=rmax[i];j<=r;++j)
			if (a[j]>a[i]){
				int &t=suc[i][0];
				if (a[j]<a[t])
					ans+=(pre[j][1]==i)-(pre[t][1]==i),t=j;
			}
			else{
				int &t=pre[i][0];
				if (a[j]>a[t])
					ans+=(suc[j][1]==i)-(suc[t][1]==i),t=j;
			}
		for (int &j=lmin[i];j>=l;--j)
			if (a[j]>a[i]){
				int &t=suc[i][1];
				if (a[j]<a[t])
					ans+=(pre[j][0]==i)-(pre[t][0]==i),t=j;
			}
			else{
				int &t=pre[i][1];
				if (a[j]>a[t])
					ans+=(suc[j][0]==i)-(suc[t][0]==i),t=j;
			}
	}
}
int main(){
	scanf("%d%d",&n,&m);
	for (int i=1;i<=n;++i)
		scanf("%d",&a[i]);
	a[0]=n+1,a[n+1]=0;
	for (int i=1;i<=n;++i){
		lmin[i]=i-1,rmax[i]=i+1;
		suc[i][0]=suc[i][0]=0;
		pre[i][0]=pre[i][1]=n+1;
	}
	for (int i=1;i<=m;++i){
		int l,r;
		scanf("%d%d",&l,&r);
		work(l,r);
		printf("%d\n",ans);
	}
	return 0;
}