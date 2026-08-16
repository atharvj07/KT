#include <bits/stdc++.h>
using namespace std;
const int inf = 1e9, maxn = 2e5 + 5, mod = 1e9 + 7;
int n, a[maxn], dp[maxn];
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  dp[1] = 0;
  for (int i = 2; i <= n + 1; i++)
    dp[i] = (dp[i - 1] * 2ll % mod + mod - dp[a[i - 1]] + 2) % mod;
  printf("%d\n", dp[n + 1]);
  return 0;
}
