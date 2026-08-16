#include <bits/stdc++.h>
using namespace std;
int N, K;
string S;
int vis[5050][5050];
vector<pair<int, int>> nex[26];
void dfs(int cur, int mask) {
  if (vis[cur][mask] || cur + 1 + mask > N) return;
  vis[cur][mask] = 1;
  int i;
  nex[S[cur] - 'a'].push_back({cur + 1, mask});
  for (i = 0; i < (K); i++)
    if (mask & (1 << i)) dfs(cur + (1 << i), mask ^ (1 << i));
}
void solve() {
  int i, j, k, l, r, x, y;
  string s;
  cin >> S;
  N = S.size();
  while (1 << (K + 1) <= N) K++;
  vector<pair<int, int>> now;
  now.push_back({0, (1 << K) - 1});
  while (now.size()) {
    for (i = 0; i < (26); i++) nex[i].clear();
    for (auto& n : now) dfs(n.first, n.second);
    char c = 'z' + 1;
    for (i = 25; i >= 0; i--)
      if (nex[i].size()) c = 'a' + i;
    if (c == 'z' + 1) break;
    cout << c;
    swap(now, nex[c - 'a']);
  }
  cout << endl;
}
int main(int argc, char** argv) {
  string s;
  int i;
  if (argc == 1) ios::sync_with_stdio(false), cin.tie(0);
  for (i = 0; i < (argc - 1); i++) s += argv[i + 1], s += '\n';
  for (i = 0; i < (s.size()); i++) ungetc(s[s.size() - 1 - i], stdin);
  cout.tie(0);
  solve();
  return 0;
}
