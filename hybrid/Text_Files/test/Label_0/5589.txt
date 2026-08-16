#include <bits/stdc++.h>

using namespace std;

int niz[300050];
vector<int> adj[300050];
int comp[300050];
int ind[100050];


void dfs(int x,int k)
{
    comp[x]=k;
    for(auto y:adj[x])
        if(!comp[y])
            dfs(y,k);
}

int main()
{
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++)
       {
            cin>>niz[i];
            ind[niz[i]]=i;
       }
    for(int i=0;i<m;i++)
    {
        int x,y;
        cin>>x>>y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }


    int br_komp=0;
    for(int i=1;i<=n;i++){
        if(comp[i]==0){
            br_komp++;
            dfs(i,br_komp);
        }
    }
    int res=0;
    for(int i=1;i<=n;i++)if(comp[i]==comp[ind[i]])res++;
    cout<<res;
    return 0;
}
