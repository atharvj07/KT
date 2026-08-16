#include <bits/stdc++.h>
using namespace std;
const int N = 5000 + 10, mod = 1e9 + 7;
int x[N], y[N], col[N], n, a[N * N];
int dist(int a, int b) { return abs(x[a] - x[b]) + abs(y[a] - y[b]); }
bool dfs(int root, int c, int len) {
  bool res = true;
  col[root] = c;
  for (int i = 0; i < n; i++) {
    if (i ^ root && dist(i, root) > len)
      if (col[i] == 0)
        res &= dfs(i, 3 - c, len);
      else if (col[i] == col[root])
        res = false;
  }
  return res;
}
int main() {
  ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
  cin >> n;
  for (int i = 0; i < n; i++) cin >> x[i] >> y[i];
  int m = 1;
  set<int> e;
  e.insert(0);
  for (int i = 0; i < n; i++)
    for (int j = i + 1; j < n; j++)
      if (e.find(dist(i, j)) == e.end()) {
        e.insert(dist(i, j));
        a[m] = dist(i, j);
        m++;
      }
  sort(a, a + m);
  int st = 0, en = m - 1, ans = a[m - 1], cnt = 1;
  while (st <= en) {
    int mid = (st + en) / 2, len = a[mid], tmp = 1;
    memset(col, 0, sizeof(col));
    bool flag = true;
    for (int i = 0; i < n; i++) {
      if (!col[i]) {
        flag &= dfs(i, 1, len);
        tmp = (tmp * 2) % mod;
      }
    }
    if (flag) {
      ans = len;
      cnt = tmp;
      en = mid - 1;
    } else
      st = mid + 1;
  }
  cout << ans << "\n" << cnt << "\n";
  return 0;
}
