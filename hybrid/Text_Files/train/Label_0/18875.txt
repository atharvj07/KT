#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 5;
const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
long long a[N];
int F[N], Finv[N], inv[N];
void init() {
  inv[1] = 1;
  for (int i = 2; i < N; i++) {
    inv[i] = (MOD - MOD / i) * 1ll * inv[MOD % i] % MOD;
  }
  F[0] = Finv[0] = 1;
  for (int i = 1; i < N; i++) {
    F[i] = F[i - 1] * 1ll * i % MOD;
    Finv[i] = Finv[i - 1] * 1ll * inv[i] % MOD;
  }
}
int comb(int n, int m) {
  if (m < 0 || m > n) return 0;
  return F[n] * 1ll * Finv[n - m] % MOD * Finv[m] % MOD;
}
int main(void) {
  init();
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) scanf("%lld", &a[i]);
  if (n == 1) {
    cout << a[1] % MOD << endl;
    return 0;
  }
  if (n == 2) {
    cout << (a[1] + a[2]) % MOD << endl;
    return 0;
  }
  if (n & 1) {
    int flag = 1;
    for (int i = 1; i <= n - 1; i++) {
      a[i] = a[i] + flag * a[i + 1];
      flag = -flag;
    }
    --n;
  }
  int flag;
  if (n % 4 == 0)
    flag = -1;
  else
    flag = 1;
  long long sum = 0;
  for (int i = 1; i <= n; i += 2) {
    int coe = comb(n / 2 - 1, (i - 1) / 2);
    sum += (a[i] + flag * a[i + 1]) % MOD * coe % MOD;
    sum = ((sum % MOD) + MOD) % MOD;
  }
  cout << sum << endl;
  return 0;
}
