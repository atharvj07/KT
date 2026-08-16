#include <bits/stdc++.h>
using namespace std;
const int mo = 1000000007;
int n, ans, v[200005], X, Y, t, H[200005], fl, e[200005];
vector<int> d, b[100005];
struct O {
  int x, y, i;
} a[100005];
bool cmx(O a, O b) { return a.x < b.x; }
bool cmy(O a, O b) { return a.y < b.y; }
bool cmi(O a, O b) { return a.i < b.i; }
void add(int x, int y) {
  b[x].push_back(y);
  b[y].push_back(x);
}
void dfs(int x, int y) {
  e[x] = 1;
  if (!v[a[x].x]) d.push_back(a[x].x), v[a[x].x] = 1;
  if (!v[a[x].y + X]) d.push_back(a[x].y + X), v[a[x].y + X] = 1;
  for (int i = 0; i < b[x].size(); ++i)
    if (b[x][i] != y)
      if (e[b[x][i]])
        fl = 0;
      else
        dfs(b[x][i], x);
}
int main() {
  scanf("%d", &n);
  H[0] = 1;
  for (int i = 1; i <= n + n; ++i) H[i] = H[i - 1] * 2 % mo;
  for (int i = 1; i <= n; ++i) scanf("%d%d", &a[i].x, &a[i].y), a[i].i = i;
  sort(a + 1, a + n + 1, cmx);
  t = a[1].x - 1;
  for (int i = 1; i <= n; ++i)
    if (a[i].x != t)
      t = a[i].x, a[i].x = ++X;
    else
      a[i].x = X, add(a[i - 1].i, a[i].i);
  sort(a + 1, a + n + 1, cmy);
  t = a[1].y - 1;
  for (int i = 1; i <= n; ++i) {
    if (a[i].y != t)
      t = a[i].y, a[i].y = ++Y;
    else
      a[i].y = Y, add(a[i - 1].i, a[i].i);
  }
  ans = 1;
  sort(a + 1, a + n + 1, cmi);
  for (int i = 1; i <= n; ++i)
    if (!e[i]) {
      fl = 1;
      dfs(i, 0);
      ans = 1ll * ans * (H[d.size()] - fl) % mo;
      for (int j = 0; j < d.size(); ++j) v[d[j]] = 0;
      d.clear();
    }
  printf("%d\n", (ans % mo + mo) % mo);
  return 0;
}
