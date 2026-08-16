#include <bits/stdc++.h>
using namespace std;
struct sgt {
  int l, r, mn, mm, tag;
  long long sum;
} c[200005 << 2];
int n;
long long ans;
int a[200005];
long long h[200005];
vector<int> x[200005];
void pd(int o) {
  if (c[o].tag) {
    c[o << 1].mm = c[o << 1].mn = c[o].tag;
    c[o << 1 | 1].mm = c[o << 1 | 1].mn = c[o].tag;
    c[o << 1].tag = c[o << 1 | 1].tag = c[o].tag;
    c[o << 1].sum = ((long long)c[o << 1].r - c[o << 1].l + 1) * c[o].tag;
    c[o << 1 | 1].sum =
        ((long long)c[o << 1 | 1].r - c[o << 1 | 1].l + 1) * c[o].tag;
    c[o].tag = 0;
  }
}
void build(int l, int r, int o) {
  c[o].l = l, c[o].r = r;
  if (l == r) {
    c[o].mn = c[o].sum = c[o].mm = l;
    return;
  }
  int mid = (l + r) >> 1;
  build(l, mid, o << 1);
  build(mid + 1, r, o << 1 | 1);
  c[o].mm = max(c[o << 1].mm, c[o << 1 | 1].mm);
  c[o].mn = min(c[o << 1].mn, c[o << 1 | 1].mn);
  c[o].sum = c[o << 1].sum + c[o << 1 | 1].sum;
}
void update(int l, int r, int k, int o) {
  if (l > r) return;
  if (l <= c[o].l && r >= c[o].r && k <= c[o].mn) return;
  if (l <= c[o].l && r >= c[o].r && k >= c[o].mm) {
    c[o].tag = k;
    c[o].mm = c[o].mn = c[o].tag;
    c[o].sum = ((long long)c[o].r - c[o].l + 1) * k;
    return;
  }
  pd(o);
  int mid = (c[o].l + c[o].r) >> 1;
  if (l > mid)
    update(l, r, k, o << 1 | 1);
  else if (r <= mid)
    update(l, r, k, o << 1);
  else {
    update(l, mid, k, o << 1);
    update(mid + 1, r, k, o << 1 | 1);
  }
  c[o].mm = max(c[o << 1].mm, c[o << 1 | 1].mm);
  c[o].mn = min(c[o << 1].mn, c[o << 1 | 1].mn);
  c[o].sum = c[o << 1].sum + c[o << 1 | 1].sum;
}
int main() {
  scanf("%d", &n);
  h[0] = 3;
  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
  for (int i = 1; i <= n; ++i) {
    int t = sqrt(a[i]);
    for (int j = 1; j <= t; ++j) {
      if (a[i] % j == 0) {
        x[j].push_back(i);
        if (j * j != a[i]) x[a[i] / j].push_back(i);
      }
    }
  }
  build(1, n, 1);
  for (int i = 200000; i >= 1; --i) {
    h[i] = (long long)n * n - c[1].sum + n;
    if (x[i].size() <= 1)
      continue;
    else {
      update(1, x[i][0], x[i][x[i].size() - 2], 1);
      update(x[i][0] + 1, x[i][1], x[i][x[i].size() - 1], 1);
      update(x[i][1] + 1, n, n + 1, 1);
    }
  }
  for (int i = 200000; i >= 1; --i)
    ans = ans + (long long)i * (h[i] - h[i - 1]);
  printf("%lld", ans);
  return 0;
}
