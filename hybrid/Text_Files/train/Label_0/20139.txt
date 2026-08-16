#include <bits/stdc++.h>
using namespace std;
long long inf = 1000000007;
const long long maxinput = 200005;
long long n, a[maxinput];
vector<pair<long long, long long>> adj[maxinput];
long long d[maxinput];
long long arr[maxinput];
long long sz[maxinput];
long long flattree[maxinput];
pair<long long, long long> query[maxinput];
long long dfs(long long u, long long par, long long curr_dist) {
  long long v, w;
  d[u] = curr_dist;
  sz[u] = 1;
  for (long long j = 0; j < adj[u].size(); j++) {
    v = adj[u][j].first;
    w = adj[u][j].second;
    if (v != par) sz[u] += dfs(v, u, curr_dist + w);
  }
  return (sz[u]);
}
long long index_in_flattree = 0;
void flatten(long long u, long long par) {
  query[u] = make_pair(index_in_flattree, index_in_flattree + sz[u] - 1);
  flattree[index_in_flattree] = arr[u];
  index_in_flattree++;
  long long v;
  for (long long j = 0; j < adj[u].size(); j++) {
    v = adj[u][j].first;
    if (v != par) flatten(v, u);
  }
}
vector<long long> msorttree[4 * maxinput + 5];
void buildtree(long long l, long long r, long long k) {
  if (l == r) {
    msorttree[k].push_back(flattree[l]);
    return;
  }
  long long mid = (l + r) / 2;
  buildtree(l, mid, 2 * k + 1);
  buildtree(mid + 1, r, 2 * k + 2);
  merge(msorttree[2 * k + 1].begin(), msorttree[2 * k + 1].end(),
        msorttree[2 * k + 2].begin(), msorttree[2 * k + 2].end(),
        back_inserter(msorttree[k]));
  return;
}
long long query_tree(long long l, long long r, long long ql, long long qr,
                     long long k, long long val) {
  if (r < ql || l > qr)
    return (0);
  else if (ql <= l && qr >= r) {
    long long idx = upper_bound(msorttree[k].begin(), msorttree[k].end(), val) -
                    msorttree[k].begin();
    return (idx);
  } else {
    long long mid = (l + r) / 2;
    long long ans1 = query_tree(l, mid, ql, qr, 2 * k + 1, val);
    long long ans2 = query_tree(mid + 1, r, ql, qr, 2 * k + 2, val);
    return (ans1 + ans2);
  }
}
signed main() {
  cin >> n;
  for (long long i = 1; i <= n; i++) cin >> a[i];
  for (long long i = 2; i <= n; i++) {
    long long v, w;
    cin >> v >> w;
    adj[v].push_back(make_pair(i, w));
    adj[i].push_back(make_pair(v, w));
  }
  dfs(1, 0, 0);
  for (long long i = 1; i <= n; i++) arr[i] = d[i] - a[i];
  flatten(1, 0);
  long long ans[maxinput];
  buildtree(0, n - 1, 0);
  for (long long i = 1; i <= n; i++)
    ans[i] = query_tree(0, n - 1, query[i].first, query[i].second, 0, d[i]) - 1;
  for (long long i = 1; i <= n; i++) cout << ans[i] << " ";
  cout << endl;
}
