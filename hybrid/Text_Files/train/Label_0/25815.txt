#include <bits/stdc++.h>
using namespace std;
const long long int M = 5e5 + 5, LG = 17, inf = 1e18;
int n, m;
long long int f[M];
vector<long long int> g[M], h[M];
long long int c2[M];
long long int c1[M];
void dfs1(long long int x) {
  if (c1[x] == 1) return;
  c1[x] = 1;
  for (long long int y : g[x]) {
    dfs1(y);
  }
}
void dfs2(long long int x) {
  if (c2[x] == 1) return;
  c2[x] = 1;
  if (f[x] == 1) return;
  for (long long int y : h[x]) {
    dfs2(y);
  }
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) cin >> f[i];
  for (int i = 0; i < m; i++) {
    long long int a, b;
    cin >> a >> b;
    a--;
    b--;
    g[a].push_back(b);
    h[b].push_back(a);
  }
  for (int i = 0; i < n; i++) {
    if (f[i] == 1) dfs1(i);
  }
  for (int i = 0; i < n; i++) {
    if (f[i] == 2) dfs2(i);
  }
  for (int i = 0; i < n; i++) {
    cout << (c1[i] && c2[i]) << '\n';
  }
}
