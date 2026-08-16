#include <bits/stdc++.h>
using namespace std;
template <class T>
inline void read(T &x) {
  int f = 0;
  x = 0;
  char ch = getchar();
  for (; !isdigit(ch); ch = getchar()) f |= (ch == '-');
  for (; isdigit(ch); ch = getchar()) x = x * 10 + ch - '0';
  if (f) x = -x;
}
long long mul(long long a, long long b, long long mod) {
  return (a * b - (long long)((long double)a / mod * b) * mod + mod) % mod;
}
long long power(long long x, long long p, long long mod) {
  long long res = 1;
  for (; p; p >>= 1, x = mul(x, x, mod))
    if (p & 1) res = mul(res, x, mod);
  return res;
}
void rmain() {
  long long a;
  cin >> a;
  int n = to_string(a).size();
  for (int m = 0;; m++) {
    long long b = (-a) % (1ll << (n + m));
    if (b < 0) b += 1ll << (n + m);
    if ((a + b) % 5 == 0) b += 1ll << (n + m);
    if (b == 0 && m == 0 || to_string(b).size() <= m) {
      long long c = (a + b) >> (n + m), pw5 = 5;
      long long t = vector<int>{-1, 0, 1, 3, 2}[c % 5];
      for (int i = (1); i <= (n + m - 1); i++) {
        while (power(2, t, pw5 * 5) != c % (pw5 * 5)) t += pw5 / 5 * 4;
        pw5 *= 5;
      }
      cout << t + n + m << endl;
      return;
    }
    a *= 10;
  }
}
int main() {
  int T;
  read(T);
  while (T--) rmain();
  return 0;
}
