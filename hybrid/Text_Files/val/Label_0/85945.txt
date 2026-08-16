#include <bits/stdc++.h>
using namespace std;
template <typename G>
struct triple {
  G first, second, T;
};
struct segment_tree {
  vector<int> st;
  vector<int> lazy;
  segment_tree(int n) : st(2 * n), lazy(2 * n) {}
  inline int id(int b, int e) { return (b + e - 1) | (b != e - 1); }
  void prop(int l, int r) {
    int cur = id(l, r);
    st[cur] += lazy[cur];
    if (l != r - 1) {
      int mid = (l + r + 1) >> 1;
      lazy[id(l, mid)] += lazy[cur];
      lazy[id(mid, r)] += lazy[cur];
    }
    lazy[cur] = 0;
  }
  void sum(int l, int r, int li, int ri, int v) {
    if (li == ri) return;
    int cur = id(l, r);
    if (lazy[cur]) prop(l, r);
    if (l >= ri || r <= li) return;
    if (li <= l && r <= ri) {
      lazy[cur] += v;
      prop(l, r);
      return;
    }
    int mid = (l + r + 1) >> 1;
    sum(l, mid, li, ri, v);
    sum(mid, r, li, ri, v);
    st[cur] = max(st[id(l, mid)], st[id(mid, r)]);
  }
  int query(int l, int r, int li, int ri) {
    int cur = id(l, r);
    if (lazy[cur]) prop(l, r);
    if (l >= ri || r <= li) return 0;
    if (li <= l && r <= ri) return st[cur];
    int mid = (l + r + 1) >> 1;
    return max(query(0, mid, li, ri), query(mid, r, li, ri));
  }
};
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n, k;
  cin >> n >> k;
  vector<int> v(n);
  for (auto &i : v) cin >> i;
  vector<int> p(n + 1, -1);
  stack<int> s;
  for (int i = n - 1; i >= 0; i--) {
    while (!s.empty() && v[s.top()] <= v[i]) s.pop();
    if (!s.empty())
      p[i] = s.top();
    else
      p[i] = n;
    s.push(i);
  }
  ++n;
  vector<vector<int>> tree(n);
  for (int i = 0; i < n - 1; i++) tree[p[i]].push_back(i);
  vector<int> l(n), r(n);
  int t = 0;
  function<void(int)> dfs = [&](int c) {
    l[c] = t++;
    for (auto a : tree[c]) dfs(a);
    r[c] = t;
  };
  dfs(n - 1);
  segment_tree st(n);
  for (int i = 0; i < k; i++) st.sum(0, n, l[i], r[i], 1);
  for (int i = k; i < n - 1; i++) {
    cout << st.query(0, n, 0, n) << " ";
    st.sum(0, n, l[i - k], r[i - k], -1);
    st.sum(0, n, l[i], r[i], 1);
  }
  cout << st.query(0, n, 0, n) << '\n';
  return 0;
}
