#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 5, maxm = 1e4 + 5, maxe = maxn * 4 + maxm,
          maxp = 4 * maxe;
int n, m, b[maxe], id[maxe], tot, cnt, d;
double p[maxp], ans;
int read() {
  int ret = 0, f = 1;
  char ch = getchar();
  while (ch > '9' || ch < '0') {
    if (ch == '-') f = -f;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') ret = ret * 10 + ch - '0', ch = getchar();
  return ret * f;
}
struct tree {
  int x, h, l, r;
} a[maxn];
struct mogu {
  int x, v;
} c[maxn];
int find(int x) {
  int L = 1, R = cnt, mid;
  while (L <= R) {
    mid = L + R >> 1;
    if (id[mid] == x) return mid;
    id[mid] < x ? L = mid + 1 : R = mid - 1;
  }
}
void build(int l, int r, int k) {
  p[k] = 1, d++;
  if (l == r) return;
  int mid = l + r >> 1;
  build(l, mid, k << 1), build(mid + 1, r, k << 1 | 1);
}
void change(int L, int R, int k, int l, int r, double x) {
  if (L > r || R < l) return;
  if (l <= L && R <= r) {
    p[k] *= x / 100.0;
    return;
  }
  if (L == R) return;
  int mid = L + R >> 1;
  change(L, mid, k << 1, l, r, x), change(mid + 1, R, k << 1 | 1, l, r, x);
}
double ask(int l, int r, int k, int x) {
  if (l == r) return p[k];
  int mid = l + r >> 1;
  if (mid >= x)
    return ask(l, mid, k << 1, x) * p[k];
  else
    return ask(mid + 1, r, k << 1 | 1, x) * p[k];
}
int main() {
  n = read(), m = read();
  for (int i = 1; i <= n; i++) {
    a[i].x = read(), a[i].h = read(), a[i].l = read(), a[i].r = read();
    b[++tot] = a[i].x - a[i].h, b[++tot] = a[i].x - 1, b[++tot] = a[i].x + 1,
    b[++tot] = a[i].x + a[i].h;
  }
  for (int i = 1; i <= m; i++) {
    c[i].x = read(), c[i].v = read();
    b[++tot] = c[i].x;
  }
  sort(b + 1, b + 1 + tot);
  for (int i = 1; i <= tot; i++)
    if (b[i] != b[i + 1]) id[++cnt] = b[i];
  build(1, cnt, 1);
  for (int i = 1; i <= n; i++) {
    int L = find(a[i].x - a[i].h), midl = find(a[i].x - 1),
        midr = find(a[i].x + 1), R = find(a[i].x + a[i].h);
    change(1, cnt, 1, L, midl, (double)100.0 - a[i].l),
        change(1, cnt, 1, midr, R, (double)100.0 - a[i].r);
  }
  for (int i = 1; i <= m; i++) {
    int x = find(c[i].x);
    ans += (double)ask(1, cnt, 1, x) * c[i].v;
  }
  printf("%.10lf\n", ans);
  return 0;
}
