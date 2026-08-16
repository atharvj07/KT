#include <bits/stdc++.h>
#define MOD 1000000007LL
using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int n,m;
vector<int> G[1005];
vector<int> rG[1005];
bool used[1005];
int gr[1005];
int cnt[10000];

void dfs2(int v,int g){
	int su=0;
	for(int i=0;i<G[v].size();i++){
		su^=gr[G[v][i]];
	}
	cnt[g^su]++;
	for(int i=0;i<G[v].size();i++){
		dfs2(G[v][i],su^gr[G[v][i]]^g);
	}
}

int dfs(int v){
	used[v]=true;
	if(G[v].size()==0)return gr[v]=1;
	int su=0;
	for(int i=0;i<G[v].size();i++){
		if(!used[G[v][i]]){
			su^=dfs(G[v][i]);
		}
	}
	memset(cnt,0,sizeof(cnt));
	cnt[su]++;
	//printf("v=%d %d\n",v,su);
	for(int i=0;i<G[v].size();i++){
		dfs2(G[v][i],su^gr[G[v][i]]);
	}
	int val=0;
	while(cnt[val]>0){
		val++;
	}
	return (gr[v]=val);
}

int main(void){
	scanf("%d%d",&n,&m);
	for(int i=0;i<m;i++){
		int a;
		scanf("%d",&a);
		a--;
		G[a].push_back(i);
		rG[i].push_back(a);
	}
	int ans=0;
	for(int i=0;i<n;i++){
		if(rG[i].size()==0){
			int md=dfs(i);
			ans^=md;
			//printf("%d %d\n",i,md);
		}
	}
	printf("%s\n",ans==0?"Bob":"Alice");
	return 0;
}

