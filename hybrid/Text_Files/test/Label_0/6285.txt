#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 1000000007;
const int MX = 1000000 + 2;
ll h[MX];
int main() {
  ios_base::sync_with_stdio(false);
  int n;
  cin >> n;
  for (int i(1); i <= n; ++i) cin >> h[i];
  ll ans(0), was(0);
  for (int i(1); i <= n; ++i) {
    ans += h[i] - 1;
    ans %= MOD;
    ans += was * (min(h[i], h[i - 1]) - 1) % MOD;
    ans %= MOD;
    ll nxt(min(h[i + 1], h[i]) - 1);
    nxt += was * (min<ll>({h[i - 1], h[i + 1], h[i]}) - 1) % MOD;
    nxt %= MOD;
    was = nxt;
  }
  cout << ans << endl;
}
