#include <bits/stdc++.h>
using namespace std;
char buf[1 << 21], *p1 = buf, *p2 = buf;
template <class T>
inline bool cmax(T &a, const T &b) {
  return a < b ? a = b, 1 : 0;
}
inline int read() {
  char ch;
  bool flag = 0;
  int res;
  while (!isdigit(
      ch = (p1 == p2 &&
                    (p2 = (p1 = buf) + fread(buf, 1, 1 << 21, stdin), p1 == p2)
                ? EOF
                : *p1++)))
    (ch == '-') && (flag = true);
  for (res = ch - '0'; isdigit(
           ch = (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 21, stdin),
                             p1 == p2)
                     ? EOF
                     : *p1++));
       res = res * 10 + ch - '0')
    ;
  (flag) && (res = -res);
  return res;
}
const int N = 1e5 + 5, mod = 1e9 + 7;
int n, m, head[N], Next[N << 1], ver[N << 1], edge[N << 1];
int S, T, lim, b[N << 1], rt[N], Pre[N], tot, cnt;
int L[N * 120], R[N * 120], sum[N * 120];
inline void add(int u, int v, int e) {
  ver[++tot] = v, Next[tot] = head[u], head[u] = tot, edge[tot] = e;
  ver[++tot] = u, Next[tot] = head[v], head[v] = tot, edge[tot] = e;
}
bool cmp(int u, int v, int l, int r) {
  if (l == r) return sum[u] > sum[v];
  int mid = (l + r) >> 1;
  if (sum[R[u]] == sum[R[v]])
    return cmp(L[u], L[v], l, mid);
  else
    return cmp(R[u], R[v], mid + 1, r);
}
int update(int last, int &now, int l, int r, int k) {
  L[now = ++cnt] = L[last], R[now] = R[last];
  if (l == r) {
    sum[now] = sum[last] ^ 1;
    return sum[last];
  }
  int mid = (l + r) >> 1, res;
  if (k > mid)
    res = update(R[last], R[now], mid + 1, r, k);
  else {
    res = update(L[last], L[now], l, mid, k);
    if (res) res = update(R[last], R[now], mid + 1, r, k);
  }
  sum[now] = (1ll * sum[R[now]] * b[mid - l + 1] + sum[L[now]]) % mod;
  return res;
}
struct node {
  int x, rt;
  bool operator<(const node &b) const { return cmp(rt, b.rt, 0, lim); }
};
priority_queue<node> q;
void dfs(int u, int dep) {
  if (u == S) {
    printf("%d\n%d ", dep, u);
    return;
  }
  dfs(Pre[u], dep + 1);
  printf("%d ", u);
}
void print(int u) {
  printf("%d\n", sum[rt[u]]);
  dfs(u, 1);
  exit(0);
}
int main() {
  n = read(), m = read();
  for (int i = 1; i <= m; ++i) {
    int u, v, e;
    u = read(), v = read(), e = read();
    add(u, v, e);
    cmax(lim, e);
  }
  lim += 18;
  b[0] = 1;
  for (int i = 1; i <= lim; ++i) b[i] = (1ll * b[i - 1] << 1) % mod;
  S = read(), T = read();
  q.push((node){S, rt[S]});
  while (!q.empty()) {
    node u = q.top();
    q.pop();
    if (u.rt != rt[u.x]) continue;
    if (u.x == T) print(T);
    for (int i = head[u.x]; i; i = Next[i]) {
      int v = ver[i], RT;
      update(u.rt, RT, 0, lim, edge[i]);
      if (!rt[v] || cmp(rt[v], RT, 0, lim))
        rt[v] = RT, q.push((node){v, rt[v]}), Pre[v] = u.x;
    }
  }
  puts("-1");
  return 0;
}
