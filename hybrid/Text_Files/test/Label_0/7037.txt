#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const long long LINF = 0x3f3f3f3f3f3f3f3f;
const int MOD = (int)1e9 + 7;
const int N = (int)1e6 + 7;
const double eps = 1e-6;
bool eq(const double &a, const double &b) { return fabs(a - b) < eps; }
bool ls(const double &a, const double &b) { return a + eps < b; }
bool le(const double &a, const double &b) { return eq(a, b) || ls(a, b); }
char read_char() {
  char c;
  for (;;) {
    c = getchar();
    if (c >= 'A' && c <= 'Z') return c;
  }
}
long long powmod(long long a, long long b) {
  long long res = 1;
  a %= MOD;
  for (; b; b >>= 1) {
    if (b & 1) res = res * a % MOD;
    a = a * a % MOD;
  }
  return res;
}
long long gcd(long long a, long long b) { return b ? gcd(b, a % b) : a; }
int add(int a, int b) {
  if ((a += b) >= MOD) a -= MOD;
  return a;
}
int mul(int a, int b) { return 1ll * a * b % MOD; }
long long n, f[N];
void Init() {}
long long change(int x) {
  if (x == 1)
    return f[1] = 2;
  else
    return f[x] = f[x - 1] + 2 + (x - 1) * 3;
}
int Solve() {
  long long ans = 0;
  for (long long i = 1; n >= change(i); ++i)
    if (n % 3 == (((3 - i) % 3 + 3) % 3)) ++ans;
  return !printf("%lld\n", ans);
}
int main() {
  while (~scanf("%lld", &n)) {
    Init();
    Solve();
  }
  return 0;
}
