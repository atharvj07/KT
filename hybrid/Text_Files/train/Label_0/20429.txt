#include<bits/stdc++.h>
using namespace std;
const int N=3005;
int n,tot,a[N],lnk[N],son[N<<1],nxt[N<<1]; bool win[N];
void add(int x,int y) {
	nxt[++tot]=lnk[x],lnk[x]=tot,son[tot]=y;
}
void dfs(int x,int p) {
	win[x]=0;
	for (int j=lnk[x]; j; j=nxt[j]) {
		if (son[j]==p) continue;
		if (a[x]>a[son[j]]) {
			dfs(son[j],x);
			if (!win[son[j]]) win[x]=1;
		}
	}
}
int main() {
	scanf("%d",&n);
	for (int i=1; i<=n; i++) scanf("%d",&a[i]);
	for (int i=1,x,y; i<n; i++) {
		scanf("%d%d",&x,&y);
		add(x,y),add(y,x);
	}
	for (int i=1; i<=n; i++) {
		dfs(i,0);
		if (win[i]) printf("%d ",i);
	}
	return 0;
}