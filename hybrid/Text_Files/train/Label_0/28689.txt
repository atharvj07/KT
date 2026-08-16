#include <bits/stdc++.h>
inline int in() {
  int x;
  scanf("%d", &x);
  return x;
}
using namespace std;
constexpr int mod = 1e9 + 7, N = 3e5 + 7;
int a[N], ps[N], n;
struct node {
  int l, r, ans;
} seg[4 * N];
node make(node x, node y) {
  node ans;
  ans.l = x.l, ans.r = y.r, ans.ans = x.ans + y.ans;
  if (x.r < y.l) ans.ans--;
  return ans;
}
int pos[N];
int pis[N];
void build(int tag = 1, int s = 0, int e = n) {
  if (e - s == 1) {
    seg[tag].l = seg[tag].r = pis[s], seg[tag].ans = 1;
    return;
  }
  int mid = (s + e) / 2, L = tag * 2, R = tag * 2 + 1;
  build(L, s, mid);
  build(R, mid, e);
  seg[tag] = make(seg[L], seg[R]);
}
node query(int l, int r, int tag = 1, int s = 0, int e = n) {
  int mid = (s + e) / 2, L = tag * 2, R = tag * 2 + 1;
  bool b1 = !(s >= r || mid <= l);
  bool b2 = !(mid >= r || e <= l);
  if (s >= l && e <= r) {
    return seg[tag];
  }
  if (b1 && b2)
    return make(query(l, r, L, s, mid), query(l, r, R, mid, e));
  else if (b1)
    return query(l, r, L, s, mid);
  else
    return query(l, r, R, mid, e);
}
void update(int idx, int nw, int tag = 1, int s = 0, int e = n) {
  if (e - s == 1) {
    seg[tag].l = seg[tag].r = nw, seg[tag].ans = 1;
    return;
  }
  int L = tag * 2, R = tag * 2 + 1, mid = (s + e) / 2;
  if (idx < mid)
    update(idx, nw, L, s, mid);
  else
    update(idx, nw, R, mid, e);
  seg[tag] = make(seg[L], seg[R]);
}
int32_t main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    int x = in() - 1;
    pos[i] = x;
    pis[x] = i;
  }
  build();
  int Q = in();
  while (Q--) {
    if (in() == 1) {
      int l = in() - 1, r = in();
      cout << query(l, r).ans << endl;
    } else {
      int x = in() - 1, y = in() - 1;
      update(pos[x], y);
      update(pos[y], x);
      swap(pos[x], pos[y]);
    }
  }
}
