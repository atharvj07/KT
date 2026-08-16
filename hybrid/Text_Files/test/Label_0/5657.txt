#include <bits/stdc++.h>
using namespace std;
int a[300010], pre[300010], pos[300010];
int n;
int max_[1200010];
int f(int x, int y) {
  if (a[x] > a[y]) return x;
  return y;
}
void pushup(int rt) { max_[rt] = f(max_[rt << 1], max_[rt << 1 | 1]); }
void build(int l, int r, int rt) {
  if (l == r) {
    max_[rt] = l;
    return;
  }
  int m = l + r >> 1;
  build(l, m, rt << 1);
  build(m + 1, r, rt << 1 | 1);
  pushup(rt);
}
int query(int L, int R, int l, int r, int rt) {
  if (L <= l && r <= R) return max_[rt];
  int m = l + r >> 1;
  int ans = 0;
  if (m >= L) ans = f(ans, query(L, R, l, m, rt << 1));
  if (m < R) ans = f(ans, query(L, R, m + 1, r, rt << 1 | 1));
  return ans;
}
long long solve(int l, int r) {
  if (l == r) {
    if (a[l] == 1) return 1;
    return 0;
  }
  if (l > r) return 0;
  int mid = query(l, r, 1, n, 1);
  int i;
  long long ans = 0;
  if (mid - l < r - mid) {
    for (i = l; i <= mid; i++) {
      if (i + a[mid] - 1 < mid) continue;
      if (i + a[mid] - 1 > r) break;
      if (pre[i + a[mid] - 1] < i) ans++;
    }
  } else {
    for (i = r; i >= mid; i--) {
      if (i - a[mid] + 1 > mid) continue;
      if (i - a[mid] + 1 < l) break;
      if (pre[i] < i - a[mid] + 1) ans++;
    }
  }
  ans += solve(l, mid - 1);
  ans += solve(mid + 1, r);
  return ans;
}
int main() {
  scanf("%d", &n);
  int i;
  for (i = 1; i <= n; i++) {
    scanf("%d", &a[i]);
    pre[i] = pos[a[i]];
    pre[i] = max(pre[i], pre[i - 1]);
    pos[a[i]] = i;
  }
  long long ans = 0;
  build(1, n, 1);
  ans = solve(1, n);
  printf("%lld\n", ans);
  return 0;
}
