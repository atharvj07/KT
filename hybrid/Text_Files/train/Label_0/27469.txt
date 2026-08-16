#include <bits/stdc++.h>
using namespace std;
using ull = uint64_t;
using ll = int64_t;
using ld = long double;
const int N = 5002;
int d[N];
int c[N];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  cout.setf(ios::fixed);
  cout.precision(20);
  int n, m;
  cin >> n >> m;
  fill(d, d + n, N);
  for (int i = 0; i < m; ++i) {
    int a, b;
    cin >> a >> b;
    --a, --b;
    int ds = b - a;
    if (ds < 0) {
      ds += n;
    }
    ++c[a];
    d[a] = min(d[a], ds);
  }
  for (int i = 0; i < n; ++i) {
    int ans = 0;
    for (int j = 0; j < n; ++j) {
      int k = (i + j) % n;
      if (c[k]) {
        ans = max(ans, (c[k] - 1) * n + j + d[k]);
      }
    }
    cout << ans << " ";
  }
}
