#include<bits/stdc++.h>
using namespace std;
using Int = long long;
template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b) a=b;}
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b) a=b;}


struct FastIO{
  FastIO(){
    cin.tie(0);
    ios::sync_with_stdio(0);
  }
}fastio_beet;


template<typename T,bool directed>
struct Dinic{
  struct edge {
    int to;
    T cap;
    int rev;
    edge(){}
    edge(int to,T cap,int rev):to(to),cap(cap),rev(rev){}
  };

  vector<vector<edge> > G;
  vector<int> level,iter;

  Dinic(){}
  Dinic(int n):G(n),level(n),iter(n){}

  int add_edge(int from,int to,T cap){
    G[from].emplace_back(to,cap,G[to].size());
    G[to].emplace_back(from,directed?0:cap,G[from].size()-1);
    return G[to].back().rev;
  }

  void bfs(int s){
    fill(level.begin(),level.end(),-1);
    queue<int> que;
    level[s]=0;
    que.emplace(s);
    while(!que.empty()){
      int v=que.front();que.pop();
      for(int i=0;i<(int)G[v].size();i++){
        edge &e=G[v][i];
        if(e.cap>0&&level[e.to]<0){
          level[e.to]=level[v]+1;
          que.emplace(e.to);
        }
      }
    }
  }

  T dfs(int v,int t,T f){
    if(v==t) return f;
    for(int &i=iter[v];i<(int)G[v].size();i++){
      edge &e=G[v][i];
      if(e.cap>0&&level[v]<level[e.to]){
        T d=dfs(e.to,t,min(f,e.cap));
        if(d==0) continue;
        e.cap-=d;
        G[e.to][e.rev].cap+=d;
        return d;
      }
    }
    return 0;
  }

  T flow(int s,int t,T lim){
    T fl=0;
    while(1){
      bfs(s);
      if(level[t]<0||lim==0) break;
      fill(iter.begin(),iter.end(),0);

      while(1){
        T f=dfs(s,t,lim);
        if(f==0) break;
        fl+=f;
        lim-=f;
      }
    }
    return fl;
  }

  T flow(int s,int t){
    return flow(s,t,numeric_limits<T>::max()/2);
  }

  T cut(int s,int t,int x,int a){
    static_assert(directed, "must be directed");
    auto &e=G[x][a];
    int y=e.to;
    T ce=e.cap,cr=G[y][e.rev].cap;
    if(cr==0) return 0;
    e.cap=G[y][e.rev].cap=0;
    T cap=cr-flow(x,y,cr);
    if(x!=s&&cap!=0) flow(x,s,cap);
    if(t!=y&&cap!=0) flow(t,y,cap);
    e.cap=ce+cr;
    return cap;
  }
};

//INSERT ABOVE HERE
signed main(){
  int n;
  cin>>n;

  vector<string> vs(n);
  for(int i=0;i<n;i++) cin>>vs[i];

  int cnt=0,ooo=0;
  for(string s:vs){
    int m=s.size();
    for(int i=0;i+2<m;i++)
      if(s[i]=='A'&&s[i+1]=='O'&&s[i+2]=='R') cnt++;
    if(s=="O") ooo++;
  }

  // 0: x?x
  // 1: x?A
  // 2: x?AO

  // 3: R?x
  // 4: R?A
  // 5: R?AO

  // 6: OR?x
  // 7: OR?A
  // 8: OR?AO
  vector<int> num(9,0);
  for(string s:vs){
    int m=s.size();
    int p=0,q=0;
    if(s[0]=='R'){
      p=1;
    }
    if(s[0]=='O'){
      if(1<m&&s[1]=='R') p=2;
    }

    if(s[m-1]=='A'){
      q=1;
    }
    if(s[m-1]=='O'){
      if(m-2>=0&&s[m-2]=='A') q=2;
    }
    num[p*3+q]++;
  }

  int sum=0;
  for(int i=1;i<9;i++) sum+=num[i];
  if(sum==0){
    cout<<cnt<<endl;
    return 0;
  }

  Dinic<int, true> G(22);
  int S=18,T=19,U=20,V=21;

  for(int i=0;i<9;i++){
    G.add_edge(S,i,num[i]);
    G.add_edge(9+i,T,num[i]);
  }

  for(int i=0;i<9;i++){
    for(int j=0;j<9;j++){
      int p=i%3,q=j/3;
      if((p==1&&q==2)||(p==2&&q==1))
        G.add_edge(i,9+j,num[i]-(i==j));

      if(p==1&&q==1){
        G.add_edge(i,U,num[i]-(i==j));
        G.add_edge(V,9+j,num[i]-(i==j));
      }
    }
  }
  G.add_edge(U,V,ooo);

  int res=G.flow(S,T);
  if(sum==res) res--;
  cout<<cnt+res<<endl;
  return 0;
}

