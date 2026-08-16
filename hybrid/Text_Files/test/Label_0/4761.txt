#include <bits/stdc++.h>
using namespace std;
long long n, k, l, m;
long long a[2][2] = {{1, 0}, {0, 1}}, b[2][2] = {{1, 1}, {1, 0}}, c[2][2];
long long f(long long p, long long q) {
  if (q == 0) return 1;
  if (q == 1) return p % m;
  long long cur = f(p, q >> 1);
  cur = cur * cur % m;
  return cur * f(p, q & 1) % m;
}
int main() {
  cin >> n >> k >> l >> m;
  if (l == 0) {
    if (k == 0)
      printf("%lld\n", 1 % m);
    else
      printf("0\n");
  } else if (l <= 62 && k >= (1LL << l))
    printf("0\n");
  else {
    long long po = f(2, n);
    n++;
    for (int i = 0; i < 61; i++) {
      if (n & (1LL << i)) {
        for (int x = 0; x < 2; x++)
          for (int y = 0; y < 2; y++) c[x][y] = 0;
        for (int x = 0; x < 2; x++)
          for (int y = 0; y < 2; y++)
            for (int z = 0; z < 2; z++) {
              c[x][y] += a[x][z] * b[z][y];
              c[x][y] %= m;
            }
        for (int x = 0; x < 2; x++)
          for (int y = 0; y < 2; y++) a[x][y] = c[x][y];
      }
      for (int x = 0; x < 2; x++)
        for (int y = 0; y < 2; y++) c[x][y] = 0;
      for (int x = 0; x < 2; x++)
        for (int y = 0; y < 2; y++)
          for (int z = 0; z < 2; z++) {
            c[x][y] += b[x][z] * b[z][y];
            c[x][y] %= m;
          }
      for (int x = 0; x < 2; x++)
        for (int y = 0; y < 2; y++) b[x][y] = c[x][y];
    }
    long long ans = 1;
    for (int i = 0; i < l; i++) {
      if (k & (1LL << i))
        ans = (ans * (po - a[0][0] + m)) % m;
      else
        ans = (ans * a[0][0]) % m;
    }
    printf("%lld\n", ans % m);
  }
  return 0;
}
