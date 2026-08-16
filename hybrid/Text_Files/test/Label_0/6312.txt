#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using P = pair<int, int>;
constexpr ld EPS = 1e-12;
constexpr int INF = numeric_limits<int>::max() / 2;
constexpr int MOD = 1e9 + 7;
template <typename T>
void printv(const vector<T> &v) {
  int sz = v.size();
  for (int i = 0; i < sz; i++) {
    cout << v[i] << " \n"[i == sz - 1];
  }
}
int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  int n;
  cin >> n;
  vector<ll> a(n + 1, 0), sum(n + 1, 0);
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    sum[i] = sum[i - 1] + a[i];
  }
  vector<ll> dp(n + 1, -1e15);
  dp[0] = 0;
  for (int i = 1; i <= n; i++) {
    ll r = sum[i - 1] - dp[i - 1] * 3;
    if (r * 2 > a[i]) {
      dp[i] = dp[i - 1] + a[i] / 2;
    } else {
      dp[i] = dp[i - 1] + r + (a[i] - 2 * r) / 3;
    }
  }
  cout << dp[n] << endl;
}
