#include <bits/stdc++.h>
using namespace std;
template <class T>
inline void in(T &x) {
  x = 0;
  char c = getchar();
  bool f = 0;
  while (!isdigit(c)) f |= (c == '-'), c = getchar();
  while (isdigit(c)) x = x * 10 + (c ^ '0'), c = getchar();
  f ? x = -x : 0;
}
template <class T>
inline void out(T x, const char c = '\n') {
  static short st[30];
  short m = 0;
  if (x < 0) {
    if (x == -2147483648) {
      printf("-2147483648");
      return;
    }
    putchar('-'), x = -x;
  }
  do st[++m] = x % 10, x /= 10;
  while (x);
  while (m) putchar(st[m--] | '0');
  putchar(c);
}
template <class T, class... Args>
inline void in(T &x, Args &...args) {
  in(x);
  in(args...);
}
template <class T, class... Args>
inline void out(const T &x, const Args &...args) {
  out(x, ' ');
  out(args...);
}
template <class T>
inline void prt(T a[], int n) {
  for (register int i = 0; i < n; ++i) out(a[i], ' ');
  putchar('\n');
}
template <class T>
inline void clr(T a[], int n) {
  memset(a, 0, sizeof(T) * n);
}
template <class T>
inline void clr(T *a, T *b) {
  memset(a, 0, sizeof(T) * (b - a));
}
template <class T>
inline bool ckmax(T &a, const T &b) {
  return a < b ? a = b, 1 : 0;
}
template <class T>
inline bool ckmin(T &a, const T &b) {
  return a > b ? a = b, 1 : 0;
}
namespace MOD_CALC {
const int md = 1e9 + 7;
inline int add(const int a, const int b) {
  return a + b >= md ? a + b - md : a + b;
}
inline int sub(const int a, const int b) {
  return a - b < 0 ? a - b + md : a - b;
}
inline int mul(const int a, const int b) { return (long long)a * b % md; }
inline void inc(int &a, const int b) { (a += b) >= md ? a -= md : 0; }
inline void dec(int &a, const int b) { (a -= b) < 0 ? a += md : 0; }
inline int qpow(int a, int b) {
  int r = 1;
  for (; b; b >>= 1, a = mul(a, a))
    if (b & 1) r = mul(r, a);
  return r;
}
inline int qpow(int a, int b, const int p) {
  int r = 1;
  for (; b; b >>= 1, a = (long long)a * a % p)
    if (b & 1) r = (long long)r * a % p;
  return r;
}
inline int mdinv(const int a) { return qpow(a, md - 2); }
template <class... Args>
inline int add(const int a, const int b, const Args &...args) {
  return add(add(a, b), args...);
}
template <class... Args>
inline int mul(const int a, const int b, const Args &...args) {
  return mul(mul(a, b), args...);
}
}  // namespace MOD_CALC
using namespace MOD_CALC;
namespace i207M {
long long t, a, b;
signed main() {
  in(t, a, b);
  if (t == a) {
    if (a == b)
      puts(t == 1 ? "inf" : "2");
    else
      puts("0");
  } else if (a == b)
    puts("1");
  else if (a < t || b < a)
    puts("0");
  else {
    long long c = 0, p = 1;
    while (b) c += (b % a) * p, b /= a, p *= t;
    ;
    if (t == 1)
      puts((c == a || c == 1) ? "1" : "0");
    else
      puts((c == a) ? "1" : "0");
  }
  return 0;
}
}  // namespace i207M
signed main() {
  i207M::main();
  return 0;
}
