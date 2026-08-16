#include<bits/stdc++.h>
#define fi first
#define se second
#define pii pair<int,int>
#define mp make_pair
#define tp tuple<int,int,int>
#define mtp make_tuple
using namespace std;

const int N=2e5+5;
int n,a[N],res[N],m,e[N],f[N];
vector<int>adj[N];

void dfs(int u,int p=-1)
{
    int prem=m;
    f[u]=lower_bound(e+1,e+m+1,a[u])-e;
    if(f[u]>m) m++;
    int pref=e[f[u]];
    e[f[u]]=a[u];
    res[u]=m;
    for(auto&v:adj[u])
    {
        if(v==p) continue;
        dfs(v,u);
    }
    m=prem;
    e[f[u]]=pref;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<n;i++)
    {
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    dfs(1);
    for(int i=1;i<=n;i++) cout<<res[i]<<'\n';
}
