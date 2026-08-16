#include <bits/stdc++.h>
using namespace std;
int n, m;
int dp[45][64][64];
int ans;
bool get_bit(int a, int n) { return (a >> n) & 1; }
int set_bit(int a, int n) { return a | (1 << n); }
int reset_bit(int a, int n) { return a & ~(1 << n); }
int main() {
  cin >> n >> m;
  if (m > n) swap(n, m);
  for (int i = 0; i <= n; i++) {
    for (int j = 0; j < (1 << m); j++) {
      for (int k = 0; k < (1 << m); k++) {
        dp[i][j][k] = -1000;
      }
    }
  }
  dp[0][0][(1 << m) - 1] = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < (1 << m); j++) {
      for (int k = 0; k < (1 << m); k++) {
        for (int l = 0; l < (1 << m); l++) {
          int s = j | l;
          int cnt = 0;
          int ns = (1 << m) - 1;
          int nr = (1 << m) - 1 - s;
          for (int i = 0; i < m; i++) {
            if (!get_bit(s, i)) {
              cnt++;
            }
          }
          if (m == 1) {
            if (get_bit(s, 0)) {
              ns = reset_bit(ns, 0);
            }
          } else {
            if (get_bit(s, 0)) {
              ns = reset_bit(ns, 0);
              ns = reset_bit(ns, 1);
            }
            if (get_bit(s, m - 1)) {
              ns = reset_bit(ns, m - 1);
              ns = reset_bit(ns, m - 2);
            }
            for (int i = 1; i < m - 1; i++) {
              if (get_bit(s, i)) {
                ns = reset_bit(ns, i - 1);
                ns = reset_bit(ns, i);
                ns = reset_bit(ns, i + 1);
              }
            }
          }
          dp[i][ns & k][nr] = max(dp[i][ns & k][nr], dp[i - 1][j][k] + cnt);
        }
      }
    }
  }
  for (int i = 0; i < (1 << m); i++) ans = max(ans, dp[n][0][i]);
  cout << ans;
  return 0;
}
