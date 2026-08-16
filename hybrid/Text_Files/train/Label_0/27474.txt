#include <bits/stdc++.h>
using namespace std;
long long read() {
  long long x;
  scanf("%lld", &x);
  return x;
}
unsigned m;
unsigned add(unsigned a, unsigned b) { return a + b < m ? a + b : a + b - m; }
void dadd(unsigned &a, unsigned b) { a = add(a, b); }
unsigned sub(unsigned a, unsigned b) { return a >= b ? a - b : a - b + m; }
void dsub(unsigned &a, unsigned b) { a = sub(a, b); }
unsigned mul(unsigned a, unsigned b) { return (long long)a * b % m; }
void dmul(unsigned &a, unsigned b) { a = mul(a, b); }
unsigned ksm(unsigned a, unsigned b) {
  unsigned ans = 1;
  while (b) {
    if (b & 1) dmul(ans, a);
    b >>= 1;
    dmul(a, a);
  }
  return ans;
}
const int N = 222;
unsigned c[N][N];
unsigned tr[N];
unsigned fo[N][N];
unsigned top[N];
int main() {
  int n = read(), d = read();
  m = read();
  if (m == 1) {
    puts("0");
    exit(0);
  }
  for (int i = (int)(0); i <= (int)(n); i++) {
    c[i][0] = 1;
    for (int j = (int)(1); j <= (int)(i); j++)
      c[i][j] = add(c[i - 1][j - 1], c[i - 1][j]);
  }
  fo[0][0] = 1;
  for (int cnt = (int)(1); cnt <= (int)(n); cnt++) {
    tr[cnt] = 0;
    for (int i = (int)(0); i <= (int)(d - 1); i++)
      dadd(tr[cnt], fo[i][cnt - 1]);
    for (int i = (int)(1); i <= (int)(n); i++) {
      for (int k = (int)(1); k <= (int)(cnt); k++)
        dadd(fo[i][cnt],
             mul(c[cnt - 1][k - 1], mul(fo[i - 1][cnt - k], tr[k])));
    }
    top[cnt] = 0;
    for (int i = (int)(2); i <= (int)(d - 1); i++)
      dadd(top[cnt], fo[i][cnt - 1]);
  }
  unsigned ans = n == 2 || d >= 2;
  for (int i = (int)(1); i <= (int)(n); i++)
    for (int j = (int)(1); j <= (int)(n); j++)
      if (i + j <= n) {
        dadd(ans, mul(top[i], top[j]));
      }
  for (int i = (int)(1); i <= (int)(n - 1); i++) dadd(ans, top[i]);
  for (int i = (int)(1); i <= (int)(n - 1); i++) dadd(ans, top[i]);
  for (int i = (int)(2); i <= (int)(d); i++) {
    dadd(ans, fo[i][n - 1]);
    dadd(ans, fo[i][n - 1]);
  }
  for (int i = (int)(1); i <= (int)(n - 1); i++) {
    for (int k1 = (int)(2); k1 <= (int)(d); k1++)
      for (int k2 = (int)(2); k2 <= (int)(d); k2++)
        if (k1 + k2 <= d) {
          dadd(ans, mul(fo[k1][i], fo[k2][n - 1 - i]));
        }
  }
  dmul(ans, mul(2 % m, mul(n % m, (n - 1) % m)));
  printf("%u\n", ans);
  return 0;
}
