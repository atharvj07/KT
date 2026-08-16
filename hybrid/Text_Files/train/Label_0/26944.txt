#include <bits/stdc++.h>
using namespace std;
const int MaxN = 100;
struct node {
  int x, y;
};
int mov[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
string mapa[MaxN];
int flood[MaxN][MaxN];
int vis[MaxN][MaxN];
int N;
queue<node> cola;
int dist(pair<int, int> a, pair<int, int> b) {
  return (a.first - b.first) * (a.first - b.first) +
         (a.second - b.second) * (a.second - b.second);
}
vector<pair<int, int> > uno, dos;
void bfs(int x, int y, int f) {
  node e, v;
  int i, j, p, q;
  e.x = x, e.y = y;
  vis[x][y] = f;
  cola.push(e);
  while (!cola.empty()) {
    e = cola.front();
    cola.pop();
    for (i = 0; i < 4; i++) {
      p = e.x + mov[i][0];
      q = e.y + mov[i][1];
      v.x = p, v.y = q;
      if (p <= 0 || p > N || q <= 0 || q > N) continue;
      if (vis[p][q]) continue;
      if (mapa[p][q] == '1') continue;
      vis[p][q] = f;
      cola.push(v);
    }
  }
}
int main() {
  int i, j, p, q, x1, x2, y1, y2, mini = 1e9;
  cin >> N;
  cin >> x1 >> y1;
  cin >> x2 >> y2;
  for (i = 1; i <= N; i++) {
    cin >> mapa[i];
    mapa[i] = '0' + mapa[i];
  }
  bfs(x2, y2, 1);
  if (vis[x1][y1]) {
    cout << "0";
    return 0;
  }
  for (i = 1; i <= N; i++) {
    for (j = 1; j <= N; j++) {
      if (vis[i][j] == 1) {
        uno.push_back(make_pair(i, j));
      }
    }
  }
  bfs(x1, y1, 2);
  for (i = 1; i <= N; i++) {
    for (j = 1; j <= N; j++) {
      if (vis[i][j] == 2) {
        dos.push_back(make_pair(i, j));
      }
    }
  }
  for (i = 0; i < uno.size(); i++) {
    for (j = 0; j < dos.size(); j++) {
      mini = min(mini, dist(uno[i], dos[j]));
    }
  }
  cout << mini;
}
