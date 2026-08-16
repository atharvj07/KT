#include <bits/stdc++.h>
#pragma GCC optimize("Ofast,unroll-loops,fast-math")
using namespace std;
long long poww(long long a, long long b, long long md) {
  return (!b ? 1
             : (b & 1 ? a * poww(a * a % md, b / 2, md) % md
                      : poww(a * a % md, b / 2, md) % md));
}
const int maxn = 27;
const int mxa = 50000 + 5;
const long long inf = 9223372036854775807;
const long long mod = 1e9 + 7;
int n, a[maxn * 2], ans, s, cnt[mxa];
pair<int, int> dp[maxn][maxn * mxa];
vector<int> v;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  ;
  cin >> n;
  for (int i = 1; i <= 2 * n; i++) {
    cin >> a[i];
    s += a[i];
    cnt[a[i]]++;
  }
  sort(a + 1, a + 2 * n + 1);
  s -= (a[1] + a[2]);
  dp[0][0] = {1, 0};
  for (int i = 3; i <= 2 * n; i++) {
    for (int j = n - 1; j >= 1; j--) {
      for (int k = s; k >= a[i]; k--) {
        if (dp[j - 1][k - a[i]].first && !dp[j][k].first) {
          dp[j][k] = {1, a[i]};
        }
      }
    }
  }
  for (int i = 0; i < maxn * mxa; i++) {
    if (dp[n - 1][i].first != 0 && i >= s - i) {
      ans = i;
      break;
    }
  }
  v.push_back(a[1]);
  cnt[a[1]]--;
  int cur = n - 1;
  while (cur) {
    v.push_back(dp[cur][ans].second);
    cnt[dp[cur][ans].second]--;
    ans = ans - dp[cur][ans].second;
    cur--;
  }
  sort((v).begin(), (v).end());
  for (auto u : v) cout << u << " ";
  cout << endl;
  for (int i = mxa - 1; i >= 0; i--) {
    while (cnt[i]--) {
      cout << i << " ";
    }
  }
}
