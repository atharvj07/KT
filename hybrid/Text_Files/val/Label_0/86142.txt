#include <bits/stdc++.h>
using namespace std;
int n, q;
char s[200005];
struct SEGMENTTREE {
  int d, mx1, mx2, mx3, mx4, mx5;
} t[200005 << 2];
void maintain(int u) {
  t[u].d = t[u << 1].d + t[u << 1 | 1].d;
  t[u].mx1 = max(t[u << 1].mx1, t[u << 1].d + t[u << 1 | 1].mx1);
  t[u].mx2 = max(t[u << 1].mx2, -2 * t[u << 1].d + t[u << 1 | 1].mx2);
  t[u].mx3 = max(max(t[u << 1].mx3, -t[u << 1].d + t[u << 1 | 1].mx3),
                 t[u << 1].mx1 - 2 * t[u << 1].d + t[u << 1 | 1].mx2);
  t[u].mx4 = max(max(t[u << 1].mx4, -t[u << 1].d + t[u << 1 | 1].mx4),
                 t[u << 1].mx2 + t[u << 1].d + t[u << 1 | 1].mx1);
  t[u].mx5 = max(max(t[u << 1].mx5, t[u << 1 | 1].mx5),
                 max(t[u << 1].mx1 - t[u << 1].d + t[u << 1 | 1].mx4,
                     t[u << 1].mx3 + t[u << 1].d + t[u << 1 | 1].mx1));
}
void se(int u, int x) {
  if (s[x] == '(') {
    t[u] = (SEGMENTTREE){1, 1, 0, 0, 1, 1};
  } else {
    t[u] = (SEGMENTTREE){-1, 0, 2, 2, 1, 1};
  }
}
void build(int u, int l, int r) {
  if (l == r) {
    se(u, l);
    return;
  }
  int mid = (l + r) >> 1;
  build(u << 1, l, mid);
  build(u << 1 | 1, mid + 1, r);
  maintain(u);
}
void update(int u, int l, int r, int x) {
  if (l == r) {
    if (s[x] == '(')
      s[x] = ')';
    else
      s[x] = '(';
    se(u, x);
    return;
  }
  int mid = (l + r) >> 1;
  if (x <= mid)
    update(u << 1, l, mid, x);
  else
    update(u << 1 | 1, mid + 1, r, x);
  maintain(u);
}
int main() {
  scanf("%d%d%s", &n, &q, s + 1);
  build(1, 1, 2 * (n - 1));
  printf("%d\n", t[1].mx5);
  for (int x, y, i = 1; i <= q; i++) {
    scanf("%d%d", &x, &y);
    update(1, 1, 2 * (n - 1), x);
    update(1, 1, 2 * (n - 1), y);
    printf("%d\n", t[1].mx5);
  }
  return 0;
}
