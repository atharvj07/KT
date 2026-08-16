#include <bits/stdc++.h>
using namespace std;
inline int re() {
  int x = 0, f = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = (x << 3) + (x << 1) + (ch ^ 48);
    ch = getchar();
  }
  return x * f;
}
long long gcd(long long a, long long b) {
  long long r;
  while (b) {
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}
long long kk(long long a, long long b) {
  long long sum = 1;
  while (b) {
    if (b) sum = sum * a;
    a = a * a;
    b >>= 1;
  }
  return sum;
}
int ly[300030 << 2], tree[300030 << 2], a[300030];
void pdd(int l, int r, int tr) {
  if (ly[tr]) {
    ly[2 * tr] += ly[tr];
    ly[2 * tr + 1] += ly[tr];
    int mid = (l + r) >> 1;
    tree[2 * tr] += (mid - l + 1) * ly[tr];
    tree[2 * tr + 1] += (r - mid) * ly[tr];
    ly[tr] = 0;
  }
}
void pup(int tr) { tree[tr] = tree[2 * tr] + tree[2 * tr + 1]; }
void upd(int l, int r, int L, int R, int tr) {
  if (L <= l && r <= R) {
    ly[tr] += 1;
    tree[tr] += (r - l + 1);
    return;
  }
  pdd(l, r, tr);
  int mid = (l + r) >> 1;
  if (L <= mid) upd(l, mid, L, R, 2 * tr);
  if (R > mid) upd(mid + 1, r, L, R, 2 * tr + 1);
  pup(tr);
}
int qry(int l, int r, int pos, int tr) {
  if (l == r) return tree[tr];
  pdd(l, r, tr);
  int mid = (l + r) >> 1;
  if (pos <= mid)
    return qry(l, mid, pos, 2 * tr);
  else
    return qry(mid + 1, r, pos, 2 * tr + 1);
}
vector<pair<int, int>> v[300030];
int e[300030];
int main() {
  int n = re(), q = re();
  for (int i = 1; i <= n; i++) {
    a[i] = re();
    a[i] = i - a[i];
    if (a[i] < 0) a[i] = 0x3f3f3f3f;
  }
  for (int i = 1; i <= q; i++) {
    int u = re(), r = re();
    r = n - r;
    v[r].push_back({u, i});
  }
  for (int i = 1; i <= n; i++) {
    int l = 1, r = i;
    int ans = -1;
    while (l <= r) {
      int mid = (l + r) >> 1;
      if (qry(1, n, mid, 1) >= a[i]) {
        ans = mid;
        l = mid + 1;
      } else
        r = mid - 1;
    }
    if (ans != -1) {
      upd(1, n, 1, ans, 1);
    }
    for (int j = 0; j < v[i].size(); j++) {
      int u = v[i][j].first;
      e[v[i][j].second] = qry(1, n, u + 1, 1);
    }
  }
  for (int i = 1; i <= q; i++) cout << e[i] << endl;
}
