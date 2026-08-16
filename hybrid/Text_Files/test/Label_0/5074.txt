#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#define INF 1000000000000
using namespace std;
typedef long long ll;

struct edge{int to; ll cap; int rev;};

vector<edge> g[310];
bool used[310];

void add_edge(int from, int to, ll cap){
    g[from].push_back((edge){to,cap,(int)g[to].size()});
    g[to].push_back((edge){from,0,(int)g[from].size()-1});
}

ll dfs(int v,int t,ll f){
    if(v==t){
        return f;
    }
    used[v]=true;
    for(int i=0;i<g[v].size();i++){
        edge &e=g[v][i];
        if(!used[e.to]&&e.cap>0){
            ll d=dfs(e.to,t,min(f,e.cap));
            if(d>0){
                e.cap-=d;
                g[e.to][e.rev].cap+=d;
                return d;
            }
        }
    }
    return 0;
}

ll max_flow(int s,int t){
    ll flow=0;
    for(;;){
        memset(used,0,sizeof(used));
        int f=dfs(s,t,INF);
        if(f==0) return flow;
        flow+=f;
    }
}

int main(){
    int n;
    ll a,ans=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%lld",&a);
        if(a<=0){
            add_edge(0,i+1,-a);
        }
        else{
            add_edge(i+1,n+1,a);
            ans+=a;
        }
        for(int j=2*(i+1);j<=n;j+=i+1){
            add_edge(i+1,j,INF);
        }
    }
    printf("%lld\n",ans-max_flow(0,n+1));
}