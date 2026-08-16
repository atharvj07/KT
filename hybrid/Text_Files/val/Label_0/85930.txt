/*بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيم*/

#include <bits/stdc++.h>
using namespace std;

const int mx=1e5+5;
vector <int> edges[mx];
int cnt,level[mx],dist[mx];
bool vis[mx];
void dfs (int u,int d,int ara[])
{
    vis[u]=true;
    ara[u]=d;
    for (int v : edges[u]) {
        if (!vis[v]) dfs(v,d+1,ara);
    }
}
int main ()
{
    int i,n,a,b;

    scanf ("%d",&n);
    for (i=1;i<n;i++) {
        scanf ("%d %d",&a,&b);
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    memset(vis,0,sizeof(vis));
    dfs(1,0,level);
    memset(vis,0,sizeof(vis));
    dfs(n,0,dist);
    cnt=0;
    for (i=1;i<=n;i++) if (dist[i]<level[i]) cnt++;
    int m=n-cnt;
    if (m>cnt) printf ("Fennec\n");
    else printf("Snuke\n");

    return 0;
}
