#include <bits/stdc++.h>
using namespace std;
struct tree {
  int l, r;
  long long sum, ans, num;
} t[500010 << 2];
int a[100010], b[100010], tmp[500010], aa[500010];
int ask[100010][3];
int search(int x, int num) {
  int mi = 1, ma = num, Mid;
  while (mi <= ma) {
    Mid = (mi + ma) >> 1;
    if (aa[Mid] == x) return Mid;
    if (aa[Mid] < x)
      mi = Mid + 1;
    else
      ma = Mid - 1;
  }
}
void pushup(int p) {
  t[p].sum = t[(p << 1)].sum + t[((p << 1) | 1)].sum;
  t[p].num = t[(p << 1)].num + t[((p << 1) | 1)].num;
  t[p].ans = t[((p << 1) | 1)].sum * t[(p << 1)].num -
             t[((p << 1) | 1)].num * t[(p << 1)].sum + t[(p << 1)].ans +
             t[((p << 1) | 1)].ans;
}
void build(int p, int l, int r) {
  t[p].l = l, t[p].r = r, t[p].ans = t[p].sum = t[p].num = 0;
  if (l == r) return;
  build((p << 1), l, ((t[p].l + t[p].r) >> 1));
  build(((p << 1) | 1), ((t[p].l + t[p].r) >> 1) + 1, r);
}
void change(int p, int x, int val) {
  if (t[p].l == t[p].r) {
    if (val > 0) {
      t[p].num++;
      t[p].ans = 0;
      t[p].sum = aa[x];
    } else {
      t[p].num = 0;
      t[p].ans = 0;
      t[p].sum = 0;
    }
    return;
  }
  if (x > ((t[p].l + t[p].r) >> 1))
    change(((p << 1) | 1), x, val);
  else
    change((p << 1), x, val);
  pushup(p);
}
struct node {
  long long ans, num, sum;
};
node query(int p, int l, int r) {
  node tt;
  if (t[p].l == l && t[p].r == r) {
    tt.ans = t[p].ans;
    tt.sum = t[p].sum;
    tt.num = t[p].num;
    return tt;
  }
  if (l > ((t[p].l + t[p].r) >> 1))
    return query(((p << 1) | 1), l, r);
  else if (r <= ((t[p].l + t[p].r) >> 1))
    return query((p << 1), l, r);
  else {
    node t1 = query((p << 1), l, ((t[p].l + t[p].r) >> 1)),
         t2 = query(((p << 1) | 1), ((t[p].l + t[p].r) >> 1) + 1, r);
    tt.sum = t1.sum + t2.sum;
    tt.num = t1.num + t2.num;
    tt.ans = t1.ans + t2.ans + t2.sum * t1.num - t1.sum * t2.num;
    return tt;
  }
}
int main() {
  int n, m, i, num = 0;
  scanf("%d", &n);
  for (i = 1; i <= n; i++) {
    scanf("%d", &a[i]);
    b[i] = a[i];
    tmp[num++] = a[i];
  }
  scanf("%d", &m);
  for (i = 1; i <= m; i++) {
    scanf("%d%d%d", &ask[i][0], &ask[i][1], &ask[i][2]);
    if (ask[i][0] == 1) {
      b[ask[i][1]] += ask[i][2];
      tmp[num++] = b[ask[i][1]];
    } else {
      tmp[num++] = ask[i][1];
      tmp[num++] = ask[i][2];
    }
  }
  sort(tmp, tmp + num);
  aa[1] = tmp[0];
  int sum = 1;
  for (i = 1; i < num; i++) {
    if (tmp[i] != tmp[i - 1]) aa[++sum] = tmp[i];
  }
  build(1, 1, sum);
  for (i = 1; i <= n; i++) {
    int po = search(a[i], sum);
    change(1, po, 1);
  }
  for (i = 1; i <= m; i++) {
    if (ask[i][0] == 1) {
      int po = search(a[ask[i][1]], sum);
      change(1, po, -1);
      a[ask[i][1]] += ask[i][2];
      po = search(a[ask[i][1]], sum);
      change(1, po, 1);
    } else {
      int l = search(ask[i][1], sum), r = search(ask[i][2], sum);
      node an = query(1, l, r);
      printf("%I64d\n", an.ans);
    }
  }
  return 0;
}
