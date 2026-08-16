#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <climits>

#define all(c) (c).begin(), (c).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const int INF=100000000;
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
using namespace std;
typedef pair<int ,int > P;
typedef long long ll;

template<typename T>
inline bool chmin(T &a,const T &b) {
    if(a>b) {
        a=b;
        return true;
    }
    return false;
}

struct Edge{
    int to,cost;
    Edge(int to,int cost):to(to),cost(cost){}
    Edge(){}
};
struct State{
    int v;
    int r;
    int bit;
    int cost;
    State(int v,int r,int bit,int cost) :
        v(v),r(r),bit(bit),cost(cost){}
    State(){}
    bool operator<(const State &rth) const {
        return this->cost>rth.cost;
    }
};
struct Event{
    int a,b,c;
    Event(int a,int b,int c):a(a),b(b),c(c){}
    Event(){}
};
vector<Edge> G[102];
Event event[10];
// ??????,??£?¶?????????§?§????,????????????????????????
int dp[102][102][1<<8];
int n,m,E,S,T,R;
int func(int v) {
    rep(i,E) {
        if(event[i].c==v) return i;
    }
    return INF;
}
int init_bit() {
    int idx=func(S);
    if(idx!=INF) return 1<<idx;
    return 0;
}
int dijk() {
    rep(i,102) rep(j,102) rep(k,1<<8) dp[i][j][k]=INF;
    
    dp[S][0][init_bit()]=0;

    priority_queue<State,vector<State> >que;
    que.push(State(S,0,init_bit(),0));
    while(que.size()) {
        State s=que.top(); que.pop();
        // printf("%d %d %d %d\n",s.v,s.r,s.bit,s.cost);
        if(s.v==T) break;
        int now=dp[s.v][s.r][s.bit];
        //if(now<s.cost) continue;
        if(s.r==R) {
            if(chmin(dp[S][0][s.bit],now+1)) {
                que.push(State(S,0,s.bit,now+1));
            }
        }
        else {
            if(chmin(dp[S][0][s.bit],now+1)) {
                que.push(State(S,0,s.bit,now+1));
            }
            rep(i,G[s.v].size()) {
                Edge e=G[s.v][i];

                int idx=func(e.to);
                int bit=s.bit;
                if(idx!=INF) bit|=1<<idx;
                if(chmin(dp[e.to][s.r+1][bit],now+1)) {
                    que.push(State(e.to,s.r+1,bit,now+1));
                }
            }
            rep(i,E) {
                if((s.bit>>i)&1) {
                    if(event[i].a==s.v) {
                        int to=event[i].b;
                        int idx=func(to);
                        int bit=s.bit;
                        if(idx!=INF) bit|=1<<idx;
                        if(chmin(dp[to][s.r+1][bit],now+1)) {
                            que.push(State(to,s.r+1,bit,now+1));
                        }
                    }
                    if(event[i].b==s.v) {
                        int to=event[i].a;
                        int idx=func(to);
                        int bit=s.bit;
                        if(idx!=INF) bit|=1<<idx;
                        if(chmin(dp[to][s.r+1][bit],now+1)) {
                            que.push(State(to,s.r+1,bit,now+1));
                        }
                    }
                }
            }
        }
    }

    int res=INF;
    rep(r,R+1) rep(k,1<<E) res=min(res,dp[T][r][k]);
    return res;
}
int main() {
    cin>>n>>m>>E>>S>>T>>R;
    rep(i,m) {
        int a,b;
        cin>>a>>b;
        G[a].pb(Edge(b,1));
        G[b].pb(Edge(a,1));
    }
    rep(i,E) {
        int a,b,c;
        cin>>a>>b>>c;
        event[i]=Event(a,b,c);
    }
    int ans=dijk();
    if(ans==INF) ans=-1;
    cout<<ans<<endl;
    return 0;
}