#include <bits/stdc++.h>
using namespace std;
const int maxn = 3e5;
int n, m, a[maxn], l[maxn], r[maxn];
long long ans = 0;
int main() {
  scanf("%d%d", &n, &m);
  if (n == 1) {
    printf("0\n");
    return 0;
  }
  memset(l, 0, sizeof(l));
  memset(r, 0, sizeof(r));
  for (int i = 1; i <= m; i++) {
    scanf("%d", &a[i]);
  }
  for (int i = m; i >= 1; i--) {
    l[a[i] + i + m] = l[a[i] + i + m + 1] + 1;
    r[a[i] - i + m] = r[a[i] - i + m - 1] + 1;
  }
  for (int i = 1; i <= n; i++) {
    int ll = max(i - m - 1 + l[i + m], 1), rr = min(i + m + 1 - r[i + m], n);
    ans += (rr - ll + 1);
  }
  printf("%lld\n", ans);
  return 0;
}
