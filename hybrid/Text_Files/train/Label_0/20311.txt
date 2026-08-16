#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;
const int maxn = 2e5+5;
vector<int> mp[maxn]; int a[maxn];
map<int,int> num;
map<int,int> * hush[maxn]; int sz[maxn];
int ans , fr , fpa; bool tag[maxn];
bool dfs(int id,int pa)
{
	if(id==0) return true;
	int son = 0; sz[id] = 1;
	for(int i=0;i<mp[id].size();++i)
	{
		int to = mp[id][i]; if(to==pa) continue;
		bool res = dfs(to,id); 
		if(!res) return false;
		sz[id] += sz[to];
		if( sz[to] > sz[son] ) son = to;
	}
	if(son) hush[id] = hush[son]; else hush[id] = new map<int,int>();
	++(  ( *hush[id] )[ a[id] ]  );
	int cid = 0 , cnum = 0;
	if( ( *hush[id] )[ a[id] ]  >= 2 ) cid = son , ++cnum;
	for(int i=0;i<mp[id].size();++i)
	{
		int to = mp[id][i]; if(to==pa || to==son) continue;
		for( auto ele : (*hush[to]) ) ( *hush[ id ] ) [ ele.first ] += ele.second;
		if( ( *hush[to] )[ a[id] ]  >= 1 ) cid = to , ++cnum;
		hush[to]->clear();
	}
	
	// 下面的点是否合法 
	int cnt = ( *hush[id] )[ a[id] ]; if( cnt < num[ a[id] ] ) tag[id] = true;
	
	// 上面的点是否合法 
	if( cnum>=2 || ( cnum == 1 && tag[id] ) ) { ans = -1; return false; }
	else if(cnum>=1) 
	{
		if(fpa) { ans = -1; return false; }
		fr = cid , fpa = id; ans = 0; 
		return false; 
	}
	
	return true;
}
void dfs2(int id,int pa)
{
	if(tag[id]) return ;
	++ans;
	for(int i=0;i<mp[id].size();++i)
	{
		int to = mp[id][i]; if(to==pa) continue;
		dfs2(to,id);
	}
}
int n; 
void mem()
{
	for(int i=1;i<=n;++i) 
	{
		if(hush[i]!=NULL) hush[i]->clear();
		sz[i] = 0;
	}
}
int main()
{
	scanf("%d",&n);
	for(int i=1;i<=n;++i) scanf("%d",&a[i]) , ++num[ a[i] ] ; 
	for(int i=1,u,v;i<n;++i) scanf("%d%d",&u,&v) , mp[u].push_back(v) , mp[v].push_back(u);
	ans = 0; fr = 1 , fpa = 0; dfs(1,0); 
	if(ans==-1) ans = 0; else
	{
		mem() ;
		dfs(fpa,fr); 
		if(ans==-1) ans = 0; else  dfs2(fr,fpa);
	}
	printf("%d",ans);
	return 0;
}