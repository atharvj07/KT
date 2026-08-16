#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

typedef pair<int,int> ii;

vector<int> G[510];

vector<string> arr;
vector<ii> edges;
bool found[510];
bool used[510];
bool cycle;

bool inValid(string a,string b) {
  if( a == b ) return false;
  int diff = -1;
  rep(i,min(a.size(),b.size())) if( a[i] != b[i] ) { diff = i; break; }
  if( diff == -1 && a.size() > b.size() ) return true;
  return false;
}

void add(string a,string b){
  if( a == b ) return;
  int diff = -1;
  rep(i,min(a.size(),b.size())) if( a[i] != b[i] ) { diff = i; break; }
  if( diff == -1 ) return;
  edges.push_back(ii(a[diff]-'a',b[diff]-'a'));
}

bool visit(int v,vector<int>& order,vector<int>& color){
  color[v] = 1;
  rep(i,G[v].size()){
    int e = G[v][i];
    if(color[e] == 2)continue;
    if(color[e] == 1)return false;
    if(!visit(e,order,color))return false;
    }
  order.push_back(v);
  color[v] = 2;
  return true;
}

bool topologicalSort(vector<int>& order){
  vector<int> color(26,0); 
  for(int u=0;u<26;u++) if(!color[u] && !visit(u,order,color)) return false;
  reverse(order.begin(),order.end());
  return true;
}


int main(){
  int n;
  while(cin >> n,n){
    rep(i,510) { G[i].clear(); found[i] = used[i] = false;  }
    bool fin = false;
    cycle = false;
    arr.clear();
    arr.resize(n);
    edges.clear();
    rep(i,n) cin >> arr[i];
    rep(i,n-1) {
      if( inValid(arr[i],arr[i+1]) ) { puts("no"); fin = true; break; }
      add(arr[i],arr[i+1]);
    }
    if( fin ) continue;
    rep(i,edges.size()) {
      int src = edges[i].first;
      int dst = edges[i].second;
      G[src].push_back(dst);
    }
    vector<int> order;
    if( !topologicalSort(order) ) { puts("no"); continue; }
    puts("yes");
  }
  return 0;
}

// same as http://codeforces.com/contest/512/problem/A 