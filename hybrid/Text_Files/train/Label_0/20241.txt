#include <algorithm>
#include <bitset>
#include <cassert>
#include <chrono>
#include <climits>
#include <cmath>
#include <complex>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <cstdint>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define MP make_pair
#define PB push_back
#define inf 1000000007
#define rep(i,n) for(int i = 0; i < (int)(n); ++i)
#define all(x) (x).begin(),(x).end()

template<typename A, size_t N, typename T>
void Fill(A (&array)[N], const T &val){
    std::fill( (T*)array, (T*)(array+N), val );
}
 
template<class T> inline bool chmax(T &a, T b){
    if(a<b){
        a = b;
        return true;
    }
    return false;
}

template<class T> inline bool chmin(T &a, T b){
    if(a>b){
        a = b;
        return true;
    }
    return false;
}

class TreeDiameter
{
public:
    int V;
    vector<vector<int> > G;
    vector<int> diameter;
    TreeDiameter(int node_size) : V(node_size), G(V){}
    void add_edge(int u,int v){
        G[u].push_back(v),G[v].push_back(u);
    }
    void dfs(int u,int p,int d,int& far,int& mx){
        if(mx < d){
            far = u;
            mx = d;
        }
        for(int v : G[u]){
            if(v != p){
                dfs(v,u,d+1,far,mx);
            }
        }
    }
    bool redfs(int u,int p,const int t){
        if(u == t){
            return true;
        }
        for(int v : G[u]){
            if(v != p){
                diameter.push_back(v);
                if(redfs(v,u,t)){
                    return true;
                }else{
                    diameter.pop_back();
                }
            }
        }
        return false;
    }
    void solve(){
        int s,t,mx;
        mx = -1;
        dfs(0,-1,0,s,mx);
        mx = -1;
        dfs(s,-1,0,t,mx);
        diameter.push_back(s);
        redfs(s,-1,t);
    }
};


template<typename T> class segtree {
private:
    int n,sz;
    vector<pair<T, int> > node;
public:
    void resize(vector<T>& v){
        sz = (int)v.size();
        n = 1;
        while(n < sz){
            n *= 2;
        }
        node.resize(2*n);
        for(int i = 0; i < sz; i++){
            node[i+n] = make_pair(v[i], i);
        }
        for(int i=n-1; i>=1; i--){
            node[i] = min(node[2*i], node[2*i+1]);
        }
    }
    void update(int k, T a)
    {
    	node[k+=n] = make_pair(a, k);
    	while(k>>=1){
            node[k] = min(node[2*k], node[2*k+1]);
    	}
    }
    pair<T, int> query(int a,int b)
    {
        pair<T, int> res1 = make_pair(numeric_limits<T>::max(), -1);
        pair<T, int> res2 = make_pair(numeric_limits<T>::max(), -1);
        a += n, b += n;
        while(a != b){
            if(a % 2) res1 = min(res1, node[a++]);
            if(b % 2) res2 = min(res2, node[--b]);
            a >>= 1, b >>= 1;
        }
        return min(res1, res2);
    }
};

class LCA{
public:
    int V;
    vector<vector<int> > G;
    vector<int> ord,depth,id;
    segtree<int> st;
    LCA(int node_size) : V(node_size), G(V), depth(V), id(V, -1){}
    void add_edge(int from,int to){
        G[from].push_back(to),G[to].push_back(from);
    }
    void dfs(int u,int p,int k){
        id[u] = (int)ord.size();
        ord.push_back(u);
        depth[u] = k;
        for(int v : G[u]){
            if(v != p){
                dfs(v,u,k+1);
                ord.push_back(u);
            }
        }
    }
    void build(){
        ord.reserve(2*V-2);
        for(int i = 0; i < V; i++){
            if(id[i] < 0){
                dfs(i,-1,0);
            }
        }
        vector<int> stvec(2*V-2);
    	for(int i = 0; i < 2*V-2; i++){
    		stvec[i] = depth[ord[i]];
    	}
        st.resize(stvec);
    }
    int solve(int u,int v){
        return ord[st.query(min(id[u],id[v]),max(id[u],id[v])+1).second];
    }
    int dist(int u,int v){
        int lca = solve(u,v);
        return depth[u] + depth[v] - 2*depth[lca];
    }
};
set<int> st;
vector<vector<int> > g;
vector<bool> sp;
void dfs(int id,int pre){
    sp[id] = true;
    for(auto x:g[id]){
        if(x!=pre&&st.count(x)==0){
            dfs(x,id);
        }
    }
}
int main(){
    int n;
    cin >> n;
    if(n==1){
        cout << 1 << endl;
        return 0;
    }
    TreeDiameter tr(n);
    LCA lca(n);
    g.resize(n);
    sp.resize(n);
    vector<int>c(n);
    rep(i,n-1){
        int a,b;
        cin >> a >> b;
        a--;b--;
        tr.add_edge(a,b);
        lca.add_edge(a,b);
        c[a]++;
        c[b]++;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    tr.solve();
    lca.build();
    int M = tr.diameter.size();
    int x = tr.diameter[0];
    int y = tr.diameter[M-1];
    for(auto xx:tr.diameter){
        st.insert(xx);
    }
    if(M%2==1){
        int mid = tr.diameter[M/2];
        dfs(mid,-1);
    }
    bool flag = 1;
    rep(i,n){
        if(c[i]>=3){
            flag = 0;
        }
    }
    if(flag){
        rep(i,n){
            cout <<1;
        }
        cout << endl;
    }else{
        int mx = 0;
        rep(i,n){
            if(st.count(i))continue;
            int dd = lca.dist(i,x);
            int zz= lca.dist(i,y);
            if(sp[i]){
                chmax(dd,zz);
                if(dd==M-1){
                    chmax(mx,dd-1);
                }else{
                    chmax(mx,dd);
                }
            }else{
                chmax(mx,dd);
                chmax(mx,zz);
            }
        }
        rep(i,n){
            if(i<=1){
                cout << 1;
            }else{
                if(i<=mx-1){
                    cout << 0;
                }else{
                    cout << 1;
                }
            }
        }
        cout << endl;
    }
    return 0;
}
