#include<cstdio>
#include<vector>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int d[1500][1500];

int N,deg[1500];
void solve(int root,vector<int> V){
	int n=V.size();
	if(V.empty()) return;

	// root と u を両端とする列を作る
	// 残りの頂点は root-u 間にある d[root][u]+1 個の頂点のどれかにぶら下がる
	int u=V[0];
	vector<int> ch[32];
	for(int i=1;i<V.size();i++){
		int v=V[i];
		ch[(d[root][u]+d[root][v]-d[u][v])/2].push_back(v);
	}

	// 列の各頂点を根にして, 再帰的に木の形を求める
	int par;
	rep(i,d[root][u]+1){
		int v; // 次の根
		if(i==0){
			v=root;
		}
		else if(i==d[root][u]){
			v=u;
		}
		else{
			v=N++;
			rep(j,ch[i].size()){
				int w=ch[i][j];
				d[v][w]=d[w][v]=d[root][w]-i;
			}
		}

		if(i!=0){
			deg[par]++;
			deg[ v ]++;
		}

		solve(v,ch[i]);

		par=v;
	}
}

int main(){
	for(int n;scanf("%d",&n),n;){
		rep(u,n) rep(v,n) scanf("%d",d[u]+v);

		vector<int> V;
		rep(i,n-1) V.push_back(i+1);
		N=n;
		rep(u,1500) deg[u]=0;
		solve(0,V);

		vector<int> ans(deg+n,deg+N);
		sort(ans.begin(),ans.end());
		rep(i,ans.size()) printf("%d%c",ans[i],i+1<ans.size()?' ':'\n');
	}

	return 0;
}