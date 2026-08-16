#include <bits/stdc++.h>
using namespace std;
inline void read(long long &x, long long f = 1) {
  x = 0;
  char ch = getchar();
  while (!isdigit(ch)) f = ch == '-' ? -1 : 1, ch = getchar();
  while (isdigit(ch)) x = (x << 3) + (x << 1) + ch - '0', ch = getchar();
  x *= f;
}
long long n, m, k, ans;
long long s2[5050][5050];
long long quick_pow(long long x, long long limit, long long sum = 1) {
  for (; limit; limit >>= 1, x = (x * x) % 998244353)
    if (limit & 1) sum = (sum * x) % 998244353;
  return sum;
}
void preset() {
  s2[0][0] = s2[1][1] = 1;
  for (long long i = 1; i <= 5050 - 50; i++) {
    for (long long j = 1; j <= 5050 - 50; j++) {
      s2[i][j] = (s2[i - 1][j - 1] + j * s2[i - 1][j]) % 998244353;
    }
  }
}
void init() {
  read(n), read(m), read(k);
  m = quick_pow(m, 998244353 - 2);
  preset();
  for (long long i = 0, fac = 1, cob = 1, x = 1; i <= k;
       i++, fac = (fac * i) % 998244353,
                 cob = cob * (n - i + 1) % 998244353 *
                       quick_pow(i, 998244353 - 2) % 998244353,
                 x = x * m % 998244353) {
    ans = (ans + s2[k][i] * fac % 998244353 * cob % 998244353 * x % 998244353) %
          998244353;
  }
  printf("%lld\n", ans);
}
int main() { init(); }
