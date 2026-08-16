#include <bits/stdc++.h>
long long m[200000], t[200000], ans, n;
int main() {
  scanf("%I64d", &n);
  for (int i = 1; i <= n; ++i) scanf("%I64d", &m[i]), t[i] = m[i] + 1;
  for (int i = 2; i <= n; ++i)
    if (t[i] < t[i - 1]) t[i] = t[i - 1];
  for (int i = n; i >= 2; --i)
    if (t[i - 1] < t[i] - 1) t[i - 1] = t[i] - 1;
  for (int i = 1; i <= n; ++i) ans += t[i] - 1 - m[i];
  printf("%I64d", ans);
  return 0;
}
