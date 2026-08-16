#include <bits/stdc++.h>
const int maxn = 100050, maxb = 20;
int n, m, d = 17, A[maxn];
long long ans = 0;
int main() {
  int d0, i, j, p, v;
  scanf("%d%d", &n, &m);
  for (i = 1; i <= n; i++) scanf("%d", &A[i]);
  for (d0 = 0; d0 < d; d0++)
    for (i = 1; i <= n; i++)
      if ((A[i] >> d0) & 1) {
        for (j = i + 1; j <= n && (A[j] >> d0) & 1; j++)
          ;
        ans += ((long long)(j - i) * (j - i + 1) / 2) << d0;
        i = j;
      }
  for (i = 0; i < m; i++) {
    scanf("%d%d", &p, &v);
    for (d0 = 0; d0 < d; d0++)
      if ((v >> d0 & 1) ^ (A[p] >> d0 & 1)) {
        int ls, rs;
        for (j = p + 1; j <= n && A[j] >> d0 & 1; j++)
          ;
        ls = j - p;
        for (j = p - 1; j && A[j] >> d0 & 1; j--)
          ;
        rs = p - j;
        if (A[p] >> d0 & 1)
          ans -= ((long long)ls * rs) << d0;
        else
          ans += ((long long)ls * rs) << d0;
      }
    A[p] = v;
    printf("%I64d\n", ans);
  }
  return 0;
}
