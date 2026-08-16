#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9 + 7;
const long long mod = 998244353;
const int maxn = 3005;
int dp[maxn][maxn];
int dp2[maxn][maxn];
long long add(long long a, long long b) { return (a + b) % mod; }
long long mul(long long a, long long b) { return (a * b) % mod; }
long long bin_pow(long long a, long long b) {
  long long res = 1;
  long long tmp = a;
  while (b) {
    if (b & 1) {
      res = mul(res, tmp);
    }
    tmp = mul(tmp, tmp);
    b >>= 1;
  }
  return res;
}
long long inv(long long a) { return bin_pow(a, mod - 2); }
long long min(long long a, long long b) {
  if (a > b)
    return b;
  else
    return a;
}
void solve() {
  int n, m;
  cin >> n >> m;
  long long n_good = 0, n_bad = 0;
  vector<bool> flags(n);
  for (int i = 0; i < n; i++) {
    int ai;
    cin >> ai;
    flags[i] = ai == 1;
  }
  vector<long long> weights(n);
  for (int i = 0; i < n; i++) {
    int w;
    cin >> w;
    weights[i] = w;
    if (flags[i]) {
      n_good += w;
    } else {
      n_bad += w;
    }
  }
  for (int i = m; i >= 0; i--) {
    dp[i][m - i] = dp2[i][m - i] = 1;
    for (int j = min(m - i - 1, (long long)n_bad); j >= 0; j--) {
      long long total = inv(n_good + n_bad + i - j);
      long long tmp = mul(dp[i + 1][j], n_good + i + 1);
      long long tmp2 = mul(dp[i][j + 1], n_bad - j);
      long long tmp3 = add(tmp, tmp2);
      dp[i][j] = mul(tmp3, total);
      tmp = mul(dp2[i + 1][j], n_good + i);
      tmp2 = mul(dp2[i][j + 1], n_bad - j - 1);
      tmp3 = add(tmp, tmp2);
      dp2[i][j] = mul(tmp3, total);
    }
  }
  for (int i = 0; i < n; i++) {
    if (flags[i]) {
      cout << mul(weights[i], dp[0][0]);
    } else {
      cout << mul(weights[i], dp2[0][0]);
    }
    cout << endl;
  }
}
int main() {
  cin.tie(0);
  cout.tie(0);
  ios_base::sync_with_stdio(false);
  solve();
  return 0;
}
