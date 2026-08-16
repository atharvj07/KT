#include <bits/stdc++.h>
using namespace std;
const long long INF = 1e18;
long long b[105][105] = {0};
int main() {
  long long n, m, k, x, y, mx = 0, mn = INF, ans;
  scanf("%lld%lld%lld%lld%lld", &n, &m, &k, &x, &y);
  if (n == 1) {
    mx = k / m + (k % m != 0);
    mn = k / m;
    ans = mn + (k % m >= y);
    printf("%lld %lld %lld\n", mx, mn, ans);
    return 0;
  } else if (n == 2) {
    mx = k / (m * 2) + (k % m != 0 || k / m % 2 != 0);
    mn = k / (m * 2);
    if (x == 1) {
      ans = k / (m * 2) + (k % (n * m) >= y);
    } else
      ans = k / (n * m) + (k % (n * m) >= m + y);
    printf("%lld %lld %lld\n", mx, mn, ans);
    return 0;
  }
  long long T = (m * (n * 2 - 2));
  mx = k / T * 2;
  if (k % T / m >= 1) {
    if (k % T / m == 1 && k % m == 0) {
      ;
    } else {
      mx++;
      if (k % T / m >= n) {
        if (k % T / m == n && k % m == 0) {
          ;
        } else
          mx++;
      }
    }
  }
  mx = max(mx, k / T + (k % T != 0));
  mn = k / T + (k % T / (n * m) != 0);
  long long aa = k / T;
  for (long long i = 1; i <= n; i++) {
    for (long long j = 1; j <= m; j++) {
      if (i == 1 || i == n) {
        b[i][j] += aa;
      } else
        b[i][j] += aa * 2;
    }
  }
  aa = k % T;
  for (long long i = 1; i <= n; i++) {
    for (long long j = 1; j <= m; j++) {
      if (aa) {
        aa--;
        b[i][j]++;
      } else {
        printf("%lld %lld %lld\n", mx, mn, b[x][y]);
        return 0;
      }
    }
  }
  for (long long i = n - 1; i >= 1; i--) {
    for (long long j = 1; j <= m; j++) {
      if (aa) {
        aa--;
        b[i][j]++;
      } else {
        printf("%lld %lld %lld\n", mx, mn, b[x][y]);
        return 0;
      }
    }
  }
  printf("%lld %lld %lld\n", mx, mn, b[x][y]);
}
