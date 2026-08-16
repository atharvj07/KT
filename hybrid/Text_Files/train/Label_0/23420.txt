#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9 + 10;
const int SZ = 1e6 + 10;
const int mod = 1e9 + 7;
const double PI = acos(-1);
const double eps = 1e-7;
long long read() {
  long long n = 0;
  char a = getchar();
  bool flag = 0;
  while (a > '9' || a < '0') {
    if (a == '-') flag = 1;
    a = getchar();
  }
  while (a <= '9' && a >= '0') {
    n = n * 10 + a - '0', a = getchar();
  }
  if (flag) n = -n;
  return n;
}
int n, q;
int a[SZ], maxr[SZ];
vector<int> g[SZ];
void build_graph() {
  stack<int> S;
  for (int i = 1; i <= n; i++) {
    while (S.size() && a[S.top()] <= a[i]) {
      maxr[S.top()] = i - 1;
      S.pop();
    }
    S.push(i);
  }
  while (S.size()) {
    maxr[S.top()] = n;
    S.pop();
  }
}
struct seg {
  int l, r;
  long long add, sum;
} tree[SZ * 4];
void update(int p) { tree[p].sum = tree[p << 1].sum + tree[p << 1 | 1].sum; }
void build(int p, int l, int r) {
  tree[p].l = l;
  tree[p].r = r;
  tree[p].add = 0;
  tree[p].sum = 0;
  if (l == r) return;
  int mid = l + r >> 1;
  build(p << 1, l, mid);
  build(p << 1 | 1, mid + 1, r);
}
void pushadd(int p, long long d) {
  tree[p].add += d;
  tree[p].sum += d * (tree[p].r - tree[p].l + 1);
}
void pushdown(int p) {
  if (tree[p].add) {
    pushadd(p << 1, tree[p].add);
    pushadd(p << 1 | 1, tree[p].add);
    tree[p].add = 0;
  }
}
void change(int p, int l, int r, long long d) {
  if (l <= tree[p].l && tree[p].r <= r) {
    pushadd(p, d);
    return;
  }
  pushdown(p);
  int mid = tree[p].l + tree[p].r >> 1;
  if (l <= mid) change(p << 1, l, r, d);
  if (mid < r) change(p << 1 | 1, l, r, d);
  update(p);
}
long long ask_sum(int p, int l, int r) {
  if (l <= tree[p].l && tree[p].r <= r) {
    return tree[p].sum;
  }
  pushdown(p);
  int mid = tree[p].l + tree[p].r >> 1;
  long long ans = 0;
  if (l <= mid) ans += ask_sum(p << 1, l, r);
  if (mid < r) ans += ask_sum(p << 1 | 1, l, r);
  return ans;
}
struct haha {
  int l, r, id;
} ask[SZ];
bool cmp(haha a, haha b) { return a.l < b.l; }
long long ans[SZ];
void work() {
  build_graph();
  build(1, 1, n);
  for (int i = 1; i <= n; i++) {
    change(1, i, maxr[i], 1);
  }
  sort(ask + 1, ask + 1 + q, cmp);
  for (int i = 1, j = 1; i <= q; i++) {
    while (j < ask[i].l) {
      change(1, j, maxr[j], -1);
      j++;
    }
    ans[ask[i].id] += ask_sum(1, ask[i].l, ask[i].r);
  }
}
int L[SZ], R[SZ];
int main() {
  n = read(), q = read();
  for (int i = 1; i <= n; i++) a[i] = read();
  for (int i = 1; i <= q; i++) L[i] = read();
  for (int i = 1; i <= q; i++) R[i] = read();
  for (int i = 1; i <= q; i++) {
    ask[i].l = L[i];
    ask[i].r = R[i];
    ask[i].id = i;
  }
  work();
  reverse(a + 1, a + 1 + n);
  for (int i = 1; i <= q; i++) {
    ask[i].l = n - R[i] + 1;
    ask[i].r = n - L[i] + 1;
    ask[i].id = i;
  }
  work();
  for (int i = 1; i <= q; i++) {
    printf("%lld ", ans[i] - (R[i] - L[i] + 1));
  }
}
