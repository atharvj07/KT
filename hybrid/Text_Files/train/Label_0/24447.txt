#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int N = 2e5 + 20;
vector<int> g[N];
vector<pair<ll, pair<int, int>>> edges;
ll bal, ans;

bool vis[N];
set<int> unvis;

int p[N], p2[N], cnt[N], sz[N];

int root(int v){
  if(p[v] == v)
    return v;
  return p[v] = root(p[v]);
}

void merge(int a, int b){
  a = root(a);
  b = root(b);
  if(a == b)
    return;
  p[b] = a;
  sz[a] += sz[b];
}

int root2(int v){
  if(p2[v] == v)
    return v;
  return p2[v] = root2(p2[v]);
}

void merge2(int a, int b){
  a = root2(a);
  b = root2(b);
  if(a == b)
    return;
  p2[b] = a;
}

queue<int> q;
void bfs(int s){
  q.push(s);
  vis[s] = true;
  unvis.erase(s);
  while(!q.empty()){
    int v = q.front();
    q.pop();
    for(int x : g[v])
      if(!vis[x])
        unvis.erase(x);
    for(int x : unvis){
      merge(v, x);
      q.push(x);
      vis[x] = true;
    }
    unvis.clear();
    for(int x : g[v])
      if(!vis[x])
        unvis.insert(x);
  }
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
  int n, m;
  cin >> n >> m;
  for(int i = 0; i < m; i ++){
    int u, v; ll w;
    cin >> u >> v >> w;
    u --; v --;
    g[v].push_back(u);
    g[u].push_back(v);
    edges.push_back({w, {u, v}});
    bal ^= w;
  }
  for(int i = 0; i < n; i ++){
    unvis.insert(i);
    p[i] = i;
    sz[i] = 1;
    p2[i] = i;
  }
  for(int i = 0; i < n; i ++){
    if(!vis[i])
      bfs(i);
  }
  bool ok = false;
  for(int i = 0; i < m; i ++){
    auto [x, y] = edges[i].second;
    if(root(x) == root(y)){
      cnt[root(x)] ++;
      bal = min(bal, edges[i].first);
    }
  }
  for(int i = 0; i < n; i ++){
    int x = root(i);
    if(sz[x] * (ll)(sz[x] - 1) / 2LL - cnt[x] - sz[x] + 1 > 0)
      ok = true;
  }
  sort(edges.begin(), edges.end());
  for(int i = 0; i < m; i ++){
    auto [x, y] = edges[i].second;
    if(root(x) != root(y)){
      ans += edges[i].first;
      merge(x, y);
      merge2(x, y);
    }
  }
  for(int i = 0; i < m; i ++){
    auto [x, y] = edges[i].second;
    if(root2(x) != root2(y))
      bal = min(bal, edges[i].first);
  }
  if(!ok)
    ans += bal;
  cout << ans;
}
