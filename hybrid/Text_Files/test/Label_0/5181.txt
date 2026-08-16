#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,abm,mmx,avx,avx2")
#pragma GCC optimize("unroll-loops")
using namespace std;
const unsigned _mod = 998244353;
const unsigned mod = 1e9 + 7;
const long long infi = 0x3f3f3f3f3f3f3f3fll;
const int inf = 0x3f3f3f3f;
char buf[1 << 24], *p1 = buf, *p2 = buf;
void rd(int &x) {
  x = 0;
  int f = 1;
  char ch =
      (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 21, stdin), p1 == p2)
           ? EOF
           : *p1++);
  while (ch < 48 || ch > 57) {
    if (ch == 45) f = -1;
    ch =
        (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 21, stdin), p1 == p2)
             ? EOF
             : *p1++);
  }
  while (ch >= 48 && ch <= 57)
    x = x * 10 + ch - 48,
    ch =
        (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 21, stdin), p1 == p2)
             ? EOF
             : *p1++);
  x *= f;
}
long long ksm(long long x, long long y) {
  long long ret = 1;
  x %= mod;
  while (y) {
    if (y & 1ll) ret = ret * x % mod;
    y >>= 1ll;
    x = x * x % mod;
  }
  return ret;
}
long long qpow(long long x, long long y) {
  long long ret = 1;
  while (y) {
    if (y & 1ll) ret = ret * x;
    y >>= 1ll;
    x = x * x;
  }
  return ret;
}
void wt(int x) {
  if (x > 9) wt(x / 10);
  putchar(x % 10 + 48);
}
int n, m, q, a[100010], f[100010], mx[100010], mn[100010], ans[100010], x;
int main() {
  rd(n), rd(m), rd(q);
  for (register int(i) = 1; (i) <= n; ++i) rd(a[i]);
  for (register int i = (1); i <= (q); ++i)
    rd(x), f[i] = m - x, mx[i] = mn[i] = a[1];
  for (register int i = (2); i <= (n); ++i)
    for (register int j = (1); j <= (q); ++j) {
      mx[j] = (mx[j] > a[i] ? mx[j] : a[i]),
      mn[j] = (mn[j] < a[i] ? mn[j] : a[i]);
      if (mx[j] - mn[j] > f[j]) mx[j] = mn[j] = a[i], ++ans[j];
    }
  for (register int i = (1); i <= (q); ++i) wt(ans[i]), putchar('\n');
  return 0;
}
