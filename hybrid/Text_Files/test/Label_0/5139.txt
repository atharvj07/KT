#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1e9 + 7;
const int INF = 2e9;
const long long INF64 = 3e18;
const double EPS = 1e-9;
const double PI = acos(-1);
const long long MD = 1551513443;
const long long T = 25923;
const int N = 100001;
const int M = 16;
const bool DEBUG = 1;
int n, r[M], b[M], dp[1 << M][M * M + 1][2];
pair<int, int> z[1 << M];
char color[M];
int main() {
  cin >> n;
  int s0 = 0, s1 = 0;
  for (int i = 0; i < int(n); i++) {
    cin >> color[i] >> r[i] >> b[i];
    s0 += max(0, r[i] - n);
    r[i] = min(r[i], n);
    s1 += max(0, b[i] - n);
    b[i] = min(b[i], n);
  }
  for (int mask = 0; mask < int((1 << n)); mask++)
    for (int i = 0; i < int(n); i++)
      if (mask & (1 << i)) {
        if (color[i] == 'R')
          z[mask].first++;
        else
          z[mask].second++;
      }
  for (int i = 0; i < int((1 << n)); i++)
    for (int j = 0; j < int(n * n + 1); j++)
      for (int t = 0; t < int(2); t++) dp[i][j][t] = INF;
  dp[0][0][0] = dp[0][0][1] = 0;
  for (int mask = 0; mask < int((1 << n)); mask++)
    for (int u = 0; u < int(n * n + 1); u++)
      for (int t = 0; t < int(2); t++)
        if (dp[mask][u][t] != INF) {
          for (int i = 0; i < int(n); i++)
            if (!(mask & (1 << i))) {
              int new_mask = mask + (1 << i), xx = 0, yy = 0;
              if (t == 0)
                xx = u;
              else
                yy = u;
              int first = max(0, r[i] - z[mask].first),
                  second = max(0, b[i] - z[mask].second);
              xx -= first;
              yy -= second;
              int q = -min(xx, yy);
              xx += q;
              yy += q;
              if (yy == 0)
                dp[new_mask][xx][0] =
                    min(dp[new_mask][xx][0], dp[mask][u][t] + q);
              else
                dp[new_mask][yy][1] =
                    min(dp[new_mask][yy][1], dp[mask][u][t] + q);
            }
        }
  int ans = INF, mask = (1 << n) - 1;
  for (int u = 0; u < int(n * n + 1); u++)
    for (int t = 0; t < int(2); t++)
      if (dp[mask][u][t] != INF) {
        int xx = 0, yy = 0;
        if (t == 0)
          xx = u;
        else
          yy = u;
        ans = min(ans, max(max(0, s0 - xx), max(0, s1 - yy)) + dp[mask][u][t]);
      }
  cout << ans + n << endl;
  return 0;
}
