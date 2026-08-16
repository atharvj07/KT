#include<cstdio>
#include<vector>
using namespace std;
int n;
const int MAXN=1e5+5;
vector<int>G[MAXN];
int dist[2][MAXN];
void dfs(int v,int p,int id,int t){
	dist[id][v]=t;
	for(int i=0;i<G[v].size();i++){
		int to=G[v][i];
		if(to!=p){
			dfs(to,v,id,t+1);
		}
	}
}
int main(){
	scanf("%d",&n);
	for(int i=0;i<n-1;i++){
		int a,b;
		scanf("%d%d",&a,&b);
		a--;b--;
		G[a].push_back(b);
		G[b].push_back(a);
	}
	dfs(0,0,0,0);
	dfs(n-1,n-1,1,0);
//	for(int i=0;i<n;i++)printf("%d ",dist[0][i]);printf("\n");
//	for(int i=0;i<n;i++)printf("%d ",dist[1][i]);printf("\n");
	int n1=0,n2=0;
	for(int i=0;i<n;i++){
		if(dist[0][i]<=dist[1][i])n1++;
		else n2++;
	}
//	printf("%d %d\n",n1,n2);
	if(n1>n2)printf("Fennec\n");
	else printf("Snuke\n");
	return 0;
}