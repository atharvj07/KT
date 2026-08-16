#include <bits/stdc++.h>
using namespace std;
const int maxn = 3e5 + 5;
int a[maxn], s[maxn];
int g[maxn], f[maxn];
int main() {
  int n, m, k;
  cin >> n >> m >> k;
  for (int i = 1; i <= n; ++i) cin >> a[i];
  for (int i = 1; i <= m; ++i) {
    int x, y;
    cin >> x >> y;
    if (x <= k) g[x] = max(g[x], y);
  }
  sort(a + 1, a + 1 + n);
  for (int i = 1; i <= k; ++i) s[i] = s[i - 1] + a[i];
  for (int i = 1; i <= k; ++i) {
    f[i] = 0;
    for (int j = 0; j < i; ++j) f[i] = max(f[i], f[j] + s[j + g[i - j]] - s[j]);
  }
  cout << s[k] - f[k] << endl;
  return 0;
}
