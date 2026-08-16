#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:10240000,10240000")
using namespace std;
const double R = 0.5772156649015328606065120900;
const int N = 50 + 5;
const int mod = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const double pi = acos(-1.0);
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
long long ex_gcd(long long a, long long b, long long &x, long long &y) {
  if (b == 0) {
    x = 1, y = 0;
    return a;
  }
  long long d = ex_gcd(b, a % b, y, x);
  y -= a / b * x;
  return d;
}
long long inverse(long long a, long long mod) {
  long long x, y;
  if (ex_gcd(a, mod, x, y) != 1) return -1;
  return (x % mod + mod) % mod;
}
bool Merge(long long a1, long long m1, long long a2, long long m2,
           long long &ansa, long long &ansm) {
  long long c = a2 - a1, d = gcd(m1, m2);
  if (c % d) return false;
  c = (c % m2 + m2) % m2;
  long long A = c / d * inverse(m1 / d, m2 / d);
  A %= m2 / d;
  long long tmp_a = m1 * A + a1;
  ansm = m1 / d * m2;
  ansa = (tmp_a % ansm + ansm) % ansm;
  return true;
}
int main() {
  long long a1, b1, a2, b2, le, ri;
  scanf("%I64d%I64d%I64d%I64d%I64d%I64d", &a1, &b1, &a2, &b2, &le, &ri);
  long long a, m;
  if (!Merge(b1, a1, b2, a2, a, m)) {
    puts("0");
    return 0;
  }
  le = max(le, max(b1, b2));
  if (le > ri)
    puts("0");
  else {
    long long c1 = double(le - a) / m;
    bool tag = false;
    for (long long i = c1 - 4; i <= c1 + 4; i++) {
      long long tm = i * m + a;
      if (tm >= le && tm <= ri) {
        c1 = i;
        tag = true;
        break;
      }
    }
    if (!tag) {
      puts("0");
      return 0;
    }
    long long c2 = double(ri - a) / m;
    tag = false;
    for (long long i = c2 + 4; i >= c2 - 4; i--) {
      long long tm = i * m + a;
      if (tm <= ri && tm >= le) {
        c2 = i;
        tag = true;
        break;
      }
    }
    if (!tag) {
      puts("0");
      return 0;
    }
    long long ans = c2 - c1 + 1;
    if (ans < 0)
      puts("0");
    else
      printf("%I64d\n", ans);
  }
  return 0;
}
