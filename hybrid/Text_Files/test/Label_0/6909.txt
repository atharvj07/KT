#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;
#define foreach(i,v) for(int i=0;i<(int)v.size();i++)

const int N=55;
const int dx[]={0,1,0,-1};
const int dy[]={1,0,-1,0};
char mz[N][N];
int con[N][N],on[N][N],off[N][N];
int pre[N][N],dis[N][N];
int tl[N*N];
struct point
{
    int x,y;
    point(){}
    point(int _x,int _y)
    :x(_x),y(_y){}
};
point task[1010];
vector<int> load;
queue<point> q;
int n,m;
void bfs(int sx,int sy,int ex,int ey)
{
    while(!q.empty()) q.pop();
    memset(pre,-1,sizeof(pre));
    memset(dis,-1,sizeof(dis));
    dis[sx][sy]=0;
    q.push(point(sx,sy));
    while(!q.empty())
    {
        point u=q.front(); q.pop();
        int x=u.x, y=u.y;
        if(x==ex && y==ey) break;
        for(int d=0;d<4;d++)
        {
            int nx=x+dx[d], ny=y+dy[d];
            if(nx<0 || nx>=n || ny<0 || ny>=m) continue;
            if(dis[nx][ny]!=-1 || mz[nx][ny]=='#') continue;
            dis[nx][ny]=dis[x][y]+1;
            pre[nx][ny]=x*m+y;
            q.push(point(nx,ny));
        }
    }
    int ntl=0;
    for(int x=ex,y=ey;pre[x][y]!=-1;)
    {
        int t=pre[x][y];
        tl[ntl++]=t;
        x=t/m; y=t%m;
    }
    for(int i=ntl-1;i>=0;i--) load.push_back(tl[i]);
}
int main()
{
//freopen("in.txt","r",stdin);
    int q;
    while(~scanf("%d%d%d",&n,&m,&q))
    {
        for(int i=0;i<n;i++) scanf("%s",mz[i]);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++) scanf("%d",&con[i][j]);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++) scanf("%d",&on[i][j]);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++) scanf("%d",&off[i][j]);
        for(int i=0;i<q;i++) scanf("%d%d",&task[i].x,&task[i].y);
        load.clear();
        for(int i=1;i<q;i++) bfs(task[i-1].x,task[i-1].y,task[i].x,task[i].y);
        load.push_back(task[q-1].x*m+task[q-1].y);
        memset(pre,-1,sizeof(pre));
        int ans=0;
        foreach(i,load)
        {
            int l=load[i];
            int x=l/m, y=l%m;
            if(pre[x][y]==-1)
            {
                ans+=on[x][y];
                ans+=off[x][y];
            }
            else
            {
                int tmp=(i-pre[x][y])*con[x][y];
                tmp=min(on[x][y]+off[x][y],tmp);
                ans+=tmp;
            }
            pre[x][y]=i;
        }
        printf("%d\n",ans);
    }
    return 0;
}