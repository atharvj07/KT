#include <cstdio>
#define Maxn 200000
int head[Maxn+5],arrive[Maxn<<1|5],nxt[Maxn<<1|5],tot;
void add_edge(int from,int to){
	arrive[++tot]=to;
	nxt[tot]=head[from];
	head[from]=tot;
}
int dep[Maxn+5];
int n;
int s,t;
void dfs(int u,int fa){
	dep[u]=dep[fa]+1;
	for(int i=head[u];i;i=nxt[i]){
		int v=arrive[i];
		if(v==fa){
			continue;
		}
		dfs(v,u);
	}
}
int main(){
	int u,v;
	scanf("%d",&n);
	for(int i=1;i<n;i++){
		scanf("%d%d",&u,&v);
		add_edge(u,v);
		add_edge(v,u);
	}
	dfs(1,0);
	for(int i=1;i<=n;i++){
		if(dep[i]>dep[s]){
			s=i;
		}
	}
	dfs(s,0);
	for(int i=1;i<=n;i++){
		if(dep[i]>dep[t]){
			t=i;
		}
	}
	if(dep[t]%3==2){
		puts("Second");
	}
	else{
		puts("First");
	}
	return 0;
}
