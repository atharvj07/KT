#include <bits/stdc++.h>
using namespace std;
int n, m;
string b[2048], s;
int idx[2048];
pair<int, int> dp[2048][2048];
vector<int> ps[2048][32];
int suf[2048][32];
int get_pos(int ix, int lo, char ch) {
  const int c = ch - 'a';
  return *lower_bound(ps[ix][c].begin(), ps[ix][c].end(), lo);
}
int get_ix(int lo, char ch) {
  const int c = ch - 'a';
  return suf[lo][c];
}
int main() {
  cin >> n;
  for (int i = 0; i < (int)(n); i++) cin >> b[i];
  cin >> m;
  for (int i = 0; i < (int)(m); i++) cin >> idx[i];
  for (int i = 0; i < (int)(m); i++) idx[i]--;
  cin >> s;
  for (int k = 0; k < (int)(n); k++) {
    for (int i = 0; i < (int)(b[k].size()); i++) {
      const int c = b[k][i] - 'a';
      ps[k][c].push_back(i);
    }
    for (int i = 0; i < (int)(32); i++) ps[k][i].push_back((1 << 28));
  }
  for (int i = 0; i < (int)(32); i++) suf[m][i] = (1 << 28);
  for (int k = m - 1; k >= 0; k--) {
    for (int i = 0; i < (int)(32); i++) suf[k][i] = suf[k + 1][i];
    for (int i = 0; i < (int)(32); i++)
      if (ps[idx[k]][i].size() > 1) suf[k][i] = k;
  }
  for (int i = 0; i < (int)(2048); i++)
    for (int j = 0; j < (int)(2048); j++) dp[i][j].first = (1 << 28);
  dp[0][0] = make_pair(0, -1);
  for (int i = 0; i < (int)(2048); i++) {
    for (int j = 0; j < (int)(s.size()); j++)
      if (dp[i][j].first < (1 << 28)) {
        const int cix = dp[i][j].first;
        const int cpos = dp[i][j].second;
        const int sp = get_pos(idx[cix], cpos + 1, s[j]);
        if (sp < (1 << 28)) {
          dp[i + 1][j + 1] = min(dp[i + 1][j + 1], make_pair(cix, sp));
        } else {
          const int nix = get_ix(cix + 1, s[j]);
          if (nix < (1 << 28)) {
            const int npos = get_pos(idx[nix], 0, s[j]);
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], make_pair(nix, npos));
          }
        }
        dp[i][j + 1] = min(dp[i][j + 1], dp[i][j]);
      }
  }
  int ans = 0;
  for (int i = 0; i < (int)(2048); i++)
    for (int j = 0; j < (int)(2048); j++)
      if (dp[i][j].first < (1 << 28)) ans = i;
  cout << ans << endl;
  return 0;
}
