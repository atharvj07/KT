#include <bits/stdc++.h>
using namespace std;
const int P = 1e9 + 7;
int m[3], sum, dp[26][26][26][2501];
int n, T, t[50], g[50], ted[26][26][26][3];
void update(int col, int &a, int &b, int &c, int k) {
  (col ? col & 1 ? b : c : a) += k;
}
int main() {
  cin >> n >> T;
  for (int i = 0; i < n; i++) cin >> t[i] >> g[i];
  dp[0][0][0][0] = 1;
  for (int i = 0; i < n; i++) {
    m[g[i]] = min(m[--g[i]] + 1, n + 1 >> 1);
    for (int a = m[0]; ~a; a--)
      for (int b = m[1]; ~b; b--)
        for (int c = m[2]; ~c; c--)
          for (int x = T; x >= t[i]; x--) {
            int &ans = dp[a][b][c][x];
            update(g[i], a, b, c, -1);
            if (~a && ~b && ~c) (ans += dp[a][b][c][x - t[i]]) %= P;
            update(g[i], a, b, c, 1);
          }
  }
  for (int a = 0; a <= m[0]; a++)
    for (int b = 0; b <= m[1]; b++)
      for (int c = 0; c <= m[2]; c++) {
        for (int d = 0; d < 3; d++) {
          int &ans = ted[a][b][c][d];
          update(d, a, b, c, -1);
          ans = !a && !b && !c;
          if (~a && ~b && ~c)
            for (int e = 0; e < 3; e++)
              (ans += e ^ d ? ted[a][b][c][e] : 0) %= P;
          update(d, a, b, c, 1);
          ans = 1LL * ans * (d ? d & 1 ? b : c : a) % P;
        }
        (sum += (1LL * ted[a][b][c][0] + ted[a][b][c][1] + ted[a][b][c][2]) *
                dp[a][b][c][T] % P) %= P;
      }
  cout << sum;
}
