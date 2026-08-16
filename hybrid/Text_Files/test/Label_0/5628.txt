#include <bits/stdc++.h>
using namespace std;

typedef int64_t i64;
typedef uint64_t ui64;

class graph{
public:
    struct adj{
        int index;
        int start;
        int to;
        i64 cost;
    };
    int nd;
    int eg;
    vector<adj> *node;
    vector<adj> edge;
    graph(int n,int m){
        nd=n;
        eg=m;
        node=new vector<adj>[nd]{};
        edge={};
    }
    void add_dir(int i,int s,int t,i64 c){
        node[s].push_back({i,s,t,c});
        edge.push_back({i,s,t,c});
    }
    void add_undir(int i,int s,int t,i64 c){
        node[s].push_back({i,s,t,c});
        node[t].push_back({i,t,s,c});
        edge.push_back({i,s,t,c});
    }
    void refr(void){
        for(int i=0;i<nd;i++) vector<adj>().swap(node[i]);
        delete[] node;
        vector<adj>().swap(edge);
    }
    bool IsLink(void);
    void DFS(int r,i64 *&p,bool *&vst);
    bool IsPlus(void);
    void BellmanFord(int s,i64 *&d);
    void Dijkstra(int s,i64 *&d);
    void BFS(int s,i64 *&d);
    void WarshallFloyd_dir(i64 **&d);
    void WarshallFloyd_undir(i64 **&d);
    i64 WMST_dir(int r);
    i64 WMST_undir(void);
    void Edmonds(int r,vector<adj> &p);
    void Kruscal(vector<adj> &p);
    void Prim(vector<adj> &p);
    void Artic(vector<int> &p);
    void Artic_sub(int r,int &k,int par,vector<int> &p,int *&ord,int *&low,bool *&vst);
    void Bridge(vector<adj> &p);
    void Bridge_sub(int r,int &k,int par,vector<adj> &p,int *&ord,int *&low,bool *&vst);
    void SCC(int *&c);
    void SCC_sub1(int r,vector<int> &vs,bool *&vst);
    void SCC_sub2(int r,int k,int *&c,bool *&vst,graph &rg);
    bool IsDAG(void);
    bool IsDAG_sub(int r,int &k,int *&l,int *&vst);
    void TopolSort(int *&l);
    void TopolSort_sub(int r,int &k,int *&l,bool *&vst);
    i64 Diameter(void);
    void Height(i64 *&h);
    void DFSTree(int s,vector<adj> &es);
    void DFSTree_sub(int r,vector<adj> &es,bool *&vst);
    void Cumul(int s,i64 *&d);
};

void graph::Height(i64 *&h){
    i64 *d=new i64[nd]{};
    for(int i=0;i<nd;i++) d[i]=INT64_MAX/2;
    queue<int> que;
    int u=0;
    d[0]=0;
    i64 ma=d[0];
    que.push(0);
    while(!que.empty()){
        int i=que.front();
        que.pop();
        for(const auto &j:node[i]){
            if(d[j.to]!=INT64_MAX/2) continue;
            d[j.to]=d[i]+j.cost;
            if(d[j.to]>ma){
                ma=d[j.to];
                u=j.to;
            }
            que.push(j.to);
        }
    }
    for(int i=0;i<nd;i++) d[i]=INT64_MAX/2;
    int v=u;
    d[u]=0;
    ma=d[u];
    que.push(u);
    while(!que.empty()){
        int i=que.front();
        que.pop();
        for(const auto &j:node[i]){
            if(d[j.to]!=INT64_MAX/2) continue;
            d[j.to]=d[i]+j.cost;
            if(d[j.to]>ma){
                ma=d[j.to];
                v=j.to;
            }
            que.push(j.to);
        }
    }
    i64 *rd=new i64[nd]{};
    for(int i=0;i<nd;i++) rd[i]=INT64_MAX/2;
    rd[v]=0;
    que.push(v);
    while(!que.empty()){
        int i=que.front();
        que.pop();
        for(const auto &j:node[i]){
            if(rd[j.to]!=INT64_MAX/2) continue;
            rd[j.to]=rd[i]+j.cost;
            que.push(j.to);
        }
    }
    for(int i=0;i<nd;i++) h[i]=max(d[i],rd[i]);
    delete[] d;
    delete[] rd;
}

int main(void){
    int n;
    scanf("%i",&n);
    graph g(n,n-1);
    int s,t;
    i64 w;
    for(int i=0;i<n-1;i++){
        scanf("%i%i%lli",&s,&t,&w);
        g.add_undir(i,s,t,w);
    }
    i64 *h=new i64[n];
    g.Height(h);
    for(int i=0;i<n;i++) printf("%lli\n",h[i]);
    return 0;
}

