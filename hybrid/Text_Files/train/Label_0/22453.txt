#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7, N = 1e6 + 7;
int b;
long long inf = 1e18;
long long get(int a, int cur) {
  if (a % cur == 0) {
    return 0;
  }
  if ((a + 1) % cur == 0 || (a - 1) % cur == 0) {
    return b;
  }
  return inf;
}
int n, arr[N], a;
long long dp[3][N];
long long tryit(int cur) {
  for (int i = 1; i <= n; i++) {
    dp[0][i] = min(inf, dp[0][i - 1] + get(arr[i], cur));
    dp[1][i] = min(inf, min(dp[0][i - 1], dp[1][i - 1]) + a);
    dp[2][i] = min(inf, min({dp[0][i - 1], dp[1][i - 1], dp[2][i - 1]}) +
                            get(arr[i], cur));
  }
  return min({dp[0][n], dp[1][n], dp[2][n]});
}
long long res;
long long divs(int cur) {
  res = inf;
  for (int i = 2; i * i <= cur; i++) {
    if (cur % i != 0) {
      continue;
    }
    res = min(res, tryit(i));
    while (cur % i == 0) {
      cur /= i;
    }
  }
  if (cur > 1) {
    res = min(res, tryit(cur));
  }
  return res;
}
vector<int> change;
long long ans;
int main() {
  cin >> n >> a >> b;
  for (int i = 1; i <= n; i++) {
    scanf("%d", &arr[i]);
    if (i == 1 || i == n) {
      change.push_back(arr[i]);
    }
  }
  ans = inf;
  for (int it : change) {
    for (int i = it - 1; i <= it + 1; i++) {
      ans = min(ans, divs(i));
    }
  }
  cout << ans;
  return 0;
}
