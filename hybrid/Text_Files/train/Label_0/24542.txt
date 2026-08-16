#include <bits/stdc++.h>
using namespace std;
vector<pair<int, int> > adj[500005];
long long D[500005];
long long seg[500005 * 4], lazy[500005 * 4];
void init(int pos, int l, int r) {
  if (l == r) {
    seg[pos] = D[l];
    return;
  }
  int mid = (l + r) / 2;
  init(pos * 2, l, mid);
  init(pos * 2 + 1, mid + 1, r);
  seg[pos] = min(seg[pos * 2], seg[pos * 2 + 1]);
}
void push(int pos, int l, int r) {
  if (lazy[pos] != 0) {
    seg[pos] += lazy[pos];
    if (l != r) {
      lazy[pos * 2] += lazy[pos];
      lazy[pos * 2 + 1] += lazy[pos];
    }
    lazy[pos] = 0;
  }
}
void update(int pos, int l, int r, int ql, int qr, int val) {
  push(pos, l, r);
  if (qr < l || r < ql) {
    return;
  }
  if (ql <= l && r <= qr) {
    lazy[pos] += val;
    push(pos, l, r);
    return;
  }
  int mid = (l + r) / 2;
  update(pos * 2, l, mid, ql, qr, val);
  update(pos * 2 + 1, mid + 1, r, ql, qr, val);
  seg[pos] = min(seg[pos * 2], seg[pos * 2 + 1]);
}
long long query(int pos, int l, int r, int ql, int qr) {
  push(pos, l, r);
  if (qr < l || r < ql) {
    return 1000000000000000LL;
  }
  if (ql <= l && r <= qr) {
    return seg[pos];
  }
  int mid = (l + r) / 2;
  return min(query(pos * 2, l, mid, ql, qr),
             query(pos * 2 + 1, mid + 1, r, ql, qr));
}
int pos = 1;
int L[500005], R[500005];
long long out[500005];
vector<pair<int, pair<int, int> > > offQuery[500005];
void dfs2(int node, int n) {
  for (pair<int, pair<int, int> > q : offQuery[node]) {
    int id = q.first;
    int l = q.second.first, r = q.second.second;
    out[id] = query(1, 1, n, l, r);
  }
  for (pair<int, int> edge : adj[node]) {
    int ch = edge.first, w = edge.second;
    update(1, 1, n, 1, n, w);
    update(1, 1, n, L[ch], R[ch], -2 * w);
    dfs2(edge.first, n);
    update(1, 1, n, 1, n, -w);
    update(1, 1, n, L[ch], R[ch], 2 * w);
  }
}
void dfs(int node, long long depth) {
  L[node] = pos++;
  if (adj[node].size() == 0) {
    D[L[node]] = depth;
  }
  for (pair<int, int> edge : adj[node]) {
    dfs(edge.first, depth + edge.second);
  }
  R[node] = pos - 1;
}
void solve() {
  int n, q;
  scanf("%d %d ", &n, &q);
  for (int i = 1; i <= n; ++i) {
    D[i] = 1000000000000000LL;
  }
  for (int i = 2; i <= n; ++i) {
    int p, w;
    scanf("%d %d ", &p, &w);
    adj[p].push_back({i, w});
  }
  for (int i = 0; i < q; ++i) {
    int v, l, r;
    scanf("%d %d %d ", &v, &l, &r);
    offQuery[v].push_back({i, {l, r}});
  }
  dfs(1, 0LL);
  init(1, 1, n);
  dfs2(1, n);
  for (int i = 0; i < q; ++i) {
    printf("%lld\n", out[i]);
  }
}
int main() {
  solve();
  return 0;
}
