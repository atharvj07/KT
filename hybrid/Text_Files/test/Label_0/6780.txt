#include<bits/stdc++.h>
using namespace std;

#define int long long
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define all(v) (v).begin(),(v).end()
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define fi first
#define se second
template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

namespace SCC{
    void visit(const vector<vector<int>>&G,vector<int>&vs,vector<int>&used,int v){
        used[v]=true;
        for(auto u:G[v]){
            if(!used[u])visit(G,vs,used,u);
        }
        vs.push_back(v);
    }

    void visit2(const vector<vector<int>>&T,vector<int>&used,vector<int>&comp,vector<int>&vec,int k,int v){
        comp[v]=k;
        used[v]=true;
        vec.push_back(v);

        for(auto u:T[v]){
            if(!used[u])visit2(T,used,comp,vec,k,u);
        }
    }

    //G:?????£?????????????§£???????????°??????
    //H:?????£??????????????°??????1???????????????????´?????????°??????
    //comp:G????????????????????????H?????????????±????????????????
    void decompose(const vector<vector<int>>&G,vector<vector<int>>&H,vector<int>&comp){
        vector<vector<int>>T(G.size());
        for(int i=0;i<G.size();i++){
            for(auto v:G[i]){
                T[v].push_back(i);
            }
        }
        comp.resize(G.size());

        vector<int>vs(G.size());
        vector<int>used(G.size());
        for(int i=0;i<G.size();i++){
            if(!used[i])visit(G,vs,used,i);
        }
        reverse(vs.begin(),vs.end());
        fill(used.begin(),used.end(),0);

        int K=0;
        vector<vector<int>>S;
        for(auto v:vs){
            if(!used[v]){
                S.push_back(vector<int>());
                visit2(T,used,comp,S.back(),K++,v);
            }
        }

        H.resize(K);
        fill(used.begin(),used.end(),0);
        for(int i=0;i<K;i++){
            for(auto v:S[i]){
                for(auto u:G[v]){
                    if(used[comp[u]]||comp[v]==comp[u])continue;
                    used[comp[u]]=true;
                    H[comp[v]].push_back(comp[u]);
                }
            }
            for(auto v:H[i])used[v]=false;
        }

    }
}

struct UF{
    vector<int>par,sz;
    void init(int n){
        par.resize(n);
        sz.resize(n);
        for(int i=0;i<n;i++){
            par[i]=i;
            sz[i]=1;
        }
    }
    int find(int x){
        return x==par[x]?x:par[x]=find(par[x]);
    }
    void unite(int x,int y){
        x=find(x);y=find(y);
        if(x==y)return;
        sz[x]+=sz[y];
        par[y]=x;
    }
    bool same(int x,int y){
        return find(x)==find(y);
    }
    int size(int x){
        return sz[find(x)];
    }
};

vector<vint>G;
vector<pair<int, int> > bridge;
int ord[1000], low[1000];
bool vis[1000];

void dfs(int v, int p, int &k)
{
	vis[v] = true;

	ord[v] = k++;
	low[v] = ord[v];

	for (int i = 0; i < G[v].size(); i++){
		if (!vis[G[v][i]]){
			dfs(G[v][i], v, k);
			low[v] = min(low[v], low[G[v][i]]);
			if (ord[v] < low[G[v][i]]) bridge.push_back(make_pair(min(v, G[v][i]), max(v, G[v][i])));
		}
		else if (G[v][i] != p){
			low[v] = min(low[v], ord[G[v][i]]);
		}
	}
}
signed main(){
    int N,M;
    int A[1000],B[1000];
    cin>>N>>M;
    rep(i,M)cin>>A[i]>>B[i],A[i]--,B[i]--;

    rep(i,M){
        UF uf;
        uf.init(N);
        rep(j,M)if(i!=j)uf.unite(A[j],B[j]);
        bool ok=true;
        rep(j,N)if(uf.find(j)!=uf.find(0))ok=false;
        if(!ok)continue;
        G=vector<vint>(N);
        rep(j,M)if(i!=j)G[A[j]].pb(B[j]);
        vector<vint>H;vint comp;
        SCC::decompose(G,H,comp);
        if(H.size()!=N)continue;
        G=vector<vint>(N);
        rep(j,M)if(i!=j)G[A[j]].pb(B[j]),G[B[j]].pb(A[j]);
        memset(vis,0,sizeof(vis));
        int K=0;
        bridge.clear();
        dfs(0,-1,K);
        if(bridge.size()>=2){
            cout<<"YES"<<endl;
            return 0;
        }
    }
    cout<<"NO"<<endl;
    return 0;
}