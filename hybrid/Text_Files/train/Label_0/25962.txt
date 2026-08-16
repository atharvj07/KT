#include <bits/stdc++.h>
using namespace std;
template <typename T>
using min_queue = priority_queue<T, vector<T>, greater<T>>;
const long long MOD = 1e9 + 7;
int N, M;
int x[100100], y[100100];
int cnt[100100];
int res[9];
map<int, set<pair<int, int>>> mp[4];
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M;
  for (int i = 0; i < M; i++) cin >> x[i] >> y[i];
  for (int i = 0; i < M; i++) {
    int a = x[i], b = y[i];
    mp[0][a].insert({b, i});
    mp[1][b].insert({a, i});
    mp[2][a + b].insert({a, i});
    mp[3][a - b].insert({a, i});
  }
  for (int i = 0; i < 4; i++) {
    for (auto& [_, s] : mp[i]) {
      for (auto [_, j] : s) {
        cnt[j] += 2;
      }
      cnt[(*s.begin()).second]--;
      cnt[(*s.rbegin()).second]--;
    }
  }
  for (int i = 0; i < M; i++) res[cnt[i]]++;
  for (int i = 0; i <= 8; i++) cout << res[i] << ' ';
  cout << '\n';
  return 0;
}
