#include <bits/stdc++.h>
using namespace std;
const int maxn = 200000 + 10;
struct Tree {
  int x, y;
  char op[5];
  void init() { scanf("%s%d%d", op, &x, &y); }
  int tl, tr;
  int mx;
} tree[maxn << 2];
set<int> xx[maxn];
int top[maxn], n, m;
void build(int id, int l, int r) {
  tree[id].tl = l;
  tree[id].tr = r;
  tree[id].mx = -1;
  if (l == r) return;
  int mid = (l + r) >> 1;
  build(id << 1, l, mid);
  build(id << 1 | 1, mid + 1, r);
}
void update(int id, int pos, int val, int y) {
  int l = tree[id].tl, r = tree[id].tr;
  if (l == r) {
    if (xx[pos].size())
      tree[id].mx = *(--xx[pos].end());
    else
      tree[id].mx = -1;
    return;
  }
  int mid = (l + r) >> 1;
  if (pos <= mid)
    update(id << 1, pos, val, y);
  else
    update(id << 1 | 1, pos, val, y);
  tree[id].mx = max(tree[id << 1].mx, tree[id << 1 | 1].mx);
}
int query(int id, int ql, int qr, int y) {
  int l = tree[id].tl, r = tree[id].tr;
  if (tree[id].mx <= y || ql > qr) {
    return -1;
  }
  int mid = (l + r) >> 1;
  if (l == r) return l;
  if (qr <= mid)
    return query(id << 1, ql, qr, y);
  else if (ql > mid)
    return query(id << 1 | 1, ql, qr, y);
  else {
    int tmp = query(id << 1, ql, mid, y);
    if (tmp != -1) return tmp;
    return query(id << 1 | 1, mid + 1, qr, y);
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    tree[i].init();
    top[i] = tree[i].x;
  }
  sort(top + 1, top + 1 + n);
  m = unique(top + 1, top + 1 + n) - (top + 1);
  build(1, 1, m);
  for (int i = 1; i <= n; i++) {
    int pos = lower_bound(top + 1, top + 1 + m, tree[i].x) - top;
    if (tree[i].op[0] == 'a') {
      xx[pos].insert(tree[i].y);
      update(1, pos, 1, tree[i].y);
    } else if (tree[i].op[0] == 'r') {
      xx[pos].erase(tree[i].y);
      update(1, pos, 1, tree[i].y);
    } else {
      int ans = query(1, pos + 1, m, tree[i].y);
      if (ans == -1)
        printf("-1\n");
      else
        printf("%d %d\n", top[ans], *xx[ans].upper_bound(tree[i].y));
    }
  }
  return 0;
}
