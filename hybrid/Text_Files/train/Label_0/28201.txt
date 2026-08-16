#include <bits/stdc++.h>
using namespace std;
const long long N = 2e5 + 100, M = 2, LG = 30, base = 2;
const long long MOD = 1e9 + 7, mod = 1e9 + 9;
const long long INF = 1e9, inf = 1e18;
long long n, l, mid, r, mi, ma;
long long x, y, i, j;
long long a[N], b[N], c[N], d[N];
pair<long long, long long> p[M][N];
bool check;
long long solve(long long t) {
  for (int i = 1; i <= n; i++)
    a[i] = max(a[i - 1], p[t][i].second), c[i] = min(c[i - 1], p[t][i].second);
  for (int i = n; i >= 1; i--)
    b[i] = max(b[i + 1], p[t][i].second), d[i] = min(d[i + 1], p[t][i].second);
  l = -1, r = inf;
  while (r - l > 1) {
    mid = (l + r) >> 1, i = 1, j = 1;
    check = (1ll * (p[t][n].first - p[t][1].first) *
             (p[t][n].first - p[t][1].first)) <= mid;
    while (!check && i <= n) {
      while ((1ll * (p[t][i].first - p[t][j].first) *
              (p[t][i].first - p[t][j].first)) > mid) {
        j++;
      }
      mi = min(c[j - 1], d[i + 1]);
      ma = max(a[j - 1], b[i + 1]);
      check |= (1ll * (ma - mi) * (ma - mi)) <= mid &&
               max((1ll * (mi) * (mi)), (1ll * (ma) * (ma))) +
                       max((1ll * (p[t][i].first) * (p[t][i].first)),
                           (1ll * (p[t][j].first) * (p[t][j].first))) <=
                   mid;
      i++;
    }
    if (check)
      r = mid;
    else
      l = mid;
  }
  return r;
}
int main() {
  ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
  ;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> x >> y;
    p[0][i] = make_pair(x, y), p[1][i] = make_pair(y, x);
  }
  sort(p[0] + 1, p[0] + n + 1);
  sort(p[1] + 1, p[1] + n + 1);
  return cout << min(solve(0), solve(1)), 0;
}
