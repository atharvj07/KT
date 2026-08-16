#include <bits/stdc++.h>
long long gi() {
  long long x = 0, f = 1;
  char ch = getchar();
  while (!isdigit(ch)) f ^= ch == '-', ch = getchar();
  while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
  return f ? x : -x;
}
int in[310], out[310], que[310], hd = 1, tl = 1;
long long val[310];
int dp[100010];
int main() {
  int n = gi(), q = gi(), a, b;
  long long t = gi();
  for (int i = 1; i <= n; ++i) val[i] = gi();
  for (int i = 1; i <= q; ++i) a = gi(), b = gi(), out[b] = a, ++in[a];
  for (int i = 1; i <= n; ++i)
    if (!in[i]) que[tl++] = i;
  while (hd ^ tl) {
    int x = que[hd++];
    if (out[x]) que[tl++] = out[x];
  }
  if (tl != n + 1) return puts("0"), 0;
  for (int i = n, x; i; --i)
    if (out[x = que[i]]) t -= val[out[x]], val[x] += val[out[x]];
  if (t < 0) return puts("0"), 0;
  dp[0] = 1;
  for (int i = 1; i <= n; ++i)
    for (int j = val[i]; j <= t; ++j)
      dp[j] = (dp[j] + dp[j - val[i]]) % 1000000007;
  printf("%d\n", dp[t]);
  return 0;
}
