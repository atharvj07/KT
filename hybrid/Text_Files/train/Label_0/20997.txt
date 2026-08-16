#include <bits/stdc++.h>
using namespace std;
const string y = "YES", n = "NO";
int N, c[32], used[32], cnt[32];
string solve() {
  for (int i = (0); i < (N); i++) cnt[c[i]]++;
  if (!cnt[N] or cnt[2]) return n;
  sort(c, c + N);
  reverse(c, c + N);
  priority_queue<int> q;
  q.push(N);
  used[0] = 1;
  while (!q.empty()) {
    int w = q.top() - 1;
    q.pop();
    if (!w) continue;
    int dp[32] = {}, cnt = 0;
    vector<int> rest[32], cand;
    for (int i = (0); i < (N); i++)
      if (!used[i] and q.top() - 1 <= c[i]) {
        w -= c[i];
        used[i] = 1;
        q.push(c[i]);
        cnt++;
      }
    if (w < 0) return n;
    for (int i = (0); i < (N); i++)
      if (!used[i]) cand.push_back(i);
    for (int i = (0); i < (N); i++) dp[i] = N + 1;
    dp[0] = 0;
    for (int &i : cand) {
      int d = c[i];
      for (int j = w - d; j >= 0; j--)
        if (dp[j + d] > dp[j] + 1) {
          dp[j + d] = dp[j] + 1;
          rest[j + d] = rest[j];
          rest[j + d].push_back(i);
        }
    }
    if (dp[w] > N or rest[w].size() + cnt < 2) return n;
    for (int &i : rest[w]) {
      used[i] = 1;
      q.push(c[i]);
    }
  }
  return y;
}
void input() {
  cin >> N;
  for (int i = (0); i < (N); i++) cin >> c[i];
}
signed main() {
  input();
  cout << solve() << endl;
  return 0;
}
