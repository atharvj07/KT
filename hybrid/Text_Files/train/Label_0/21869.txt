#include <bits/stdc++.h>
using namespace std;
const long long N = 1e5 + 5;
long long n, s, sum;
struct E {
  long long v, w, c;
  E() {}
  E(long long v, long long w, long long c) : v(v), w(w), c(c) {}
};
vector<E> G[N];
vector<long long> p, q;
bool cmp(long long a, long long b) { return a > b; }
long long dfs(long long u, long long fa, long long w, long long c) {
  long long sz = 0;
  for (auto x : G[u]) {
    auto &v = x.v, &w = x.w, &c = x.c;
    if (v == fa) continue;
    sz += dfs(v, u, w, c);
  }
  if (!sz) sz = 1;
  sum += sz * w;
  if (c == 1)
    while (w * sz - w / 2 * sz) p.push_back(w * sz - w / 2 * sz), w /= 2;
  else
    while (w * sz - w / 2 * sz) q.push_back(w * sz - w / 2 * sz), w /= 2;
  return sz;
}
void solve() {
  p.clear(), q.clear();
  p.push_back(0), q.push_back(0);
  dfs(1, 0, 0, 0);
  long long cnt1 = 0, cnt2 = 0;
  sort(p.begin() + 1, p.end(), cmp);
  sort(q.begin() + 1, q.end(), cmp);
  for (long long i = 2; i < p.size(); i++) p[i] += p[i - 1];
  for (long long i = 2; i < q.size(); i++) q[i] += q[i - 1];
  long long res = 0x3f3f3f3f;
  sum -= s;
  for (long long i = 0, j = q.size() - 1; i < p.size(); i++) {
    bool f = false;
    while (j >= 0 && p[i] + q[j] >= sum) j--, f = true;
    if (f) j++;
    if (p[i] + q[j] >= sum) res = min(res, i + j * 2);
  }
  printf("%lld\n", res);
}
signed main() {
  long long T;
  scanf("%lld", &T);
  while (T--) {
    scanf("%lld%lld", &n, &s);
    sum = 0;
    for (long long i = 1; i <= n; i++) G[i].clear();
    for (long long i = 1; i < n; i++) {
      long long u, v, w, c;
      scanf("%lld%lld%lld%lld", &u, &v, &w, &c);
      G[u].push_back(E(v, w, c));
      G[v].push_back(E(u, w, c));
    }
    solve();
  }
  return 0;
}
