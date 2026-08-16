#include <bits/stdc++.h>
#define ll long long
#define INF 1000000005
#define MOD 1000000007
#define EPS 1e-10
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;--i)
#define srep(i,s,t) for(int i=(int)(s);i<(int)(t);++i)
#define each(a,b) for(auto& (a): (b))
#define all(v) (v).begin(),(v).end()
#define len(v) (int)(v).size()
#define zip(v) sort(all(v)),v.erase(unique(all(v)),v.end())
#define cmx(x,y) x=max(x,y)
#define cmn(x,y) x=min(x,y)
#define fi first
#define se second
#define pb push_back
#define show(x) cout<<#x<<" = "<<(x)<<endl
#define spair(p) cout<<#p<<": "<<p.fi<<" "<<p.se<<endl
#define sar(a,n) cout<<#a<<":";rep(pachico,n)cout<<" "<<a[pachico];cout<<endl
#define svec(v) cout<<#v<<":";rep(pachico,v.size())cout<<" "<<v[pachico];cout<<endl
#define svecp(v) cout<<#v<<":";each(pachico,v)cout<<" {"<<pachico.first<<":"<<pachico.second<<"}";cout<<endl
#define sset(s) cout<<#s<<":";each(pachico,s)cout<<" "<<pachico;cout<<endl
#define smap(m) cout<<#m<<":";each(pachico,m)cout<<" {"<<pachico.first<<":"<<pachico.second<<"}";cout<<endl

using namespace std;

typedef pair<int,int> P;
typedef pair<ll,int> pli;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<P> vp;
typedef vector<string> vs;

const int MAX_N = 100005;

class UF {
private:
    int sz; vector<int> par,nrank;
public:
    UF(){}
    UF(int node_size){ sz = node_size; par.resize(sz),nrank.resize(sz,0); rep(i,sz) par[i] = i; }
    int find(int x){ if(par[x] == x){ return x; }else{ return par[x] = find(par[x]); } }
    void unite(int x,int y)
    { x = find(x),y = find(y); if(x == y) return;
    	if(nrank[x] < nrank[y]){ par[x] = y; }else{ par[y] = x; if(nrank[x] == nrank[y]) nrank[x]++; } }
    bool same(int x,int y){ return find(x) == find(y); }
};

struct edge
{
    int from,to;
    ll cost;
    bool operator< (const edge& another) const {
        return cost < another.cost;
    }
};

vector<edge> G[MAX_N], graph[MAX_N];
map<P,int> mp;

template<typename T> class Heap {
public:
    struct node {
        node* l; node* r; T val;
        node(T t) : l(nullptr), r(nullptr), val(t){}
    };
    node* root;
    int sz;
    Heap() : root(nullptr), sz(0){}
    node* meld(node* a, node* b){
        if(!a) return b; if(!b) return a;
        if(a->val > b->val) swap(a, b);
        a->r = meld(a->r,b); swap(a->l, a->r);
        return a;
    }
    void meld(Heap<T>* hp){
        sz += hp->sz;
        root = meld(root, hp->root);
    }
    bool empty(){ return !root; }
    void push(T val){ sz++; node* p = new node(val); root = meld(root, p); }
    T top(){ return root->val; }
    void pop(){ sz--; node* p = root; root = meld(root->r, root->l); delete p; }
};

pair<Heap<pli>*, set<int>* > dfs(int u,int p,vl& ans)
{
    Heap<pli>* hp = new Heap<pli>();
    set<int>* st = new set<int>{u};
    each(e,G[u]){
        if(e.to != p){
            auto res = dfs(e.to,u,ans);
            auto nhp = res.fi;
            auto nst = res.se;
            ll val = -1;
            while(nhp->root){
                pli p = nhp->top();
                if(nst->find(p.se) == nst->end()){
                    val = p.fi - e.cost;
                    break;
                }else{
                    nhp->pop();
                }
            }
            if(val < 0){
                ans[mp[P(u,e.to)]] = val;
            }else{
                ans[mp[P(u,e.to)]] += val;
            }
            if(hp->sz > nhp->sz){
                hp->meld(nhp);
            }else{
                nhp->meld(hp);
                hp = nhp;
            }
            if(st->size() > nst->size()){
                each(it,*nst){
                    st->insert(it);
                }
            }else{
                each(it,*st){
                    nst->insert(it);
                }
                st = nst;
            }
        }
    }
    each(e,graph[u]){
        if(e.to != p && st->find(e.to) == st->end()){
            hp->push(pli(e.cost,e.to));
        }
    }
    return make_pair(hp,st);
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,m;
    cin >> n >> m;
    vector<edge> es(m);
    rep(i,m){
        int a,b,c;
        cin >> a >> b >> c;
        --a,--b;
        es[i] = (edge){a,b,c};
        graph[a].pb((edge){a,b,c}),graph[b].pb((edge){b,a,c});
        mp[P(a,b)] = mp[P(b,a)] = i;
    }
    sort(all(es));
    UF uf(n);
    ll cri = 0;
    int ch = 0;
    each(e,es){
        if(!uf.same(e.from,e.to)){
            ch++;
            cri += e.cost;
            uf.unite(e.from,e.to);
            G[e.from].pb(e),G[e.to].pb((edge){e.to,e.from,e.cost});
        }
    }
    if(ch != n-1){
        rep(i,m){
            cout << "-1\n";
        }
        return 0;
    }
    vl ans(m,cri);
    dfs(0,-1,ans);
    rep(i,m){
        cout << ans[i] << "\n";
    }
    return 0;
}

