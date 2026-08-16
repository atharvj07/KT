#include <bits/stdc++.h>
using namespace std;
int par[400001];
int r[400001];
bool vis[400001];
int find(int x) {
  if (x == par[x]) return x;
  return find(par[x]);
}
void merge(int x, int y) {
  x = find(x);
  y = find(y);
  if (r[x] == r[y]) {
    par[x] = y;
    r[y]++;
  } else if (r[x] > r[y])
    par[y] = x;
  else
    par[x] = y;
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m, q;
  cin >> n >> m >> q;
  for (int i = 1; i <= n + m; i++) par[i] = i;
  while (q--) {
    int r, c;
    cin >> r >> c;
    c += n;
    if (find(r) != find(c)) merge(r, c);
  }
  for (int i = 1; i <= n + m; i++) vis[find(i)] = 1;
  int ret = -1;
  for (int i = 1; i <= n + m; i++) ret += vis[i];
  cout << ret << '\n';
  return 0;
}
