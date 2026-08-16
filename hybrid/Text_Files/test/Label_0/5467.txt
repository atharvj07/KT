#include <bits/stdc++.h>
using namespace std;
namespace chhokmah {
vector<int> g[2000005];
int n, m;
int vis[2000005], f[2000005], suc[2000005];
template <typename T>
T gcd(T a, T b) {
  return b == 0 ? a : gcd(b, a % b);
}
long long exgcd(long long a, long long b, long long &x, long long &y) {
  if (!b) {
    x = 1;
    y = 0;
    return a;
  }
  long long d = exgcd(b, a % b, x, y), z = x;
  x = y;
  y = z - (a / b) * y;
  return d;
}
void chhokmah() {
  scanf("%d%d", &n, &m);
  for (int i = 1, x; i <= n; i++) scanf("%d", &x), vis[x] = 1;
  for (int i = 1; i < m; i++) {
    if (!vis[i]) g[gcd(i, m)].push_back(i);
  }
  for (int i = m - 1; i; i--) {
    int k = m;
    for (int j = i + i; j < m; j += i)
      if (f[j] > f[k]) k = j;
    f[i] = f[k] + g[i].size();
    suc[i] = k;
  }
  printf("%d\n", f[1] + 1 - vis[0]);
  int pre = 1;
  for (int i = 1; i < m; i = suc[i]) {
    for (int j = 0; j < (int)g[i].size(); j++) {
      long long x, y, d = exgcd(m, pre, x, y);
      y = (y * g[i][j] / d % m + m) % m;
      pre = g[i][j];
      printf("%d ", (int)y);
    }
  }
  if (!vis[0]) printf("0\n");
}
}  // namespace chhokmah
int main() {
  chhokmah::chhokmah();
  return 0;
}
