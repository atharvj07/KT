#include <bits/stdc++.h>
using namespace std;
long long cc[400005], ans;
int u[400005], c, D[400005], n, i, j, cnt, x, y, d, is[400005], p[400005];
inline long long cal(int mx, int f1, int f2) {
  long long res = 0;
  for (int i = 2; i <= mx + mx; ++i)
    res += cc[max(f2, i * f1 - n)] * min(i - 1, mx + mx + 1 - i);
  return res % 1000000007;
}
long long ksm(long long x, long long y) {
  long long ret = 1;
  for (; y; y >>= 1, x = x * x % 1000000007)
    if (y & 1) ret = ret * x % 1000000007;
  return ret;
}
int main() {
  cin >> n >> c;
  for (i = cc[0] = 1; i <= n + n; ++i) cc[i] = cc[i - 1] * c % 1000000007;
  for (i = 2, u[1] = D[1] = 1; i <= n; ++i) {
    if (!is[i]) p[++cnt] = i, D[i] = 2, u[i] = -1;
    for (j = 1; j <= cnt && (d = i * p[j]) < 400005; ++j) {
      is[d] = 1;
      if (i % p[j] == 0) {
        x = i / p[j];
        y = 3;
        while (x % p[j] == 0) x /= p[j], ++y;
        D[d] = D[x] * y;
        break;
      }
      D[d] = D[i] << 1;
      u[d] = -u[i];
    }
  }
  int h = n - 1;
  for (i = 1; i <= h; ++i)
    for (x = h / i, j = 1; j <= x; ++j) ans += u[j] * cal(x / j, i * j, i);
  cout << (ans % 1000000007 + 1000000007) * ksm(cc[n], 1000000007 - 2) %
              1000000007;
}
