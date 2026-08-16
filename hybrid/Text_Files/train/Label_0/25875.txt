#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;
template <class T>
typename T::value_type arr_sum(const T& v, int n) {
  typename T::value_type sum = 0;
  for (int i = (0); i < (n); ++i) sum += v[i];
  return sum;
}
struct Sync_stdio {
  Sync_stdio() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
  }
} _sync_stdio;
int main() {
  string s;
  cin >> s;
  int n = s.size();
  const int C = 53;
  vector<vector<long long>> dp(C, vector<long long>(2));
  dp[0][0] = 1;
  dp[0][1] = 0;
  for (int i = (1); i < (C); ++i) {
    dp[i][1] = dp[i - 1][0];
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
  }
  if (s.size() % 2 == 0) {
    string t;
    string t2;
    for (int i = (0); i < (n); ++i) {
      t += 'A' + i % 2;
      t2 += 'B' - i % 2;
    }
    if (s == t || s == t2) {
      cout << dp[n / 2][0] + dp[n / 2 - 1][1];
      return 0;
    }
  }
  while (s.back() != s.front()) {
    s.insert(s.begin(), s.back());
    s.pop_back();
  }
  long long res = 1;
  for (int i = (0); i < (n - 1); ++i) {
    if (s[i] == s[i + 1]) {
      continue;
    }
    int j = i;
    while (j < n - 1 && s[j] != s[j + 1]) {
      ++j;
    }
    int t = j - i + 1;
    if (s[j] == 'B') {
      --t;
    }
    if (s[i] == 'A') {
      --t;
    }
    t /= 2;
    if (t == 0 && s[i] == 'A' && s[j] == 'B') {
      cout << 0;
      return 0;
    }
    if (s[j] == 'B') {
      --t;
    }
    if (s[i] == 'A') {
      --t;
    }
    t = max(t, 0);
    res *= dp[t][0] + dp[t][1];
    i = j;
  }
  cout << res;
}
