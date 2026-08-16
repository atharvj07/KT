#include <bits/stdc++.h>
using namespace std;
int n, m;
int N;
char a[51][51];
int c[51][51];
vector<vector<int> > g;
int mt[51 * 51][51 * 51];
int used[51 * 51];
int d[51 * 51];
int color[51 * 51];
void dfs(int first, int second) {
  c[first][second] = N;
  if (first > 0 && c[first - 1][second] == 0 &&
      a[first - 1][second] == a[first][second])
    dfs(first - 1, second);
  if (first + 1 < n && c[first + 1][second] == 0 &&
      a[first + 1][second] == a[first][second])
    dfs(first + 1, second);
  if (second > 0 && c[first][second - 1] == 0 &&
      a[first][second - 1] == a[first][second])
    dfs(first, second - 1);
  if (second + 1 < m && c[first][second + 1] == 0 &&
      a[first][second + 1] == a[first][second])
    dfs(first, second + 1);
}
inline int dist(int v) {
  queue<int> b;
  memset(used, 0, sizeof(used));
  b.push(v);
  d[v] = 0;
  used[v] = 1;
  int dmax = -1;
  if (color[v] == 'B') dmax = 0;
  while (!b.empty()) {
    int v = b.front();
    b.pop();
    for (int(j) = (0); (j) < (g[v].size()); ++(j)) {
      int to = g[v][j];
      if (used[to] == 0) {
        used[to] = 1;
        d[to] = d[v] + 1;
        if (color[to] == 'B' && d[to] > dmax) dmax = d[to];
        b.push(to);
      }
    }
  }
  return dmax;
}
inline void add(int first, int second) {
  if (mt[first][second] == 0) {
    mt[first][second] = 1;
    mt[second][first] = 1;
    g[first - 1].push_back(second - 1);
    g[second - 1].push_back(first - 1);
  }
}
int main() {
  scanf("%d%d", &n, &m);
  for (int(i) = (0); (i) < (n); ++(i)) scanf("%s", &a[i]);
  for (int(i) = (0); (i) < (n); ++(i))
    for (int(j) = (0); (j) < (m); ++(j))
      if (c[i][j] == 0) {
        color[N] = a[i][j];
        N++;
        dfs(i, j);
      }
  g.assign(N, vector<int>());
  for (int(i) = (0); (i) < (n); ++(i))
    for (int(j) = (0); (j) < (m); ++(j)) {
      int first = c[i][j], second;
      if (i + 1 < n && c[i][j] != c[i + 1][j]) {
        second = c[i + 1][j];
        add(first, second);
      }
      if (j + 1 < m && c[i][j] != c[i][j + 1]) {
        second = c[i][j + 1];
        add(first, second);
      }
    }
  int ans = n * m;
  for (int(i) = (0); (i) < (N); ++(i)) {
    int r = dist(i);
    ans = min(r + 1, ans);
  }
  printf("%d\n", ans);
}
