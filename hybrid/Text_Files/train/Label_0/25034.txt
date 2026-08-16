#include <bits/stdc++.h>
using namespace std;
struct fenwick_tree_1D {
  long long n, log_n;
  vector<long long> tree;
  fenwick_tree_1D(long long _n)
      : n(_n), log_n((long long)(log2(_n) + 1.0L)), tree(_n + 5) {}
  void update(long long x, long long v) {
    while (x <= n) {
      tree[x] += v;
      x += x & (-x);
    }
  }
  long long prefix_sum(long long x) {
    long long r = 0;
    while (x) {
      r += tree[x];
      x -= x & (-x);
    }
    return r;
  }
  long long range_sum(long long l, long long r) {
    return prefix_sum(r) - prefix_sum(l - 1);
  }
};
const long long bs = 300;
fenwick_tree_1D bit(100005);
long long a[100005], nxt[100005], last[100005] = {0}, dl[2 * bs + 5],
                                  id[100005], dc = 0, result[100005] = {0};
set<long long> s[100005];
long long qc;
struct query {
  long long t, l, r, qno;
} q[bs + 5];
long long q2c;
struct query2 {
  long long l, r, qno;
} q2[bs + 5];
vector<long long> ans;
int32_t main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long n, m;
  cin >> n >> m;
  for (long long i = 1; i <= n; i++) {
    cin >> a[i];
    s[a[i]].insert(i);
  }
  for (long long h = 0; h < m; h += bs) {
    qc = min(bs, m - h);
    for (long long j = 0; j < qc; j++) {
      cin >> q[j].t >> q[j].l >> q[j].r;
      q[j].qno = h + j;
      if (q[j].t == 1) {
        if (!id[a[q[j].l]]) dl[dc] = a[q[j].l], id[a[q[j].l]] = 1, dc++;
        if (!id[q[j].r]) dl[dc] = q[j].r, id[q[j].r] = 1, dc++;
      } else
        q2[q2c].l = q[j].l, q2[q2c].r = q[j].r, q2[q2c].qno = q[j].qno,
        ans.push_back(q[j].qno), q2c++;
    }
    for (long long i = n; i >= 1; i--) {
      if (id[a[i]]) {
        nxt[i] = 0;
        continue;
      }
      nxt[i] = last[a[i]];
      if (nxt[i]) bit.update(nxt[i], nxt[i] - i);
      last[a[i]] = i;
    }
    sort(q2, q2 + q2c,
         [](const query2 &l, const query2 &r) { return l.l < r.l; });
    long long pos = 1;
    for (long long i = 0; i < q2c; i++) {
      while (pos < q2[i].l) {
        if (id[a[pos]] || !nxt[pos]) {
          pos++;
          continue;
        }
        bit.update(nxt[pos], pos - nxt[pos]);
        pos++;
      }
      result[q2[i].qno] = bit.prefix_sum(q2[i].r);
    }
    for (long long i = 0; i < qc; i++) {
      if (q[i].t == 1) {
        s[a[q[i].l]].erase(q[i].l);
        a[q[i].l] = q[i].r;
        s[a[q[i].l]].insert(q[i].l);
      } else {
        for (long long j = 0; j < dc; j++) {
          auto it1 = s[dl[j]].lower_bound(q[i].l);
          auto it2 = s[dl[j]].upper_bound(q[i].r);
          if (it1 != s[dl[j]].end() && it2 != s[dl[j]].begin()) {
            it2--;
            if (*it2 > *it1) result[q[i].qno] += *it2 - *it1;
          }
        }
      }
    }
    for (long long i = 0; i < dc; i++) id[dl[i]] = 0;
    dc = 0;
    q2c = 0;
    for (long long i = 1; i <= n; i++) bit.tree[i] = 0, last[i] = 0;
  }
  for (auto &k : ans) cout << result[k] << "\n";
}
