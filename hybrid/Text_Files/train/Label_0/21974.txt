#include <bits/stdc++.h>
#define ll long long
using namespace std;
struct state
{
	ll s;
	int v,len;
};
struct comp{
bool operator()(state a,state b)
{
	return a.len>b.len;
}};
priority_queue<state,vector<state>,comp> que;
int n,m,c[50],ans;
vector<int> G[50];
map<ll,int> d[50];
ll mask[50];
inline void add_edge(int f,int t)
{
	G[f].push_back(t);
	G[t].push_back(f);
}
int main()
{
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++)
	scanf("%d",&c[i]);
	for(int i=1,a,b;i<=m;i++)
	{
		scanf("%d%d",&a,&b);
		add_edge(a,b);
		mask[a]|=1LL<<b;
		mask[b]|=1LL<<a;
	}
	for(int i=1;i<=n;i++)
	{
		mask[i]|=1LL<<i;
		if(mask[1]&(1LL<<i)) ans+=c[i];
	}
	que.push((state){mask[1],1,ans});
	d[1][mask[1]]=ans;
	while(!que.empty())
	{
		state S=que.top(); que.pop();
		if(S.v==n) {printf("%d\n",S.len); return 0;}
		for(int i=0;i<G[S.v].size();i++)
		{
		    state New=(state){0,0,0};	
		    New.v=G[S.v][i];
			New.s=S.s|mask[New.v];
			for(int j=1;j<=n;j++)
			if(New.s&(1LL<<j)) New.len+=c[j];
			if(d[New.v].find(New.s)==d[New.v].end() || d[New.v][New.s]>New.len) que.push(New),d[New.v][New.s]=New.len;
		}
	 } 
	return 0;
}