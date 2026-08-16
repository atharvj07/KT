#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline void read(T &x) {
  x = 0;
  char c = getchar();
  bool flag = false;
  while (!isdigit(c)) {
    if (c == '-') flag = true;
    c = getchar();
  }
  while (isdigit(c)) {
    x = (x << 1) + (x << 3) + (c ^ 48);
    c = getchar();
  }
  if (flag) x = -x;
}
int T, n, m, rt, mn, px, py, tot;
int d[1000010], deg[1000010], pre[1000010], dep[1000010], fa[1000010],
    bel[1000010];
bool tag[1000010], vis[1000010];
vector<int> ve[1000010];
struct edge {
  int to, nxt;
} e[1000010];
int head[1000010], edge_cnt;
void add(int from, int to) {
  e[++edge_cnt] = {to, head[from]}, head[from] = edge_cnt;
}
struct node {
  int x, y;
} t[1000010];
bool check1() {
  if (n == 1) return false;
  for (int i = 1; i <= n; ++i)
    if (!d[i]) return tag[i] = true;
  return false;
}
bool check2() {
  if (!rt || n == 2) return false;
  queue<int> q;
  q.push(rt);
  while (!q.empty()) {
    int x = q.front();
    q.pop();
    for (int i = head[x]; i; i = e[i].nxt) {
      int y = e[i].to;
      if (pre[y] || !d[y] || y == rt) continue;
      if (d[y] == 1) {
        while (pre[x]) tag[x] = true, x = pre[x];
        return tag[rt] = tag[y] = true;
      }
      pre[y] = x, q.push(y);
    }
  }
  return false;
}
void dfs(int x) {
  bel[x] = tot;
  for (int i = head[x]; i; i = e[i].nxt) {
    int y = e[i].to;
    if (d[y] != 2) continue;
    if (!bel[y])
      fa[y] = x, dep[y] = dep[x] + 1, dfs(y);
    else if (y != fa[x] && dep[x] > dep[y] && dep[x] - dep[y] < mn)
      px = x, py = y, mn = dep[x] - dep[y];
  }
}
bool check3() {
  mn = 1000000000;
  for (int i = 1; i <= n; ++i)
    if (d[i] == 2 && !dep[i]) tot++, dfs(i);
  if (mn != 1000000000) {
    while (px != py) tag[px] = true, px = fa[px];
    return tag[py] = true;
  }
  return false;
}
void find(int s) {
  queue<int> q;
  q.push(s);
  while (!q.empty()) {
    int x = q.front();
    q.pop();
    for (int i = head[x]; i; i = e[i].nxt) {
      int y = e[i].to;
      if (pre[y] || d[y] != 2 || y == s) continue;
      if (vis[y]) {
        while (pre[x]) tag[x] = true, x = pre[x];
        tag[s] = tag[y] = true;
        return;
      }
      pre[y] = x, q.push(y);
    }
  }
}
bool check4() {
  if (!rt || deg[rt] <= 4) return false;
  for (int i = 1; i <= n; ++i) pre[i] = 0;
  for (int i = head[rt]; i; i = e[i].nxt) {
    int y = e[i].to;
    ve[bel[y]].push_back(y), vis[y] = true;
  }
  int cnt = 0;
  for (int i = 1; i <= tot; ++i) {
    if (ve[i].size() < 2) continue;
    find(ve[i][0]);
    if (++cnt == 2) return tag[rt] = true;
  }
  return false;
}
void print() {
  int cnt = 0;
  for (int i = 1; i <= n; ++i) cnt += !tag[i];
  if (cnt == n || !cnt) {
    puts("No");
    return;
  }
  printf("Yes\n%d\n", cnt);
  for (int i = 1; i <= n; ++i)
    if (!tag[i]) printf("%d ", i);
  putchar('\n');
}
void clear() {
  edge_cnt = rt = px = py = tot = 0;
  for (int i = 1; i <= n; ++i)
    head[i] = d[i] = tag[i] = pre[i] = dep[i] = fa[i] = bel[i] = vis[i] = 0,
    ve[i].clear();
}
int main() {
  read(T);
  while (T--) {
    read(n), read(m);
    for (int i = 1; i <= m; ++i) {
      int x, y;
      read(x), read(y), d[x]++, d[y]++;
      add(x, y), add(y, x), t[i] = {x, y};
    }
    for (int i = 1; i <= n; ++i) {
      deg[i] = d[i], d[i] %= 3;
      if (d[i] == 1) rt = i;
    }
    if (check1() || check2() || check3() || check4())
      print();
    else
      puts("No");
    clear();
  }
  return 0;
}
