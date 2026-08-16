#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ff first
#define ss second

const int MX=200000+10;

int V[MX], S[MX], a[555][555], vis[MX], T, K;
vector<int>g[MX];

void dfs(int id, int n)
{
    K=max(K, id);

    vector<int>v;
    for(int i=1; i<=n; i++)
    {
        if(vis[i]==id) v.push_back(i);
    }

    int mx=0, x=v[0];
    for(auto xx:v)
    {
        if(vis[xx]==id) mx=max(mx, a[x][xx]);
    }

    S[id]=mx;

    vector<int>child, v2;
    while(v.size())
    {
        v2=v; v.clear();
        int cn=0, p=v2[0]; ++T;
        for(auto q:v2)
        {
            if(a[p][q]!=mx) cn++, vis[q]=T;
            else            v.push_back(q);
        }
        if(cn==1)
        {
            g[id].push_back(p); T--;
            vis[p]=p;
        }
        else      g[id].push_back(T), child.push_back(T);
    }
    for(auto x:child) dfs(x, n);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);


    int n; cin>>n;
    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++) cin>>a[i][j];
    }

    for(int i=1; i<=n; vis[i]=n+1, i++) V[i]=i, S[i]=a[i][i];

    T=n+1;
    dfs(T, n);

    cout<<K<<endl;
    for(int i=1; i<=K; i++) cout<<S[i]<<' ';
    cout<<endl;
    cout<<n+1<<endl;
    for(int i=1; i<=K; i++)
    {
        if(g[i].size())
        {
            for(auto x:g[i])
            {
                cout<<x<<' '<<i<<endl;
            }
        }
    }
    return 0;
}
