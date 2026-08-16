#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 10;
const int mod = 1e9 + 9;
int n, m;
long long pot[maxn];
bool test() {
  long long p = 1;
  for (int i = 1; i <= m; ++i) {
    p *= 2LL;
    if (p > n) return true;
  }
  return false;
}
int main() {
  cin >> n >> m;
  if (!test()) {
    cout << 0 << '\n';
    return 0;
  }
  long long ans = 1LL;
  pot[0] = 1LL;
  for (int i = 1; i <= m; ++i) pot[i] = (pot[i - 1] * 2LL) % mod;
  for (int i = 1; i <= n; ++i) {
    long long add = (pot[m] - i + mod) % mod;
    ans = (ans * add) % mod;
  }
  cout << ans << '\n';
  return 0;
}
