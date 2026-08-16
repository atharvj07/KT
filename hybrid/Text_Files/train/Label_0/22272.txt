#include <bits/stdc++.h>
using namespace std;
#pragma GCC target("avx2")
#pragma GCC optimization("O2")
#pragma GCC optimization("unroll-loops")
const long double ERR = 1e-5;
const int MOD = 1e9 + 7;
bool areEqual(long double _n1, long double _n2) {
  return fabs(_n1 - _n2) < ERR;
}
const int maxN = 25, maxM = 405;
int N, M;
bool adj[maxN][maxN] = {};
vector<vector<int> > adjV(maxN);
int DEGREE[maxN] = {};
bool foundCycle = false, vis[maxN] = {};
bool degreeSort(int, int);
void DFS(int, int);
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> N >> M;
  int x, y;
  for (int i = 0; i < M; i++) {
    cin >> x >> y;
    x--;
    y--;
    if (x == y || adj[x][y]) continue;
    adjV[x].push_back(y);
    adjV[y].push_back(x);
    adj[x][y] = adj[y][x] = true;
    DEGREE[x]++;
    DEGREE[y]++;
  }
  for (vector<int> &V : adjV) {
    sort(V.begin(), V.end(), degreeSort);
  }
  for (int i = 0; i < N; i++) {
    memset(vis, 0, sizeof vis);
    DFS(i, -1);
    bool allVisited = true;
    for (int j = 0; j < N; j++)
      if (!vis[j]) {
        allVisited = false;
        break;
      }
    if (allVisited) {
      cout << "Yes" << '\n';
      return 0;
    }
  }
  cout << "No" << '\n';
}
void DFS(int V, int p) {
  if (vis[V]) return;
  vis[V] = true;
  for (int _V : adjV[V]) {
    if (vis[_V]) continue;
    DFS(_V, V);
    return;
  }
}
bool degreeSort(int x, int y) {
  if (DEGREE[x] != DEGREE[y]) return DEGREE[x] < DEGREE[y];
  return x < y;
}
