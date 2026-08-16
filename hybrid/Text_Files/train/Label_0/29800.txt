#include <bits/stdc++.h>
using namespace std;
template <typename _t>
inline void read(_t &x) {
  x = 0;
  _t fu = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') fu = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = (x << 3) + (x << 1) + (ch & 15);
    ch = getchar();
  }
  x *= fu;
}
long long gcd(long long x, long long y) { return !x ? y : gcd(y % x, x); }
void exgcd(long long a, long long b, long long &x, long long &y) {
  if (!b) {
    x = 1;
    y = 0;
    return;
  }
  exgcd(b, a % b, y, x);
  y -= a / b * x;
}
long long log(long long n, long long a, long long x = 0, long long res = 1) {
  while (res <= n / a) {
    x++;
    res *= a;
  }
  return x;
}
long long qp(long long a, long long p, long long M) {
  long long ans = 1;
  while (p) {
    if (p & 1) ans = ans * a % M;
    a = a * a % M;
    p >>= 1;
  }
  return ans;
}
struct Mart {
  int a, b, c, d;
  Mart operator*(Mart &m) {
    Mart temp;
    temp.a = a * m.a + b * m.c;
    temp.b = a * m.b + b * m.d;
    temp.c = c * m.a + d * m.c;
    temp.d = c * m.b + d * m.d;
    return temp;
  }
  Mart() { a = b = c = d = 0; }
  Mart(int x[4]) {
    a = x[0];
    b = x[1];
    c = x[2];
    d = x[3];
  }
  Mart(int u, int v, int w, int x) {
    a = u;
    b = v;
    c = w;
    d = x;
  }
  int det() { return a * d - b * c; }
};
const int maxn = 2e5 + 10;
const int M = 998244353;
int n, m;
int a[maxn], b[maxn];
;
int suf[maxn];
struct NODE {
  int x, y;
} seg[maxn];
int main() {
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= n; i++) scanf("%d", a + i);
  for (int i = 1; i <= m; i++) scanf("%d", b + i);
  suf[n] = a[n];
  for (int i = n - 1; i >= 1; i--) suf[i] = min(suf[i + 1], a[i]);
  int left = 1, right = 1, bp = 1;
  int fail = 0;
  while (bp <= m) {
    if (suf[left] == b[bp]) {
      right = left;
      while (right <= n && suf[right] == b[bp]) right++;
      seg[bp] = {left, right - 1};
      bp++;
      left = right;
    } else {
      while (left <= n && suf[left] != b[bp]) left++;
      if (left > n) {
        fail = 1;
        break;
      }
    }
  }
  if (fail || suf[1] != b[1]) {
    puts("0");
    return 0;
  }
  left = right = bp = 1;
  long long ans = 1;
  while (bp <= m) {
    left = seg[bp].y;
    if (bp + 1 <= m) {
      if (seg[bp].y + 1 != seg[bp + 1].x) left = seg[bp + 1].x - 1;
      right = seg[bp + 1].y - 1;
    } else
      right = left;
    ans *= right - left + 1;
    ans %= M;
    bp++;
  }
  printf("%lld\n", ans);
  return 0;
}
