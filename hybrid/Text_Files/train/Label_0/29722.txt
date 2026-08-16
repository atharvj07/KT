#include <bits/stdc++.h>
using namespace std;
struct BIT {
  vector<int> t;
  int gb;
  BIT(int n) {
    t.assign(n + 1, 0);
    gb = 1;
    while (gb < n) gb <<= 1;
    if (gb > n) gb = gb >>= 1;
  }
  int query(int idx) {
    int sum = 0;
    for (; idx; idx -= idx & -idx) sum += t[idx];
    return sum;
  }
  void add(int idx, int val) {
    for (; idx < (int)t.size(); idx += idx & -idx) t[idx] += val;
  }
  int find(int cf) {
    int idx = 0, bm = gb;
    while (bm) {
      int tidx = idx + bm;
      if (tidx < (int)t.size() && cf > t[tidx]) {
        idx = tidx;
        cf -= t[tidx];
      }
      bm >>= 1;
    }
    return idx + 1;
  }
};
int main() {
  int n, m;
  while (cin >> n >> m) {
    BIT b(n);
    vector<int> a(m + 1), E(n + 1);
    for (int i = 1; i <= m; ++i) cin >> a[i];
    int sz = 0;
    for (int i = 1; i <= n; ++i) {
      int e;
      cin >> e;
      E[i] = e;
      if (e == -1) {
        int k = upper_bound(a.begin() + 1, a.end(), sz) - a.begin();
        --k;
        sz -= k;
        for (int j = k; j > 0; --j) {
          b.add(b.find(a[j]), -1);
        }
      } else {
        ++sz;
        b.add(i, 1);
      }
    }
    if (sz) {
      for (int i = 1; i <= sz; ++i) {
        cout << E[b.find(i)];
      }
      cout << endl;
    } else
      cout << "Poor stack!" << endl;
  }
  return 0;
}
