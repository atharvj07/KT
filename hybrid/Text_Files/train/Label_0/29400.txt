#include <bits/stdc++.h>
using namespace std;
const int N = 4000009;
struct tree {
  long long Mul[4000009];
  long long Sub[4000009];
  void update(int left, int right, long long by) {
    internalUpdate(left, by, by * (left - 1));
    internalUpdate(right + 1, -by, -by * right);
  }
  void internalUpdate(int at, long long mul, long long sub) {
    while (at < N) {
      Mul[at] += mul;
      Sub[at] += sub;
      at += (at & -at);
    }
  }
  long long query(int at) {
    long long mul = 0, sub = 0;
    int start = at;
    while (at > 0) {
      mul += Mul[at];
      sub += Sub[at];
      at -= (at & -at);
    }
    return mul * start - sub;
  }
  long long rangeQuery(long long a, long long b) {
    return query(b) - query(a - 1);
  }
} rows, cols;
int main() {
  int n, m, k;
  cin >> n >> m >> k;
  int mode;
  int x1, y1, x2, y2, t;
  while (k--) {
    cin >> mode;
    if (mode == 0) {
      cin >> x1 >> y1 >> x2 >> y2 >> t;
      rows.update(x1, x2, (y2 - y1 + 1) * t * 1ll);
      cols.update(y1, y2, (x2 - x1 + 1) * t * 1ll);
    } else {
      cin >> x1 >> y1 >> x2 >> y2;
      cout << -rows.rangeQuery(1, n) + rows.rangeQuery(x1, x2) +
                  cols.rangeQuery(y1, y2)
           << endl;
    }
  }
  return 0;
}
