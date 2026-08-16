#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

#define CIN_ONLY if(1)
struct cww{cww(){
    CIN_ONLY{
        ios::sync_with_stdio(false);cin.tie(0);
    }
}}star;
#define fin "\n"
#define FOR(i,bg,ed) for(int i=(bg);i<(ed);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define fi first
#define se second
#define pb push_back
#define DEBUG if(0)
#define REC(ret, ...) std::function<ret (__VA_ARGS__)>
template <typename T>inline bool chmin(T &l,T r)
{bool a=l>r;if(a)l=r;return a;}
template <typename T>inline bool chmax(T &l,T r)
{bool a=l<r;if(a)l=r;return a;}
template <typename T>
istream& operator>>(istream &is,vector<T> &v){
    for(auto &it:v)is>>it;
    return is;
}
typedef vector<int> V;
typedef vector<V> VV;
typedef VV Graph;
typedef pair<int,int> P;

int pp[22][312345];
int s[612345];

void euler_tour(int v,Graph &C,vector<P>& seg,int &cnt){
    int pt=0;
    s[pt++]=-1;
    s[pt++]=1;
    while(pt){
        int vv=s[--pt];
        int v=abs(vv)-1;
        if(vv>0){
            seg[v].fi=cnt++;
            for(auto &u:C[v])
                if(u!=pp[0][v]){
                    s[pt++]=-u-1;
                    s[pt++]=u+1;
                }
        }
        else
            seg[v].se=cnt++;   
    }
}

//lca?????????
void build_PP(int N){
    for(int k = 0,f=1;f; k++){
	f=0;
	for(int i = 0; i < N; i++){
	    if(pp[k][i]<0)pp[k+1][i]=-1;
	    else {pp[k+1][i]=pp[k][pp[k][i]];f=1;}
	}
    }
}

int lca(int u,int v,V& D){
    if(D[u] > D[v])swap(u,v);
    for(int k = 0,d;(d=D[v]-D[u]); k++)if((d >> k) & 1)v=pp[k][v];
    if(u==v)return v;
    for(int k = 21; k >=0 ; k--){
	if(pp[k][u]!=pp[k][v]){
	    u=pp[k][u];
	    v=pp[k][v];
	}
    }
    return pp[0][u];
}

void dfs(int v,Graph &g,V &d){
    int pt=0;
    s[pt++]=v;
    while(pt){
        int v=s[--pt];
        for(auto &u:g[v])
            if(pp[0][v]!=u){
                d[u]=d[v]+1;
                pp[0][u]=v;
                s[pt++]=u;
            }
    }
}
#define BITTYPE long long 
#define BITCNT  2
#define BITSIZE 6123456
namespace _BIT{
    int i=0;
    BITTYPE t[2][BITSIZE];
    inline BITTYPE* get(){
        return t[i++];
    }
}

struct BIT{
    using T=BITTYPE;
    T *t;
    int n;
    BIT(int N):t(_BIT::get()),n(N+1){
        REP(i,n+1)t[i]=0;
    }
    void add(int r,T v){//add v for [1,r]
        for(;r;r-=r&-r)t[r]+=v;
    }
    void add(int l,int r,T v){//add v for [l,r]
        add(r,v);
        add(l-1,-v);
    }
    T get(int i){//get sum[i]
        T res=0;
        for(;i<=n;i+=i&-i)res+=t[i];
        return res;
    }
};

int main(){
    int N,Q;
    cin>>N>>Q;
    Graph g(N);
    REP(i,N-1){
        int a,b;
        cin>>a>>b;
        g[a].pb(b);
        g[b].pb(a);
    }
    V d(N,0);
    REP(i,22)REP(j,N)pp[i][j]=-1;
    dfs(0,g,d);
    build_PP(N);
    vector<P> seg(N);
    int M=1;
    euler_tour(0,g,seg,M);
    BIT latte(M+10);
    BIT malta(M+10);
    REP(q,Q){
        int type,x,y;
        cin>>type>>x>>y;
        if(type==0){
            int camy=lca(x,y,d);
            LL A=latte.get(seg[x].fi)*d[x]+malta.get(seg[x].fi);
            LL B=latte.get(seg[y].fi)*d[y]+malta.get(seg[y].fi);
            LL C=latte.get(seg[camy].fi)*d[camy]+malta.get(seg[camy].fi);
            //cout<<A<<" "<<B<<" "<<C<<endl;
            cout<<A+B-2*C<<endl;
        }
        else{
            LL luz=y;
            LL izr=-y*d[x];
            latte.add(seg[x].fi,seg[x].se,luz);
            malta.add(seg[x].fi,seg[x].se,izr);

        }
    }
    return 0;
}