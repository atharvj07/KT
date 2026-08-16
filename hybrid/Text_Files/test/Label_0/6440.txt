#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define llint long long

using namespace std;

int n;
vector<int> G[100005];
vector<int> vec;
bool used[100005];

void bfs()
{
  queue<int> Q;
  used[1] = true;
  Q.push(1);

  while(Q.size()){
    int v = Q.front();
    Q.pop();
    vec.push_back(v);
    for(int i = 0; i < G[v].size(); i++){
      if(used[G[v][i]]) continue;
      Q.push(G[v][i]);
      used[G[v][i]]= true;
    }
  }
}

int Prev[100005][17];
int depth[100005];

void dfs(int v, int p, int d)
{
  depth[v] = d;
  Prev[v][0] = p;
  for(int i = 0; i < G[v].size(); i++){
    dfs(G[v][i], v, d+1);
  }
}

int getLCA(int u, int v){
  int x = u, y = v;
  if(depth[y] > depth[x]) swap(x, y);

  for(int i = 16; i >= 0; i--){
    if(depth[x] - (1<<i) >= depth[y]) x = Prev[x][i];
  }
  if(x == y) return x;
  for(int i = 16; i >= 0; i--){
    if(Prev[x][i] != Prev[y][i]){
      x = Prev[x][i];
      y = Prev[y][i];
    }
  }
  x = Prev[x][0];
  return x;
}

int main(void)
{
  cin >> n;
  int p;
  for(int i = 2; i <= n; i++){
    cin >> p;
    G[p].push_back(i);
  }
  for(int i = 1; i <= n; i++) sort(G[i].begin(), G[i].end());

  bfs();
  dfs(1, 0, 0);

  //or(int i = 0; i < vec.size(); i++) cout << vec[i] << " "; cout << endl;

  for(int i = 1; i < 17; i++){
    for(int j = 1; j <= n; j++){
      Prev[j][i] = Prev[Prev[j][i-1]][i-1];
    }
  }

  llint ans = depth[vec[0]];
  for(int i = 1; i < vec.size(); i++){
    ans += depth[vec[i-1]] + depth[vec[i]] - 2 * depth[getLCA(vec[i-1], vec[i])];
    //cout << vec[i] << " " << ans << endl;
  }
  cout << ans << endl;
}

