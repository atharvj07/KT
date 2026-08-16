#include <bits/stdc++.h>
using namespace std;
const int MAX = 5e4 + 1;
int t, n, p[MAX], dp[MAX];
int main(int argc, char *argv[]) {
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    for (int i = 1, a; i <= 2 * n; ++i) {
      scanf("%d", &a);
      p[a] = i;
      dp[i] = 0;
    }
    dp[0] = 1;
    int mn = 2 * n + 1, mx = 0;
    for (int i = 2 * n; i > 0; --i) {
      if (p[i] < mn) {
        int val = mn - p[i];
        mn = p[i];
        for (int j = mx; j >= 0; --j)
          if (dp[j]) {
            dp[j + val] = 1;
            mx = max(mx, j + val);
          }
      }
    }
    if (dp[n])
      puts("YES");
    else
      puts("NO");
  }
  return 0;
}
