#include<bits/stdc++.h>
using namespace std;

struct edge{
  int to,from;  
  edge(int to,int from) :
    to(to), from(from) {}
  edge(){}
};

int N,M;
bool used[5000];
set<int> G[555];
vector<edge> E;

int main(){
  cin >> N >> M;  
  for(int i=0;i<M;i++){
    int s,t; cin >> s >> t;
    --s; --t;
    E.push_back( edge(t,s) );
    G[s].insert( i );
    G[t].insert( i );
  }
  if( M == 0 ) {
    cout << 0 << endl;
    return 0;
  }
  bool ed = true;
  int res = 0;
  while( ed ){
    int minid=0;
    while( G[minid].empty() ) minid++;
    for(int i=0;i<N;i++){
      if( G[i].empty() ) continue;
      if( G[minid].size() > G[i].size()  ) minid = i;
    }
    //   cout << G[minid].size() << endl;
    res += G[minid].size()-1;
    for(auto it = G[minid].begin(); it != G[minid].end(); it++ ){
      used[*it] = true;
      // cout << "new " << *it << endl;
      for(int i=0;i<N;i++){
        if( i == minid ) continue;
        G[i].erase(*it);
      }
    }
    G[minid].clear();
    ed = false;
    for(int i=0;i<M;i++)
      if( !used[i] ) ed = true;
  }
  cout << res << endl;
}