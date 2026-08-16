#include <bits/stdc++.h>
const int N = 1e5 + 5;
int n;
long long ans, dlt[N], s[N];
char t[N], p[N];
int main() {
  scanf("%d%s%s", &n, p + 1, t + 1);
  for (int i = 1; i <= n; ++i) s[i] = p[i];
  for (int i = 1; i < n; ++i)
    dlt[i] = t[i] - s[i], s[i + 1] += dlt[i], ans += abs(dlt[i]);
  if (s[n] != t[n]) return puts("-1"), 0;
  for (int i = 1; i <= n; ++i) s[i] = p[i];
  printf("%lld\n", ans);
  if (ans > 100000) ans = 100000;
  int now = 1;
  while (ans--) {
    while (!dlt[now]) ++now;
    while ((dlt[now] > 0 && s[now + 1] + 1 > '9') ||
           (dlt[now] < 0 && s[now + 1] - 1 < '0'))
      ++now;
    int x = dlt[now] > 0 ? 1 : -1;
    printf("%d %d\n", now, x), dlt[now] -= x;
    s[now] += x, s[now + 1] += x;
    --now;
  }
  return 0;
}
