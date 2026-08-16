
#include<bits/stdc++.h>
using namespace std;
using Int = long long;
using ll = long long;

template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b)a=b;};
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b)a=b;};


struct SCC{
  vector<vector<int> > G, R, T, C;
  vector<int> vs, used, blg;

  SCC(){}
  SCC(int n):G(n), R(n), used(n), blg(n){}

  void add_edge(int u, int v){
    G[u].emplace_back(v);
    R[v].emplace_back(u);
  }

  void dfs(int v){
    used[v] = 1;
    for(int u:G[v])
      if(!used[u]) dfs(u);
    vs.emplace_back(v);
  }

  void rdfs(int v, int k){
    used[v] = 1;
    blg[v] = k;
    C[k].emplace_back(v);
    for(int u:R[v])
      if(!used[u]) rdfs(u, k);
  }

  int build(){
    int n =G.size();
    for(int v=0;v<n;v++)
      if(!used[v]) dfs(v);

    fill(used.begin(), used.end(), 0);

    int k = 0;
    for(int i=n-1;i>=0;i--){
      if(!used[vs[i]]){
        T.emplace_back();
        C.emplace_back();
        rdfs(vs[i], k++);
      }
    }

    for(int v=0;v<n;v++)
      for(int u:G[v])
        if(blg[v] != blg[u])
          T[blg[v]].push_back(blg[u]);

    for(int i=0;i<k;i++){
      sort(T[i].begin(), T[i].end());
      T[i].erase(unique(T[i].begin(), T[i].end()), T[i].end());
    }
    return k;
  }
  int operator[](int k) const{return blg[k];}
};


struct IndependentSet{
  int n;
  vector<vector<int> > G;
  IndependentSet(int n):n(n), G(n){}

  void add_edge(int u, int v){
    G[u].emplace_back(v);
    G[v].emplace_back(u);
  }

  int build(){
    vector<int> deg(n, 0);
    for(int i=0;i<n;i++) deg[i] = G[i].size();

    int res = 0, cnt = 0, alive = n;
    vector<int> used(n, 0), dead(n, 0);

    function<void(void)> dfs = [&](){
      if(cnt + alive <= res) return;
      int v = -1;

      for(int i=0;i<n;i++){
        if(used[i] || dead[i] ) continue;
        if(deg[i] <= 1){
          v = i;
          break;
        }
        if(v < 0 || deg[v] < deg[i]) v = i;
      }

      if(v < 0) return;

      if(deg[v] != 1){
        dead[v] = 1;
        alive--;
        for(int u:G[v]) deg[u]--;
        dfs();

        dead[v] = 0;
        alive++;
        for(int u:G[v]) deg[u]++;
      }

      {
        used[v] = 1;
        alive--;
        for(int u:G[v])
          if(0 == dead[u]++) alive -= !used[u];
        
        cnt++;
        chmax(res, cnt);

        dfs();
        used[v] = 0;
        alive++;
        for(int u:G[v])
          if(--dead[u] == 0) alive += !used[u];
        cnt--;
                               
      }
    };

    dfs();
    return res;
  }

};
signed main(){
  cin.tie(0);
  ios::sync_with_stdio(0);

  int n,m;
  while(cin>>n>>m,n){
    vector< vector<int> > as(n,vector<int>(m));
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)
        cin>>as[i][j];
    
    IndependentSet G(m);
    for(int a=0;a<m;a++){
      for(int b=0;b<a;b++){
        int ng=0;
        for(int i=0;i<n;i++){
          for(int j=0;j<i;j++){
            if(as[i][a]==as[j][a]) continue;
            if(as[i][b]==as[j][b]) continue;
            if((as[i][a]>as[j][a])^(as[i][b]>as[j][b])) ng=1;
            if(ng) break;
          }
          if(ng) break;
        }
        
        if(ng) G.add_edge(a,b);        
      }
    }

    cout<<G.build()<<endl;
  }
  
  return 0;
}

