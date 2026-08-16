#include <bits/stdc++.h>
using namespace std;
const int N = 200005;
pair<int, int> c[N];
struct Node {
  int l, r, v;
  bool cv;
} a[N << 2];
void Build(int i, int l, int r) {
  a[i].l = l;
  a[i].r = r;
  a[i].cv = false;
  if (l == r) return;
  int mid = l + r >> 1;
  Build(i << 1, l, mid);
  Build(i << 1 | 1, mid + 1, r);
}
inline void PushUp(int i) { a[i].v = a[i << 1].v + a[i << 1 | 1].v; }
inline void PushDown(int i) {
  if (a[i].cv) {
    a[i << 1].cv = a[i << 1 | 1].cv = a[i].cv;
    a[i << 1].v = a[i << 1 | 1].v = 0;
    a[i].cv = false;
  }
}
void Mdf(int i, int x, int val) {
  if (a[i].l == x && a[i].r == x) {
    a[i].v = val;
    return;
  }
  PushDown(i);
  if (x <= a[i << 1].r)
    Mdf(i << 1, x, val);
  else
    Mdf(i << 1 | 1, x, val);
  PushUp(i);
}
void Cv(int i, int l, int r) {
  if (l <= a[i].l && a[i].r <= r) {
    a[i].cv = true;
    a[i].v = 0;
    return;
  }
  PushDown(i);
  if (l <= a[i << 1].r) Cv(i << 1, l, r);
  if (a[i << 1 | 1].l <= r) Cv(i << 1 | 1, l, r);
  PushUp(i);
}
int Qry(int i, int l, int r) {
  if (l <= a[i].l && a[i].r <= r) return a[i].v;
  PushDown(i);
  if (r <= a[i << 1].r)
    return Qry(i << 1, l, r);
  else if (a[i << 1 | 1].l <= l)
    return Qry(i << 1 | 1, l, r);
  else
    return Qry(i << 1, l, r) + Qry(i << 1 | 1, l, r);
}
struct Query {
  int l, r, id;
} q[N];
int ans[N];
inline bool cmp(const Query& q, const Query& w) { return q.l > w.l; }
int main() {
  int n;
  scanf("%d", &n);
  Build(1, 1, n);
  for (int i = 1; i <= n; i++) scanf("%d %d", &c[i].first, &c[i].second);
  c[n + 1].first = c[n].second;
  int m;
  scanf("%d", &m);
  for (int i = 1; i <= m; i++) {
    scanf("%d %d", &q[i].l, &q[i].r);
    q[i].id = i;
  }
  sort(q + 1, q + 1 + m, cmp);
  int pos = 1;
  for (int i = n; i >= 1; i--) {
    if (c[i].first + c[i].second >= c[i + 1].first) {
      int l = i + 1, r = n;
      while (l < r) {
        int mid = l + r + 1 >> 1;
        if (c[i].first + c[i].second >= c[mid].first)
          l = mid;
        else
          r = mid - 1;
      }
      Cv(1, i, l);
      if (l < n)
        Mdf(1, l + 1,
            min(Qry(1, l + 1, l + 1),
                c[l + 1].first - c[i].first - c[i].second));
    } else
      Mdf(1, i + 1, c[i + 1].first - c[i].first - c[i].second);
    while (q[pos].l == i) {
      ans[q[pos].id] = Qry(1, 1, q[pos].r);
      pos++;
    }
    if (pos > m) break;
  }
  for (int i = 1; i <= m; i++) printf("%d\n", ans[i]);
  return 0;
}
