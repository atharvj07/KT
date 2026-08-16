#include <bits/stdc++.h>
using namespace std;
int n, m, a[100011];
vector<int> head[100011], bot[100011];
bool chk[100011], kt[100011];
void input() {
  int i, u, v;
  scanf("%d", &n);
  scanf("%d", &m);
  for (i = 1; i <= n; i++) scanf("%d", &a[i]);
  for (i = 1; i <= m; i++) {
    scanf("%d", &u);
    scanf("%d", &v);
    head[u].push_back(v);
    bot[v].push_back(u);
  }
}
void dfs1(int u) {
  chk[u] = 1;
  int i, v;
  if (!head[u].empty())
    for (i = 0; i <= head[u].size() - 1; i++) {
      v = head[u][i];
      if (a[v] != 1 && !chk[v]) dfs1(v);
    }
}
void dfs2(int u) {
  kt[u] = 1;
  if (a[u] == 1) return;
  int i, v;
  if (!bot[u].empty())
    for (i = 0; i <= bot[u].size() - 1; i++) {
      v = bot[u][i];
      if (!kt[v]) dfs2(v);
    }
}
void solve() {
  int i;
  for (i = 1; i <= n; i++)
    if (a[i] == 1) dfs1(i);
  for (i = 1; i <= n; i++)
    if (a[i] == 2) dfs2(i);
}
void output() {
  int i;
  for (i = 1; i <= n; i++)
    if (chk[i] && kt[i])
      printf("1\n");
    else
      printf("0\n");
}
int main() {
  input();
  solve();
  output();
}
