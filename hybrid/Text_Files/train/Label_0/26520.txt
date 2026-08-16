#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast")
const long long maxn = 2e5 + 50, N = 2e4 + 10, SQRT = 300, base = 607583,
                mod = 1e9 + 7, INF = 1e14 + 1, lg = 25;
const long double eps = 1e-4;
struct node {
  pair<long long, long long> last;
  node() { last = {-1, -1}; }
};
node seg[4 * maxn];
long long n, m, a[maxn], b[maxn], tme;
inline void shift(long long v, long long s, long long e) {
  if (seg[v].last.first > seg[2 * v].last.first) {
    seg[2 * v].last = seg[v].last;
  }
  if (seg[v].last.first > seg[2 * v + 1].last.first) {
    seg[2 * v + 1].last.first = seg[v].last.first;
    seg[2 * v + 1].last.second = seg[v].last.second + (s + e) / 2 - s;
  }
}
long long modify(long long l, long long r, long long val, long long v = 1,
                 long long s = 0, long long e = n) {
  if (l >= e || s >= r) {
    return 0;
  }
  if (l <= s && e <= r) {
    seg[v].last = {tme, val};
    return e - s;
  }
  shift(v, s, e);
  long long bef = modify(l, r, val, 2 * v, s, (s + e) / 2);
  long long aft = modify(l, r, val + bef, 2 * v + 1, (s + e) / 2, e);
  return bef + aft;
}
long long get(long long p, long long v = 1, long long s = 0, long long e = n) {
  if (e - s == 1) {
    if (seg[v].last.first == -1) {
      return b[s];
    }
    return a[seg[v].last.second];
  }
  shift(v, s, e);
  if (p < (s + e) / 2) {
    return get(p, 2 * v, s, (s + e) / 2);
  }
  return get(p, 2 * v + 1, (s + e) / 2, e);
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (long long i = 0; i < n; ++i) {
    cin >> a[i];
  }
  for (long long j = 0; j < n; ++j) {
    cin >> b[j];
  }
  while (m--) {
    long long type, l1, l2, sz;
    cin >> type;
    if (type == 1) {
      cin >> l1 >> l2 >> sz;
      l1--;
      l2--;
      modify(l2, l2 + sz, l1);
    } else {
      cin >> l2;
      l2--;
      cout << get(l2) << '\n';
    }
    tme++;
  }
}
