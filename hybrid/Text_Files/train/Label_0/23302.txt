#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2e5 + 5;
int lson[MAXN << 5], rson[MAXN << 5], sum[MAXN << 5];
int T[MAXN];
int n, q, tot;
int update(int pre, int l, int r, int x) {
  int rt = ++tot;
  lson[rt] = lson[pre], rson[rt] = rson[pre], sum[rt] = sum[pre] + 1;
  if (l < r) {
    int mid = (l + r) / 2;
    if (x <= mid)
      lson[rt] = update(lson[pre], l, mid, x);
    else
      rson[rt] = update(rson[pre], mid + 1, r, x);
  }
  return rt;
}
int query(int u, int v, int l, int r, int i, int j) {
  if (i <= l && j >= r) return sum[v] - sum[u];
  int mid = (l + r) / 2;
  int ans = 0;
  if (i <= mid) {
    ans += query(lson[u], lson[v], l, mid, i, j);
  }
  if (j > mid) {
    ans += query(rson[u], rson[v], mid + 1, r, i, j);
  }
  return ans;
}
int ask(int x1, int x2, int y1, int y2) {
  if (x1 > x2 || y1 > y2) return 0;
  return query(T[x1 - 1], T[x2], 1, n, y1, y2);
}
int main(void) {
  while (cin >> n >> q) {
    tot = 0;
    memset(sum, 0, sizeof(sum));
    T[0] = 0;
    for (int i = 1; i <= n; i++) {
      int x;
      scanf("%d", &x);
      T[i] = update(T[i - 1], 1, n, x);
    }
    for (int i = 1; i <= q; i++) {
      int l, d, r, u;
      scanf("%d%d%d%d", &l, &d, &r, &u);
      long long ans = 0, tmp = ask(l, r, d, u);
      ans += (long long)ask(1, l - 1, 1, d - 1) * (ask(l, n, d, n) + tmp);
      ans += (long long)ask(l, r, 1, d - 1) * (ask(1, n, d, n) + tmp);
      ans += (long long)ask(r + 1, n, 1, d - 1) * (ask(1, r, d, n) + tmp);
      ans += (long long)ask(r + 1, n, d, u) * (ask(1, r, 1, n) + tmp);
      ans += (long long)ask(1, l - 1, d, u) * (ask(l, n, 1, n) + tmp);
      ans += (long long)ask(1, l - 1, u + 1, n) * (ask(l, n, 1, u) + tmp);
      ans += (long long)ask(l, r, u + 1, n) * (ask(1, n, 1, u) + tmp);
      ans += (long long)ask(r + 1, n, u + 1, n) * (ask(1, r, 1, u) + tmp);
      printf("%I64d\n", (ans + tmp * (tmp - 1)) / 2);
    }
  }
  return 0;
}
