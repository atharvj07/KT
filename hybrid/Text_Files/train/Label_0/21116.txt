#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
const long long INF = 0x3f3f3f3f3f3f3f3f;
const long long mod = (int)1e9 + 7;
const int N = 1e6 + 100;
int n;
int op[N];
int ok[N];
int val[N];
int ans[2];
char s[10];
vector<int> son[N];
void dfs(int u) {
  if (op[u] == 4) return;
  for (int i = 0; i < son[u].size(); i++) dfs(son[u][i]);
  int x = son[u][0];
  if (op[u] == 3) {
    val[u] = 1 ^ val[x];
    ok[x] = 1;
  }
  int y = son[u][1];
  if (op[u] == 1) {
    val[u] = val[x] & val[y];
    if (val[y] == 1) ok[x] = 1;
    if (val[x] == 1) ok[y] = 1;
  } else if (op[u] == 2) {
    val[u] = val[x] ^ val[y];
    ok[x] = ok[y] = 1;
  } else if (op[u] == 5) {
    val[u] = val[x] | val[y];
    if (val[x] == 1 && val[y] == 0) ok[x] = 1;
    if (val[x] == 0 && val[y] == 1) ok[y] = 1;
    if (val[x] == 0 && val[y] == 0) ok[x] = ok[y] = 1;
  }
}
void dfs2(int u, int flag) {
  ok[u] &= flag;
  for (int i = 0; i < son[u].size(); i++) dfs2(son[u][i], ok[u]);
}
int main() {
  scanf("%d", &n);
  int u, v;
  for (int i = 1; i <= n; i++) {
    scanf("%s", s + 1);
    if (s[1] == 'I')
      op[i] = 4, scanf("%d", &val[i]);
    else if (s[1] == 'N') {
      scanf("%d", &u);
      son[i].push_back(u);
      op[i] = 3;
    } else {
      scanf("%d%d", &u, &v);
      son[i].push_back(u);
      son[i].push_back(v);
      if (s[1] == 'A') op[i] = 1;
      if (s[1] == 'X') op[i] = 2;
      if (s[1] == 'O') op[i] = 5;
    }
  }
  dfs(1);
  ok[1] = 1;
  dfs2(1, 1);
  ans[0] = val[1];
  ans[1] = val[1] ^ 1;
  for (int i = 1; i <= n; i++)
    if (op[i] == 4) printf("%d", ans[ok[i]]);
  return 0;
}
