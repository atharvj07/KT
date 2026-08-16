#include <bits/stdc++.h>
using namespace std;
const long long inf = 2e18;
const long long mod = 1e9 + 7;
const long long mod2 = 998244353;
const long long delta = 12473;
const long long maxn = 1e6 + 10;
long long p = 0, v = 0;
long long n;
long long nn;
long long power(long long a, long long b) {
  long long ans = 1;
  while (b > 0) {
    if ((long long)b % 2 == 1) ans = (a * ans);
    b /= 2;
    a = a * a;
  }
  return ans;
}
void dojob(long long k) {
  if (n <= k) {
    v += n;
    return;
  }
  v += k;
  n -= k;
  p += (long long)floor(n / 10);
  n -= (long long)floor(n / 10);
  ;
  dojob(k);
}
long long dojob2(long long l, long long r) {
  if (l == r) return l;
  long long pp = (long long)floor((l + r) / 2);
  p = 0;
  v = 0;
  n = nn;
  dojob(pp);
  if (v >= p)
    return dojob2(l, pp);
  else
    return dojob2(pp + 1, r);
}
int main() {
  cin >> nn;
  cout << dojob2(1, nn);
  return 0;
}
