#include <bits/stdc++.h>
using namespace std;
int n, q;
int p[200005];
struct node {
  int l, r;
  long long sum;
  int Min, Max;
  long long lazy;
} tree[200005 * 4];
void pushup(node& k, node& l, node& r) {
  k.sum = l.sum + r.sum;
  k.Min = min(l.Min, r.Min);
  k.Max = max(l.Max, r.Max);
}
void pushup(int x) { pushup(tree[x], tree[x << 1], tree[x << 1 | 1]); }
void build(int l, int r, int x = 1) {
  if (l == r) {
    tree[x] = {l, r, p[l], p[l], p[l], 0};
    return;
  }
  tree[x] = {l, r, 0, 0, 0, 0};
  int mid = (l + r) >> 1;
  build(l, mid, x << 1);
  build(mid + 1, r, x << 1 | 1);
  tree[x].sum = tree[x * 2].sum + tree[x * 2 + 1].sum;
  tree[x].Max = max(tree[x * 2].Max, tree[x * 2 + 1].Max);
  tree[x].Min = min(tree[x * 2].Min, tree[x * 2 + 1].Min);
}
void pushdown(node& op, long long lazy) {
  op.sum = lazy * (op.r - op.l + 1);
  op.Min = lazy;
  op.Max = lazy;
  op.lazy = lazy;
}
void pushdown(int x) {
  if (!tree[x].lazy) return;
  pushdown(tree[x << 1], tree[x].lazy);
  pushdown(tree[x << 1 | 1], tree[x].lazy);
  tree[x].lazy = 0;
}
int check(int l, int r, int& have, int x = 1) {
  if (l <= tree[x].l && r >= tree[x].r) {
    if (have < tree[x].Min) return 0;
    if (have >= tree[x].sum) {
      have -= tree[x].sum;
      return tree[x].r - tree[x].l + 1;
    }
    if (tree[x].l == tree[x].r) return 0;
  }
  pushdown(x);
  int mid = tree[x].l + tree[x].r >> 1;
  int res = 0;
  if (l <= mid) res += check(l, r, have, x << 1);
  if (r > mid) res += check(l, r, have, x << 1 | 1);
  return res;
}
void judge(int l, int r, int c, int x = 1) {
  if (l <= tree[x].l && r >= tree[x].r) {
    if (tree[x].Min >= c) return;
    if (tree[x].Max < c) {
      pushdown(tree[x], c);
      return;
    }
  }
  pushdown(x);
  int mid = tree[x].l + tree[x].r >> 1;
  if (l <= mid) judge(l, r, c, x << 1);
  if (r > mid) judge(l, r, c, x << 1 | 1);
  pushup(x);
}
int main() {
  cin >> n >> q;
  for (int i = 1; i <= n; i++) cin >> p[i];
  build(1, n);
  for (int i = 1; i <= q; i++) {
    int t, x, y;
    cin >> t >> x >> y;
    if (t == 1)
      judge(1, x, y);
    else
      cout << check(x, n, y) << endl;
  }
  return 0;
}
