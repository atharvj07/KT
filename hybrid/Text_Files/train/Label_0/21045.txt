#include <bits/stdc++.h>
using namespace std;
long long n, m, k, i, j, lim[9][9], lim2[9][9], a[9][9], s, mod = 1e9 + 7;
vector<long long> v;
long long dfs(long long x, long long y, long long cnt) {
  if (x > n) return 1;
  if (y > m) return dfs(x + 1, 1, cnt);
  long long ans = 0, i;
  lim[x][y] = lim[x - 1][y] | lim[x][y - 1];
  for (i = 0; i < k; i++) {
    if (a[x][y] != -1 && a[x][y] != i) continue;
    if (lim[x][y] & (1 << i)) continue;
    if (lim2[x][y] & (1 << i)) continue;
    if (!((1 << i) & s)) {
      if (a[x][y] == -1 && v[cnt] < i) continue;
    }
    lim[x][y] ^= (1 << i);
    long long s =
        dfs(x, y + 1, min((long long)((int)v.size() - 1), cnt + (v[cnt] == i)));
    if (i == v[cnt] && a[x][y] == -1)
      (ans += s * (v.size() - cnt)) %= mod;
    else
      (ans += s) %= mod;
    lim[x][y] ^= (1 << i);
  }
  return ans;
}
int main() {
  scanf("%I64d%I64d%I64d", &n, &m, &k);
  if (n + m > 11 || n + m - 1 > k) {
    cout << 0;
    return 0;
  }
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= m; j++) {
      scanf("%I64d", &a[i][j]);
      a[i][j]--;
      if (a[i][j] >= 0) s |= (1 << a[i][j]);
      if (a[i][j] >= 0) lim2[i - 1][j] |= (1 << a[i][j]);
      if (a[i][j] >= 0) lim2[i][j - 1] |= (1 << a[i][j]);
    }
  }
  for (i = n; i >= 1; i--) {
    for (j = m; j >= 1; j--) {
      if (a[i][j] >= 0 && ((lim2[i][j] >> a[i][j]) & 1)) {
        cout << 0;
        return 0;
      }
      lim2[i][j] |= lim2[i + 1][j] | lim2[i][j + 1];
    }
  }
  for (i = 0; i < k; i++)
    if ((s >> i) % 2 == 0) v.push_back(i);
  if (v.size() == 0) {
    cout << 1;
    return 0;
  }
  cout << dfs(1, 1, 0);
  return 0;
}
