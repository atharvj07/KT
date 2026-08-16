#include <bits/stdc++.h>
using namespace std;
const int maxn = 50005, maxm = maxn;
inline int read() {
  int w = 0, f = 1;
  char ch = getchar();
  while (ch < '0' or ch > '9') {
    if (ch == '-') f = -f;
    ch = getchar();
  }
  while (ch >= '0' and ch <= '9') w = w * 10 + ch - '0', ch = getchar();
  return w * f;
}
int N, M, d, vis[maxn], match[maxn], ans[maxn];
int head[maxn], Next[maxm], ver[maxm], tot;
int p[maxn], c[maxn], k[maxn];
void add(int x, int y) { ver[++tot] = y, Next[tot] = head[x], head[x] = tot; }
bool dfs(int x) {
  for (int i = head[x]; i; i = Next[i]) {
    if (!vis[ver[i]]) {
      vis[ver[i]] = 1;
      if (match[ver[i]] == -1 or dfs(match[ver[i]])) {
        match[ver[i]] = x;
        return 1;
      }
    }
  }
  return 0;
}
int main() {
  N = read(), M = read();
  for (int i = 1; i <= N; i++) p[i] = read();
  for (int i = 1; i <= N; i++) c[i] = read();
  d = read();
  for (int i = 1; i <= d; i++) {
    k[i] = read();
    vis[k[i]] = 1;
  }
  for (int i = 1; i <= N; i++) {
    if (!vis[i]) add(p[i], c[i]);
  }
  for (int i = 1; i < maxn; i++) match[i] = -1;
  int mex = 0;
  for (int i = d; i >= 1; i--) {
    memset(vis, 0, sizeof vis);
    while (dfs(mex)) {
      mex++;
      memset(vis, 0, sizeof(vis));
    }
    ans[i] = mex;
    add(p[k[i]], c[k[i]]);
  }
  for (int i = 1; i <= d; i++) printf("%d\n", ans[i]);
  return 0;
}
