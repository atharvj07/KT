#include <bits/stdc++.h>
using namespace std;
mt19937 myrand(time(0));
bool isprime(long long n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  for (long long i = 5; i * i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) return false;
  }
  return true;
}
long long modexp(long long a, long long b, long long m) {
  long long r = 1;
  a = a % m;
  while (b > 0) {
    if (b & 1) r = (r * a) % m;
    b = b >> 1;
    a = (a * a) % m;
  }
  return r % m;
}
long long builtin_popcount(long long x) {
  long long cnt = 0;
  for (long long i = 60; i >= 0; i--) {
    if ((1LL << i) & x) cnt++;
  }
  return cnt;
}
long long addmod(long long a, long long b) {
  a %= 1000000007;
  b %= 1000000007;
  return (a + b) % 1000000007;
}
long long mulmod(long long a, long long b) {
  a %= 1000000007;
  b %= 1000000007;
  return (a * b) % 1000000007;
}
long long submod(long long a, long long b) {
  a %= 1000000007;
  b %= 1000000007;
  a -= b;
  if (a < 0) a += 1000000007;
  return a % 1000000007;
}
struct CustomCompare {
  bool operator()(long long a, long long b) { return a > b; }
};
const int mxn = 5e5 + 10;
long long inf = 1e18;
long long n, q;
long long tree[4 * mxn], lazy[4 * mxn], l[mxn], r[mxn], ans[mxn], dp[mxn],
    id[mxn];
long long e_start[mxn], e_end[mxn];
vector<pair<long long, long long>> g[mxn];
vector<long long> query[mxn];
long long nxt = 1;
void propagate(long long v, long long tl, long long tr, long long val) {
  tree[v] += val;
  if (tl != tr) {
    lazy[2 * v] += val;
    lazy[2 * v + 1] += val;
  }
  lazy[v] = 0;
}
void update(long long v, long long tl, long long tr, long long l, long long r,
            long long val) {
  propagate(v, tl, tr, lazy[v]);
  if (tl > r || l > tr) return;
  if (l <= tl && tr <= r) {
    propagate(v, tl, tr, val);
    return;
  }
  long long mid = tl + (tr - tl) / 2;
  update(2 * v, tl, mid, l, r, val);
  update(2 * v + 1, mid + 1, tr, l, r, val);
  tree[v] = min(tree[2 * v], tree[2 * v + 1]);
}
long long query_lr(long long v, long long tl, long long tr, long long l,
                   long long r) {
  propagate(v, tl, tr, lazy[v]);
  if (tl > r || l > tr) return inf;
  if (l <= tl && tr <= r) return tree[v];
  long long mid = tl + (tr - tl) / 2;
  return min(query_lr(2 * v, tl, mid, l, r),
             query_lr(2 * v + 1, mid + 1, tr, l, r));
}
void dfs(long long src) {
  id[src] = e_start[src] = nxt;
  nxt++;
  if (src != 1 && g[src].size() == 0)
    update(1, 1, n, id[src], id[src], dp[src]);
  else
    update(1, 1, n, id[src], id[src], inf);
  for (auto x : g[src]) {
    long long to = x.first, w = x.second;
    dp[to] = dp[src] + x.second;
    dfs(to);
  }
  e_end[src] = nxt - 1;
}
void dfs2(long long src) {
  for (auto x : query[src]) {
    ans[x] = query_lr(1, 1, n, l[x], r[x]);
  }
  for (auto x : g[src]) {
    long long to = x.first, w = x.second;
    update(1, 1, n, e_start[to], e_end[to], -w);
    if (e_start[to] >= 2) update(1, 1, n, 1, e_start[to] - 1, w);
    if (e_end[to] + 1 <= n) update(1, 1, n, e_end[to] + 1, n, w);
    dfs2(to);
    update(1, 1, n, e_start[to], e_end[to], w);
    if (e_start[to] >= 2) update(1, 1, n, 1, e_start[to] - 1, -w);
    if (e_end[to] + 1 <= n) update(1, 1, n, e_end[to] + 1, n, -w);
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> q;
  for (int i = 2; i < n + 1; i++) {
    long long par, weight;
    cin >> par >> weight;
    g[par].push_back({i, weight});
  }
  dfs(1);
  for (int i = 1; i < q + 1; i++) {
    long long v;
    cin >> v >> l[i] >> r[i];
    query[v].push_back(i);
  }
  dfs2(1);
  for (int i = 1; i < q + 1; i++) cout << ans[i] << "\n";
  return 0;
}
