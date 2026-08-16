#include <bits/stdc++.h>
using namespace std;
long long t, n, m, u, v, q, k, l, r;
const int N = 2e5 + 500;
const int SN = 331;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 57;
long long arr[N], brr[N];
string str, ss;
long long dp[11][70][1100][2];
long long solve(int base, int pos, int mask, bool started) {
  if (pos == 70) {
    return (mask == 0);
  }
  long long &ret = dp[base][pos][mask][started];
  if (ret != -1) return ret;
  ret = 0;
  for (int i = 0; i < base; ++i) {
    int next_mask = mask ^ (1 << i);
    if (i == 0 && !started) next_mask = mask;
    ret += solve(base, pos + 1, next_mask, started |= (i > 0));
  }
  return ret;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> q;
  memset(dp, -1, sizeof(dp));
  for (int i = 0; i < 10; ++i) solve(i, 0, 0, 0);
  while (q--) {
    int b;
    cin >> b >> l >> r;
    long long sol = 0;
    vector<int> str = vector<int>();
    while (r) {
      str.push_back(r % b);
      r /= b;
    }
    while (str.size() < 70) str.push_back(0);
    reverse(str.begin(), str.end());
    int cur = 0;
    bool started = false;
    for (int i = 0; i < str.size(); ++i) {
      for (int j = 0; j < str[i]; ++j) {
        int ncur = cur ^ (1 << j);
        if (j == 0 && started == false) ncur = cur;
        sol += solve(b, i + 1, ncur, started | (j > 0));
      }
      if (started || str[i] > 0) cur ^= (1 << str[i]);
      started |= (str[i] > 0);
    }
    if (cur == 0) sol++;
    l--;
    str = vector<int>();
    while (l) {
      str.push_back(l % b);
      l /= b;
    }
    while (str.size() < 70) str.push_back(0);
    reverse(str.begin(), str.end());
    cur = 0;
    started = false;
    for (int i = 0; i < str.size(); ++i) {
      for (int j = 0; j < str[i]; ++j) {
        int ncur = cur ^ (1 << j);
        if (j == 0 && started == false) ncur = cur;
        sol -= solve(b, i + 1, ncur, started | (j > 0));
      }
      if (started || str[i] > 0) cur ^= (1 << str[i]);
      started |= (str[i] > 0);
    }
    if (cur == 0) sol--;
    cout << sol << '\n';
  }
}
