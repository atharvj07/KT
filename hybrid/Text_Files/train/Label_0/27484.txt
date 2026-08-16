#include <bits/stdc++.h>
using namespace std;
void build_sum(int i, int l, int r, long long *nodes, long long *val,
               long long (*add_fun)(long long, long long)) {
  if (l == r) {
    nodes[i] = val[l];
    return;
  } else {
    build_sum(i * 2, l, (l + r) / 2, nodes, val, add_fun);
    build_sum(i * 2 + 1, (l + r) / 2 + 1, r, nodes, val, add_fun);
    nodes[i] = add_fun(nodes[i * 2], nodes[i * 2 + 1]);
  }
}
long long query_sum(int i, int l, int r, int tl, int tr, long long *nodes,
                    long long (*add_fun)(long long, long long)) {
  if (r < tl || l > tr || l > r) return 0;
  if (l >= tl && r <= tr) {
    return nodes[i];
  }
  return add_fun(
      query_sum(i * 2, l, (l + r) / 2, tl, tr, nodes, add_fun),
      query_sum(i * 2 + 1, (l + r) / 2 + 1, r, tl, tr, nodes, add_fun));
}
long long query_sum_b(int i, int l, int r, int tl, int tr, long long *nodes,
                      long long (*add_fun)(long long, long long)) {
  if (r < tl || l > tr || l > r) return INT_MAX;
  if (l >= tl && r <= tr) {
    return nodes[i];
  }
  return add_fun(
      query_sum_b(i * 2, l, (l + r) / 2, tl, tr, nodes, add_fun),
      query_sum_b(i * 2 + 1, (l + r) / 2 + 1, r, tl, tr, nodes, add_fun));
}
void query_change_sum(int i, int l, int r, int target, long long *nodes,
                      long long value,
                      long long (*add_fun)(long long, long long)) {
  if (target < l || target > r) return;
  if (l == r) {
    nodes[i] = value;
    return;
  }
  query_change_sum(i * 2, l, (l + r) / 2, target, nodes, value, add_fun);
  query_change_sum(i * 2 + 1, (l + r) / 2 + 1, r, target, nodes, value,
                   add_fun);
  nodes[i] = add_fun(nodes[i * 2], nodes[i * 2 + 1]);
}
long long sum_fun(long long a, long long b) { return a + b; }
long long min_fun(long long a, long long b) { return min(a, b); }
const int maxn = 4 * 1e5 + 10;
const int maxt = (1 << 21) + 10;
const int maxv = maxn * 2 + 5;
long long a[maxn];
set<long long> ind[maxn];
map<long long, long long> CC;
pair<long long, long long> queries[maxn];
long long sum_tree[maxt];
long long min_tree[maxt];
long long I[maxv];
int main() {
  int n, q;
  cin >> n >> q;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    CC[a[i]] = 0;
  }
  for (int i = 0; i < q; i++) {
    long long p, x;
    cin >> p >> x;
    CC[x] = 0;
    queries[i].first = p;
    queries[i].second = x;
  }
  long long cnt = -1;
  for (auto it = CC.begin(); it != CC.end(); it++) {
    CC[it->first] = ++cnt;
    I[cnt] = LLONG_MAX;
  }
  for (int i = 0; i < n; i++) {
    int vplace = CC[a[i]];
    if (i != 0) {
      ind[vplace].insert(i);
      I[vplace] = min(I[vplace], (long long)i);
    }
  }
  build_sum(1, 0, n - 1, sum_tree, a, sum_fun);
  build_sum(1, 0, cnt, min_tree, I, min_fun);
  for (int i = 0; i < q; i++) {
    if (queries[i].first - 1 != 0) {
      int new_value = CC[queries[i].second];
      int last_value = CC[a[queries[i].first - 1]];
      ind[last_value].erase(queries[i].first - 1);
      ind[new_value].insert(queries[i].first - 1);
      int index_last;
      if (!ind[last_value].empty())
        index_last = (*ind[last_value].begin());
      else
        index_last = INT_MAX;
      int index_new;
      if (!ind[new_value].empty())
        index_new = (*ind[new_value].begin());
      else
        index_new = INT_MAX;
      query_change_sum(1, 0, cnt, last_value, min_tree, index_last, min_fun);
      query_change_sum(1, 0, cnt, new_value, min_tree, index_new, min_fun);
    }
    query_change_sum(1, 0, n - 1, queries[i].first - 1, sum_tree,
                     queries[i].second, sum_fun);
    a[queries[i].first - 1] = queries[i].second;
    if (a[0] == 0) {
      cout << 1 << '\n';
    } else {
      long long pi = a[0];
      bool done = 0;
      int j = 0;
      while (j < n) {
        auto v = CC.lower_bound(pi);
        if (v == CC.end()) break;
        int vv = v->second;
        j = query_sum_b(1, 0, cnt, vv, cnt, min_tree, min_fun);
        if (j == INT_MAX) break;
        long long sum = query_sum(1, 0, n - 1, 0, j - 1, sum_tree, sum_fun);
        if (a[j] == sum) {
          cout << j + 1 << '\n';
          done = 1;
          break;
        }
        pi = sum + a[j];
      }
      if (!done) {
        cout << -1 << '\n';
      }
    }
  }
}
