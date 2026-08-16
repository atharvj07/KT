#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 5;
struct segNode {
  long long val;
  long long lazy;
  int l, r;
  segNode() { val = lazy = 0; }
  segNode(int a, int b, int c) {
    val = a;
    l = b;
    r = c;
    lazy = 0;
  }
};
int arr[N];
segNode segTree[4 * N];
void shift(int num, int left, int right) {
  int upd = segTree[num].lazy;
  segTree[num].val += upd;
  if (segTree[num].l != segTree[num].r) {
    segTree[left].lazy += upd;
    segTree[right].lazy += upd;
  }
  segTree[num].lazy = 0;
}
void build(int l, int r, int num) {
  if (l > r) return;
  if (l == r) {
    segTree[num] = segNode(arr[l], l, r);
    return;
  }
  int mid = (l + r) >> 1, left = num << 1, right = left | 1;
  build(l, mid, left);
  build(mid + 1, r, right);
  segTree[num] = segNode(min(segTree[left].val, segTree[right].val), l, r);
}
void update(int l, int r, int num, int lu, int ru, int inc) {
  if (l > r) return;
  int mid = (l + r) >> 1, left = num << 1, right = left | 1;
  if (segTree[num].lazy != 0) shift(num, left, right);
  if (l > ru || r < lu) return;
  if (l >= lu && r <= ru) {
    segTree[num].lazy += inc;
    shift(num, left, right);
    return;
  }
  update(l, mid, left, lu, ru, inc);
  update(mid + 1, r, right, lu, ru, inc);
  segTree[num].val = min(segTree[right].val, segTree[left].val);
}
long long query(int l, int r, int num, int lq, int rq) {
  if (l > r) return (long long)1e17;
  int mid = (l + r) >> 1, left = num << 1, right = left | 1;
  if (segTree[num].lazy != 0) shift(num, left, right);
  if (l > rq || r < lq) return (long long)1e17;
  if (l >= lq && r <= rq) {
    return segTree[num].val;
  }
  return min(query(l, mid, left, lq, rq), query(mid + 1, r, right, lq, rq));
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", arr + i);
  }
  build(0, n - 1, 1);
  int q;
  scanf("%d", &q);
  while (q--) {
    int x, y;
    char ch;
    scanf("%d%d%c", &x, &y, &ch);
    if (ch == ' ') {
      int v;
      scanf("%d", &v);
      if (x <= y)
        update(0, n - 1, 1, x, y, v);
      else
        update(0, n - 1, 1, x, n - 1, v), update(0, n - 1, 1, 0, y, v);
    } else {
      long long ans;
      if (x <= y)
        ans = query(0, n - 1, 1, x, y);
      else
        ans = min(query(0, n - 1, 1, x, n - 1), query(0, n - 1, 1, 0, y));
      printf("%lld\n", ans);
    }
  }
}
