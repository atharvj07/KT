#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10;
map<pair<int, int>, int> ma;
int n, q;
int f[N], d[N], st[N], top, str[N], ran[N];
inline int read() {
  char ch = getchar();
  int x = 0, f = 1;
  while (ch < '0' || ch > '9') {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = (x << 1) + (x << 3) - '0' + ch;
    ch = getchar();
  }
  return x * f;
}
int find(int x) {
  for (; x != f[x]; x = f[x])
    ;
  return x;
}
int getd(int x) {
  int ret = 0;
  for (; x != f[x]; ret ^= d[x], x = f[x])
    ;
  return ret;
}
struct edge {
  int l, r, s, t;
};
vector<edge> e;
int cnt;
int ans[N];
int res[N];
void merge(int u, int v, int w) {
  ++top;
  if (ran[u] < ran[v]) swap(u, v);
  if (ran[u] == ran[v])
    ++ran[u], str[top] = u;
  else
    str[top] = 0;
  st[top] = v;
  f[v] = u;
  d[v] = w;
}
void clr() {
  if (str[top]) --ran[str[top]];
  f[st[top]] = st[top];
  d[st[top]] = 0;
  --top;
}
void solve(int l, int r, vector<edge> e) {
  int mid = l + r >> 1, now = top;
  vector<edge> L, R;
  for (int i = 0; i < e.size(); i++) {
    if (e[i].s <= l && e[i].t >= r) {
      int fu = find(e[i].l), fv = find(e[i].r);
      int w = getd(e[i].l) ^ getd(e[i].r) ^ 1;
      if (fu != fv)
        merge(fu, fv, w);
      else if (w & 1) {
        for (int i = l; i <= r; i++) ans[i] = false;
        while (top > now) clr();
        return;
      }
    } else {
      if (e[i].s <= mid) L.push_back(e[i]);
      if (e[i].t > mid) R.push_back(e[i]);
    }
  }
  if (l == r) return;
  solve(l, mid, L);
  solve(mid + 1, r, R);
  while (top > now) clr();
}
int main() {
  n = read(), q = read();
  for (int i = 1; i <= n; i++) f[i] = i;
  for (int i = 1; i <= q; i++) {
    ans[i] = 1;
    int x = read(), y = read();
    if (x > y) swap(x, y);
    if (ma[{x, y}] == 0) {
      ++cnt;
      e.push_back({x, y, i});
      ma[{x, y}] = cnt;
    } else {
      e[ma[{x, y}] - 1].t = i - 1;
      ma[{x, y}] = 0;
    }
  }
  for (auto &j : e) {
    if (j.t == 0) {
      j.t = q;
    }
  }
  solve(1, q, e);
  for (int i = 1; i <= q; i++) {
    if (ans[i]) {
      puts("YES");
    } else {
      puts("NO");
    }
  }
}
