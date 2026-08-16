#include <bits/stdc++.h>
using namespace std;
int get() {
  char ch;
  while (ch = getchar(), (ch < '0' || ch > '9') && ch != '-')
    ;
  if (ch == '-') {
    int s = 0;
    while (ch = getchar(), ch >= '0' && ch <= '9') s = s * 10 + ch - '0';
    return -s;
  }
  int s = ch - '0';
  while (ch = getchar(), ch >= '0' && ch <= '9') s = s * 10 + ch - '0';
  return s;
}
const int N = 65;
const int mo = 1e9 + 7;
const int MAXN = 2e6;
long long js[100005];
int n, k;
int fa[N];
struct node {
  int x, y, v;
} a[N], p[N];
unsigned long long mi[70];
int m;
map<int, int> idx, idy;
int kx, ky;
long long c[N], tmp[N], s[N];
unsigned long long suf[N];
struct zt {
  unsigned long long u;
  int cnt, val;
} que[MAXN + 5];
map<unsigned long long, int> id[N];
bool vis[N];
int kth[N];
long long td[N];
int getfather(int x) { return fa[x] == x ? x : fa[x] = getfather(fa[x]); }
bool cmp(node a, node b) { return kth[a.x] < kth[b.x]; }
long long dec(long long x, long long y) { return x < y ? x - y + mo : x + y; }
long long add(long long x, long long y) {
  return x + y >= mo ? x + y - mo : x + y;
}
int num[N];
int getcnt(unsigned long long v) {
  int ret = 0;
  for (; v; v -= v & -v) ret++;
  return ret;
}
int main() {
  n = get();
  k = get();
  for (int i = 1; i <= k; i++) {
    a[i].x = get(), a[i].y = get(), a[i].v = get() - 1;
  }
  srand(20010419);
  random_shuffle(a + 1, a + 1 + k);
  for (int i = 1; i <= k; i++) fa[i] = i;
  js[0] = 1;
  for (int i = 1; i <= 100000; i++) js[i] = js[i - 1] * i % mo;
  for (int i = 1; i <= k; i++)
    for (int j = i + 1; j <= k; j++)
      if (a[i].x == a[j].x || a[i].y == a[j].y) {
        int fx = getfather(i), fy = getfather(j);
        fa[fy] = fx;
      }
  mi[0] = 1;
  for (int i = 1; i <= k; i++) mi[i] = mi[i - 1] * 2;
  c[0] = 1;
  for (int tp = 1; tp <= k; tp++)
    if (getfather(tp) == tp) {
      m = 0;
      idx.clear();
      idy.clear();
      kx = ky = 0;
      for (int i = 1; i <= k; i++)
        if (getfather(i) == tp) {
          if (!idx[a[i].x]) idx[a[i].x] = ++kx;
          if (!idy[a[i].y]) idy[a[i].y] = ++ky;
          p[++m].x = idx[a[i].x];
          p[m].y = idy[a[i].y];
          p[m].v = a[i].v;
        }
      if (kx < ky) {
        swap(kx, ky);
        for (int i = 1; i <= m; i++) swap(p[i].x, p[i].y);
      }
      for (int i = 1; i <= kx; i++) vis[num[i] = i] = td[i] = 0;
      for (int i = 1; i <= m; i++) td[p[i].x] |= mi[p[i].y];
      unsigned long long now = 0;
      for (int i = kx; i >= 1; i--) {
        int key = 0, cnt = 0;
        unsigned long long tp = 0;
        for (int j = 1; j <= kx; j++)
          if (!vis[j]) {
            if (!key || cnt > getcnt(now | td[j])) {
              tp = now | td[j];
              cnt = getcnt(tp);
              key = j;
            }
          }
        vis[key] = 1;
        now = tp;
        kth[num[i] = key] = i;
      }
      sort(p + 1, p + 1 + m, cmp);
      suf[m + 1] = 0;
      for (int i = m; i >= 1; i--) suf[i] = suf[i + 1] | mi[p[i].y];
      int he = 0, ta = 1;
      que[1].cnt = 0;
      que[1].val = 1;
      que[1].u = 0;
      int w = 1;
      for (int i = 1; i <= kx; i++) {
        for (int j = 0; j <= k; j++) id[j].clear();
        int qw = w;
        while (w <= m && p[w].x == num[i]) w++;
        int qt = ta;
        while (he < qt) {
          he++;
          unsigned long long nu = que[he].u;
          long long nv = que[he].val;
          int cnt = que[he].cnt;
          int to;
          if (id[cnt][nu & suf[w]])
            to = id[cnt][nu & suf[w]];
          else {
            to = ++ta;
            que[to].cnt = cnt;
            que[to].u = nu;
            que[to].val = 0;
            id[cnt][nu & suf[w]] = to;
          }
          que[to].val = add(que[to].val, nv);
          for (int x = qw; x <= w - 1; x++)
            if ((nu & mi[p[x].y]) == 0) {
              unsigned long long u_ = (nu ^ mi[p[x].y]) & suf[w];
              int to;
              if (id[cnt + 1][u_])
                to = id[cnt + 1][u_];
              else {
                to = ++ta;
                que[to].cnt = cnt + 1;
                que[to].u = nu ^ mi[p[x].y];
                que[to].val = 0;
                id[cnt + 1][u_] = to;
              }
              que[to].val = add(que[to].val, nv * p[x].v % mo);
            }
        }
      }
      for (int i = 0; i <= k; i++) tmp[i] = s[i] = 0;
      for (; he < ta;) {
        he++;
        s[que[he].cnt] = add(s[que[he].cnt], que[he].val);
      }
      for (int i = 0; i <= k; i++)
        for (int j = 0; j <= k - i; j++)
          tmp[i + j] = add(tmp[i + j], c[i] * s[j] % mo);
      for (int i = 0; i <= k; i++) c[i] = tmp[i];
    }
  long long ans = 0;
  for (int i = 0; i <= k; i++) ans = add(ans, c[i] * js[n - i] % mo);
  printf("%I64d\n", ans);
  return 0;
}
