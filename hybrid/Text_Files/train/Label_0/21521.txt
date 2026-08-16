#include <bits/stdc++.h>
using namespace std;
const long long INF=1LL<<60;
const int MAXN=1005;
int n, m, S1, S2, T;
char s[100];
struct edge{
    int to;
    long long w;
    bool type;
    edge(int to=0, long long w=0, bool type=false):to(to),w(w),type(type) {}
};
vector<edge> G[MAXN];
long long dist[MAXN][MAXN];
priority_queue< pair<long long, pair<int, int> > > q;
pair<long long, pair<int, int> > now;
vector<long long> ans;
long long cross(long long a1, long long b1, long long a2, long long b2){
    if(a1==INF||a2==INF) return 0;
    return floor((a1-a2+1.0)/(b2-b1));
}
long long calc(long long dp[MAXN], int k, long long x){
    long long ret=INF;
    for(int i=0; i<=k; i++){
        ret=min(ret,dp[i]+x*i);
    }
    return ret;
}
int main(){
    while(~scanf("%d%d%d%d%d",&n,&m,&S1,&S2,&T)&&n){
        for(int i=1; i<=n; i++){
            G[i].clear();
        }
        int k=0;
        for(int i=0, x, y, z; i<m; i++){
            scanf("%d%d%s",&x,&y,s);
            if(s[0]=='x'){
                G[x].push_back(edge(y,0,1));
                G[y].push_back(edge(x,0,1));
                k++;
            }
            else{
                sscanf(s,"%d",&z);
                G[x].push_back(edge(y,z,0));
                G[y].push_back(edge(x,z,0));
            }
        }
        for(int i=1; i<=n; i++){
            for(int j=0; j<=k; j++){
                dist[i][j]=INF;
            }
        }
        dist[T][0]=0;
        while(!q.empty()) q.pop();
        q.push(make_pair(0LL,make_pair(T,0)));
        while(!q.empty()){
            now=q.top(); q.pop();
            int u=now.second.first, cnt=now.second.second;
            long long d=dist[u][cnt];
            if(-now.first>d) continue;
            for(auto p: G[u]){
                int ncnt=cnt+p.type, nidx=p.to;
                long long ndist=d+p.w;
                if(ncnt<=k&&ndist<dist[nidx][ncnt]){
                    dist[nidx][ncnt]=ndist;
                    q.push(make_pair(-ndist,make_pair(nidx,ncnt)));
                }
            }
        }
        ans.clear();
        ans.push_back(0LL);
        for(int i=0; i<=k; i++){
            for(int j=0; j<=k; j++) if(i!=j){
                long long x1, x2, x3;
                x1=cross(dist[S1][i],i,dist[S2][j],j);
                x2=cross(dist[S1][i],i,dist[S1][j],j);
                x3=cross(dist[S2][i],i,dist[S2][j],j);
                for(int d=-1; d<=1; d++){
                    ans.push_back(x1+d);
                    ans.push_back(x2+d);
                    ans.push_back(x3+d);
                }
            }
        }
        sort(ans.begin(),ans.end());
        ans.erase(unique(ans.begin(),ans.end()),ans.end());
        long long ret=INF;
        for(auto p: ans){
            if(p>=0){
                ret=min(ret,abs(calc(dist[S1],k,p)-calc(dist[S2],k,p)));
            }
        }
        printf("%lld\n",ret);
    }
    return 0;
}