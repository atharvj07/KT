#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10, MOD = 998244353;
long long a, n, prev = 1, cur, ind = 0;
int k, temp;
long long binPow(long long b, long long p) {
  if (!p) return 1;
  long long v = binPow(b, p >> 1);
  if (p & 1) return ((((v * v) % MOD) * b) % MOD);
  return (v * v) % MOD;
}
int main() {
  scanf("%lld%d%lld", &n, &k, &a);
  cur = 1;
  for (int i = 0; i < k; i++) {
    scanf("%d", &temp);
    long long len = temp - ind;
    ind = temp;
    long long sides = binPow(a, len) * binPow(a, len);
    sides %= MOD;
    long long toRem = binPow(a, len) * (binPow(a, len) - 1);
    toRem %= MOD;
    toRem *= binPow(2, MOD - 2);
    toRem %= MOD;
    sides -= toRem;
    sides += MOD;
    sides %= MOD;
    cur *= sides;
    cur %= MOD;
  }
  long long left = n - (temp * 2);
  cur *= binPow(a, left);
  cur %= MOD;
  printf("%lld\n", cur);
  return 0;
}
