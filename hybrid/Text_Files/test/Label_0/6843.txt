#include <bits/stdc++.h>
using namespace std;
long long l, r, _, ans, k, na, nb, cnt, a[50], b[50], f[333];
void pretype() {
  k = 1;
  while (k <= 2000000000ll) a[na++] = k, k *= 2;
  k = 1;
  while (k <= 2000000000ll) b[nb++] = k, k *= 3;
  for (long long i = 0; i < na; i++)
    for (long long j = 0; j < nb; j++)
      if (a[i] * b[j] > 2000000000ll)
        break;
      else
        f[++cnt] = a[i] * b[j];
  f[++cnt] = 2000000001ll;
}
int main() {
  pretype();
  sort(f + 1, f + cnt + 1);
  scanf("%I64d%I64d", &l, &r);
  while (f[_] < l) _++;
  ans = _;
  while (f[_] <= r) _++;
  ans = _ - ans;
  printf("%I64d\n", ans);
  return 0;
}
