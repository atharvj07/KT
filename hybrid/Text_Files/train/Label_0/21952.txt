#include <bits/stdc++.h>
using namespace std;
inline int read() {
  static int r, sign;
  static char c;
  r = 0, sign = 1;
  do c = getchar();
  while (c != '-' && (c < '0' || c > '9'));
  if (c == '-') sign = -1, c = getchar();
  while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
  return sign * r;
}
template <typename T>
inline void print(T *a, int n) {
  for (int i = 1; i < n; ++i) cout << a[i] << " ";
  cout << a[n] << endl;
}
const int mod = (int)1e9 + 7;
struct hashInt {
  int x;
  hashInt() {}
  hashInt(int _x) : x(_x) {}
  inline hashInt operator+(const hashInt &y) const {
    int z = x + y.x;
    if (z >= mod) z -= mod;
    if (z < 0) z += mod;
    return hashInt(z);
  }
  inline hashInt operator-(const hashInt &y) const {
    int z = x - y.x;
    if (z >= mod) z -= mod;
    if (z < 0) z += mod;
    return hashInt(z);
  }
  inline hashInt operator*(const hashInt &y) const {
    return hashInt((long long)x * y.x % mod);
  }
};
struct edge {
  int next, node;
  hashInt w;
} e[100100 << 1 | 1];
int head[100100 + 1], tot = 0;
inline void addedge(int a, int b, int w) {
  e[++tot].next = head[a];
  head[a] = tot, e[tot].node = b, e[tot].w = w;
}
struct DP {
  hashInt sum, sqr;
  DP() {}
  DP(int _s, int _q) : sum(_s), sqr(_q) {}
  DP(hashInt _s, hashInt _q) : sum(_s), sqr(_q) {}
} up[100100 + 1], down[100100 + 1], downex[100100 + 1];
int n, size[100100 + 1];
inline hashInt delta(const DP &x, int n, hashInt b) {
  return x.sqr + b * b * n + b * 2 * x.sum;
}
void preUp(int x, int f) {
  size[x] = 1, up[x].sum = up[x].sqr = 0;
  for (int i = head[x]; i; i = e[i].next) {
    int node = e[i].node;
    if (node == f) continue;
    preUp(node, x);
    size[x] += size[node];
    up[x].sum = up[x].sum + up[node].sum + e[i].w * size[node];
    up[x].sqr = up[x].sqr + delta(up[node], size[node], e[i].w);
  }
}
void preDown(int x, int f) {
  for (int i = head[x]; i; i = e[i].next) {
    int node = e[i].node;
    if (node == f) continue;
    DP cur;
    cur.sum = down[x].sum + up[x].sum - up[node].sum - e[i].w * size[node];
    cur.sqr = down[x].sqr + up[x].sqr - delta(up[node], size[node], e[i].w);
    downex[node] = cur;
    down[node].sum = cur.sum + e[i].w * (n - size[node]);
    down[node].sqr = delta(cur, n - size[node], e[i].w);
    preDown(node, x);
  }
}
int p[18 + 1][100100 + 1], logn, dep[100100 + 1];
hashInt dis[100100 + 1], dissum[100100 + 1], dissqr[100100 + 1];
void preDA(int x, int f) {
  p[0][x] = f;
  for (int i = head[x]; i; i = e[i].next) {
    int node = e[i].node;
    if (node == f) continue;
    dep[node] = dep[x] + 1;
    dis[node] = dis[x] + e[i].w;
    dissum[node] = dissum[x] + dis[node];
    dissqr[node] = dissqr[x] + dis[node] * dis[node];
    preDA(node, x);
  }
}
inline int LCA(int x, int y) {
  if (dep[x] > dep[y]) swap(x, y);
  for (int i = logn; i >= 0; --i)
    if (dep[x] <= dep[p[i][y]]) y = p[i][y];
  if (x == y) return x;
  for (int i = logn; i >= 0; --i)
    if (p[i][x] != p[i][y]) x = p[i][x], y = p[i][y];
  return p[0][x];
}
inline int LCA2(int x, int y) {
  for (int i = logn; i >= 0; --i)
    if (dep[x] < dep[p[i][y]]) y = p[i][y];
  return y;
}
vector<pair<int, int> > Q[100100 + 1];
int q, ans[100100 + 1], seq[100100 + 1], cnt = 0;
DP pre[100100 + 1], suf[100100 + 1];
struct BIT {
  hashInt a[100100 + 1];
  inline void modify(int x, hashInt w) {
    for (; x <= n; x += x & -x) a[x] = a[x] + w;
  }
  inline hashInt query(int x) {
    hashInt r = 0;
    for (; x > 0; x -= x & -x) r = r + a[x];
    return r;
  }
} sufsum, sufsqr;
void dfs(int x, int f) {
  for (int i = 0; i < Q[x].size(); ++i) {
    int node = Q[x][i].first, id = Q[x][i].second;
    int p = LCA(x, node);
    hashInt b = dis[node] - dis[p];
    b = b * b;
  }
  for (int i = head[x]; i; i = e[i].next) {
    int node = e[i].node;
    if (node == f) continue;
    seq[++cnt] = x;
    pre[cnt].sum = pre[cnt - 1].sum + e[i].w * (cnt - 1);
    pre[cnt].sqr = delta(pre[cnt - 1], cnt - 1, e[i].w);
    dfs(node, x);
    --cnt;
  }
}
int main(int argc, char *argv[]) {
  scanf("%d", &n);
  for (int i = 1; i < n; ++i) {
    int x, y, w;
    scanf("%d%d%d", &x, &y, &w);
    addedge(x, y, w), addedge(y, x, w);
  }
  preUp(1, 0);
  preDown(1, 0);
  dep[1] = 1, preDA(1, 0);
  logn = (int)(log((double)n) / log(2.0));
  for (int i = 1; i <= logn; ++i)
    for (int j = 1; j <= n; ++j) p[i][j] = p[i - 1][p[i - 1][j]];
  scanf("%d", &q);
  while (q--) {
    int x, y;
    scanf("%d%d", &x, &y);
    int p = LCA(x, y);
    hashInt d = dis[x] + dis[y] - dis[p] * 2;
    hashInt ans = 0;
    if (p == y) {
      ans = delta(down[y], n - size[y], d);
      ans = up[x].sqr + down[x].sqr - ans * 2;
    } else {
      ans = delta(up[y], size[y], d);
      ans = ans * 2 - up[x].sqr - down[x].sqr;
    }
    printf("%d\n", ans.x);
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
