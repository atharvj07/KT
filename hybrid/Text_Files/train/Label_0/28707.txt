#include <bits/stdc++.h>
using namespace std;
constexpr int R = 5e7 + 69, INF = 2e9 + 6969;
int qq, n, m, x, y;
int t[111][1001];
int main() {
  scanf("%d", &qq);
  while (qq--) {
    scanf("%d%d%d%d", &n, &m, &x, &y);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        char ch;
        cin >> ch;
        if (ch == '*')
          t[i][j] = 1;
        else
          t[i][j] = 0;
      }
    }
    y = min(y, 2 * x);
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m - 1; ++j) {
        if (t[i][j] == 0 && t[i][j + 1] == 0) {
          t[i][j] = 1;
          t[i][j + 1] = 1;
          ans += (long long)y;
        } else if (t[i][j] == 0) {
          t[i][j] = 1;
          ans += (long long)x;
        }
      }
      if (t[i][m - 1] == 0) ans += (long long)x;
    }
    printf("%lld\n", ans);
  }
  return 0;
}
