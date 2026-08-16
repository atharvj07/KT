#include <bits/stdc++.h>
using namespace std;
const long long mod = 1000007;
const int inf = 0x3f3f3f3f;
const double tiaohe = 0.57721566490153286060651209;
long long oula(long long x) {
  long long res = x;
  for (register int i = 2; i <= x / i; ++i) {
    if (x % i == 0) {
      res = res / i * (i - 1);
      while (x % i == 0) x /= i;
    }
  }
  if (x > 1) res = res / x * (x - 1);
  return res;
}
long long quickmod(long long a, long long n, long long m) {
  long long s = 1;
  while (n) {
    if (n & 1) {
      s = s * a % m;
    }
    a = (a * a) % m;
    n = n / 2;
  }
  return s;
}
long long gcd(long long a, long long b) { return b ? gcd(b, a % b) : a; }
void ex_gcd(long long a, long long b, long long &x, long long &y,
            long long &d) {
  if (!b) {
    d = a, x = 1, y = 0;
  } else {
    ex_gcd(b, a % b, y, x, d);
    y -= x * (a / b);
  }
}
long long inv(long long t, long long p) {
  long long d, x, y;
  ex_gcd(t, p, x, y, d);
  return d == 1 ? (x % p + p) % p : -1;
}
bool isPrime(long long x) {
  if (x == 2) return true;
  if (x % 2 == 0) return false;
  for (long long i = 2; i * i <= x; i++)
    if (x % i == 0) return false;
  return true;
}
double eqa = (1 + sqrt(5.0)) / 2.0;
const int N = 2e3 + 5;
long long mo = 1ll << 30;
int p[N + 1], mob[N + 1], cnt, d[N][N];
bool vis[N + 1];
void x_x() {
  mob[1] = 1;
  for (register int i = 2; i <= N; ++i) {
    if (!vis[i]) {
      p[++cnt] = i;
      mob[i] = -1;
    }
    for (int j = 1; p[j] <= N / i; j++) {
      vis[p[j] * i] = true;
      if (i % p[j] == 0) {
        mob[p[j] * i] = 0;
        break;
      }
      mob[p[j] * i] = -mob[i];
    }
  }
}
int GCD(int a, int b) {
  if (d[a][b]) return d[a][b];
  return b ? d[a][b] = GCD(b, a % b) : a;
}
long long cal(int i, int top) {
  long long res = 0;
  for (register int j = 1; j <= top; ++j)
    if (GCD(i, j) == 1) res = (res + top / j) % mo;
  return res;
}
int main() {
  x_x();
  int a, b, c;
  while (cin >> a >> b >> c) {
    long long ans = 0;
    for (register int i = 1; i <= a; ++i)
      for (register int j = 1; j <= min(b, c); ++j)
        if (GCD(i, j) == 1) {
          long long tmp = (long long)(a / i) * mob[j] * cal(i, b / j) % mo *
                          cal(i, c / j) % mo;
          ans = (ans + tmp) % mo;
        }
    cout << ans << endl;
  }
  return 0;
}
