#include <bits/stdc++.h>
using namespace std;
template <class T>
inline void chmax(T &x, T &y) {
  if (x < y) swap(x, y);
}
template <class T>
inline void chmin(T &x, T &y) {
  if (x > y) swap(x, y);
}
const long long INF = 0x3f3f3f3f3f3f;
const long long MOD = 1e9 + 7;
const long double EPS = 10e-10;
void Solution() {
  string a, b;
  cin >> a >> b;
  unordered_map<char, long long> freq_a;
  unordered_map<char, long long> freq_b;
  for (long long i = 0; i < (long long)a.size(); i += 1) freq_a[a[i]]++;
  for (long long i = 0; i < (long long)b.size(); i += 1) freq_b[b[i]]++;
  long long ans = 0;
  for (auto x : freq_b) {
    if (freq_a.count(x.first) == 0) {
      cout << -1;
      return;
    }
    ans += min(x.second, freq_a[x.first]);
  }
  cout << ans << '\n';
}
int32_t main() {
  long long tc = 1;
  for (long long tn = 1; tn < tc + 1; tn += 1) {
    Solution();
  }
  return 0;
}
