#include <bits/stdc++.h>
using namespace std;
int ara[100003], tra[100003], val[15];
int dp[2][5003];
int main() {
  int n, k, sz = 0, a, b, c, d, lt, ans = 0, fr, sc, x, y, z, i, j;
  vector<int> v;
  scanf("%d %d", &n, &k);
  lt = n * k;
  for (i = 1; i <= lt; i++) {
    scanf("%d", &a);
    ara[a]++;
  }
  for (i = 1; i <= n; i++) {
    scanf("%d", &a);
    tra[a]++;
    if (tra[a] == 1) {
      v.push_back(a);
      sz++;
    }
  }
  for (i = 1; i <= k; i++) {
    scanf("%d", &a);
    val[i] = a;
  }
  int idx, cap;
  for (i = 0; i < sz; i++) {
    a = v[i];
    b = tra[a];
    c = min(b * k, ara[a]);
    if (c != 0) {
      for (idx = b; idx >= 1; idx--) {
        fr = idx % 2;
        sc = (idx + 1) % 2;
        for (cap = 0; cap <= c; cap++) {
          if (idx == b) {
            int p = 0;
            for (int lp = 0; lp <= k; lp++) {
              if (cap - lp < 0) break;
              p = max(p, val[lp]);
            }
            dp[fr][cap] = p;
          } else {
            int p = 0;
            for (int lp = 0; lp <= k; lp++) {
              if (cap - lp < 0)
                break;
              else {
                p = max(p, val[lp] + dp[sc][cap - lp]);
              }
            }
            dp[fr][cap] = p;
          }
        }
      }
      ans = ans + dp[1][c];
    }
  }
  printf("%d\n", ans);
  return 0;
}
