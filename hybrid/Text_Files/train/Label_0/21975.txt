#include <bits/stdc++.h>
#define int long long
#define INF 1000000007
using namespace std;

int n,m,a[50],ans=INF;
vector<int> v[50];

inline void dfs(int loc,int mask1,int cost)
{
	int mask2=mask1;
	if(!((mask1>>loc)&1ll)){
		cost+=a[loc];
		mask1|=(1ll<<(loc));
	}
	for(int i=0;i<v[loc].size();i++){
		if(!(mask1&(1ll<<(v[loc][i])))){
			cost+=a[v[loc][i]];
			mask1|=(1ll<<(v[loc][i]));
		}
	}
	if(cost>=ans) return;
	if(loc==n-1){
		ans=cost;
		return;
	}
	for(int i=0;i<v[loc].size();i++){
		if(!(mask2&(1ll<<(v[loc][i])))){
			dfs(v[loc][i],mask1,cost);
		}
	}
}

signed main()
{
	ios::sync_with_stdio(false);
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	for(int i=0;i<m;i++){
		int x,y;
		cin>>x>>y;
		x--;y--;
		v[x].push_back(y);
		v[y].push_back(x);
	}
	dfs(0,0,0);
	cout<<ans<<endl;
	return 0;
}
