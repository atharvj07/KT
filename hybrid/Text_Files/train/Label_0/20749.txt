#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<queue>
using namespace std;
const int N=2e5+10;
struct Tree
{
    struct edge{int next,to;}a[N<<1];
    int head[N],cnt;
    void link(int x,int y)
        {
            a[++cnt]=(edge){head[x],y};head[x]=cnt;
            a[++cnt]=(edge){head[y],x};head[y]=cnt;
        }
}A,B;
int n,p1,p2,dep[N],dis[N],fr[N],vis[N],ans;
queue<int> Q;
void bfs1()
{
    memset(dis,-1,sizeof(dis));
    if(dep[p1]) Q.push(p1);dis[p1]=0;
    while(!Q.empty())
    {
        int x=Q.front();Q.pop();vis[x]=1;
        for(int i=A.head[x];i;i=A.a[i].next)
        {
            int R=A.a[i].to;
            if(dis[R]==-1)
            {
                dis[R]=dis[x]+1;
                if(dis[R]<dep[R]) Q.push(R);
                else if(dis[R]==dis[R]) vis[R]=1;
            }
        }
    }
}
void bfs2()
{
    memset(dep,-1,sizeof(dep));
    Q.push(p2);dep[p2]=0;
    while(!Q.empty())
    {
        int x=Q.front();Q.pop();
        for(int i=B.head[x];i;i=B.a[i].next)
        {
            int R=B.a[i].to;
            if(dep[R]==-1) dep[R]=dep[x]+1,fr[R]=x,Q.push(R);
        }
    }
}
int Dis(int x,int y)
{
    if(dep[x]<dep[y]) swap(x,y);
    if(fr[x]==fr[y]||x==y||fr[x]==y) return 0;
    if(fr[fr[x]]==y) return 0;
    return 1;
}
int main()
{
    cin>>n>>p1>>p2;
    for(int i=1,x,y;i<n;i++) scanf("%d%d",&x,&y),A.link(x,y);
    for(int i=1,x,y;i<n;i++) scanf("%d%d",&x,&y),B.link(x,y);
    bfs2();bfs1();
    for(int x=1;x<=n;x++)
        for(int i=A.head[x];i;i=A.a[i].next)
            if(vis[x]&&vis[A.a[i].to]&&Dis(x,A.a[i].to))
                puts("-1"),exit(0);
    for(int i=1;i<=n;i++) if(vis[i]) ans=max(dep[i],ans);
    cout<<ans*2<<endl;
}
