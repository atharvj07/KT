#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> t;
int q(int v, int l, int r, int L, int R, int k) {
  if (l > R || r < L || L > R) return 0;
  if (l <= L && R <= r)
    return lower_bound(t[v].begin(), t[v].end(), k) - t[v].begin();
  return q(v * 2, l, r, L, (L + R) / 2, k) +
         q(v * 2 + 1, l, r, (L + R) / 2 + 1, R, k);
}
int32_t main() {
  int n, m, U = 1;
  cin.tie(0);
  ios::sync_with_stdio(false);
  cin >> n;
  vector<pair<int, int>> a(n);
  vector<int> u(n);
  for (int i = 0; i < n; i++)
    cin >> a[i].first, a[i].second = -i, u[i] = a[i].first;
  while (U < n) U <<= 1;
  n = U;
  while (a.size() < n) a.push_back({-1e9, -(int)a.size()}), u.push_back(1e9);
  t.resize(n * 2);
  vector<int> z(n + 1);
  sort(a.rbegin(), a.rend());
  for (int i = 0; i < n; i++) z[i] = -a[i].second, t[i + n].push_back(z[i]);
  for (int i = n - 1; i > 0; i--) {
    for (auto e : t[i * 2]) t[i].push_back(e);
    for (auto e : t[i * 2 + 1]) t[i].push_back(e);
    sort(t[i].begin(), t[i].end());
  }
  cin >> m;
  while (m--) {
    int a, b, l = 0, r = n + 1;
    cin >> a >> b;
    while (l < r - 1) {
      int m = (l + r) / 2;
      int ans = q(1, 0, a - 1, 0, n - 1, m);
      if (ans > b - 1)
        r = m;
      else
        l = m;
    }
    cout << u[l] << "\n";
  }
}
