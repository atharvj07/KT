#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
int n, head[N], cnt, base1, base2, base3, dfn[N], idx, idfn[N], sz[N], fa[N];
int d[N], a[N];
unsigned long long hx[N];
struct edge {
  int to, nxt;
} e[N << 1];
struct data {
  unsigned long long val;
  int sz, l, r;
  inline bool operator<(const data& rhs) const {
    return val == rhs.val ? (sz == rhs.sz ? l < rhs.l : sz < rhs.sz)
                          : val < rhs.val;
  }
};
vector<data> vec;
void dfs(int now) {
  hx[now] = 0;
  idfn[dfn[now] = ++idx] = now;
  sz[now] = 1;
  for (int i = head[now]; i; i = e[i].nxt)
    if (!dfn[e[i].to]) {
      fa[e[i].to] = now;
      dfs(e[i].to);
      sz[now] += sz[e[i].to];
      hx[now] ^= hx[e[i].to] * base3 + base1;
    }
  hx[now] ^= (unsigned long long)sz[now] * base2 + 1;
  int l = dfn[now], r = dfn[now] + sz[now];
  vec.push_back((data){hx[now], sz[now], 1, l - 1});
  vec.push_back((data){hx[now], sz[now], r, n});
}
void dfs2(int now) {
  unsigned long long vx = hx[now],
                     nx = hx[now] ^ ((unsigned long long)sz[now] * base2 + 1);
  for (int i = head[now]; i; i = e[i].nxt)
    if (dfn[now] < dfn[e[i].to]) {
      hx[now] = nx ^ (hx[e[i].to] * base3 + base1);
      if (fa[now]) hx[now] ^= hx[fa[now]] * base3 + base1;
      hx[now] ^= (unsigned long long)(n - sz[e[i].to]) * base2 + 1;
      vec.push_back((data){hx[now], n - sz[e[i].to], dfn[e[i].to],
                           dfn[e[i].to] + sz[e[i].to] - 1});
      dfs2(e[i].to);
    }
  hx[now] = vx;
}
int main() {
  srand(time(0));
  base1 = rand() % 20000 + 10000, base2 = rand() % 30000 + 23333,
  base3 = rand() % 1919810 + 114514;
  scanf("%d", &n);
  for (int i = 1; i < n; ++i) {
    int u, v;
    scanf("%d%d", &u, &v);
    e[++cnt] = (edge){v, head[u]}, head[u] = cnt;
    e[++cnt] = (edge){u, head[v]}, head[v] = cnt;
  }
  idx = 0;
  vec.clear();
  dfs(1);
  dfs2(1);
  sort(vec.begin(), vec.end());
  data nw = vec[0];
  for (int i = 1; i <= vec.size(); ++i)
    if (i == vec.size() || nw.val != vec[i].val || nw.sz != vec[i].sz ||
        nw.r < vec[i].l) {
      ++d[nw.l], --d[nw.r + 1];
      nw = vec[i];
    } else
      nw.r = vec[i].r;
  for (int i = 1; i <= n; ++i) d[i] += d[i - 1];
  for (int i = 1; i <= n; ++i) a[i] = max(a[i], d[i]), d[i] = 0;
  printf("%d\n", idfn[max_element(a + 1, a + n + 1) - a]);
  return 0;
}
