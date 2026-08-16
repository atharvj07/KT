#include <bits/stdc++.h>
using namespace std;
int a[210000], len, b[410000], p[410000];
int as[210000], aslen;
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  len = 0, b[++len] = -2;
  for (int i = 1; i < n; i++) b[++len] = a[i + 1] - a[i], b[++len] = -1;
  b[len] = -3;
  int k = 0;
  p[k] = 0;
  for (int i = 1; i <= len; i++) {
    int Lk = k - p[k] + 1, Rk = k + p[k] - 1;
    int j = k - (i - k);
    if (Lk <= j)
      p[i] = min(p[j], j - Lk + 1);
    else
      p[i] = 0;
    while (b[i + p[i]] == b[i - p[i]] && i - p[i] > 0 && i + p[i] <= len)
      p[i]++;
    if (i + p[i] - 1 > Rk) k = i;
  }
  for (int i = 1; i < n; i++) {
    if ((i == 1 || p[i] >= i - 1) && (i == n - 1 || p[i + n] >= n - i - 1)) {
      int d1 = a[1] + a[i], d2 = a[i + 1] + a[n] - m;
      if (d1 == d2) as[++aslen] = d1;
    }
  }
  if (p[n] >= n - 1) as[++aslen] = (a[1] + a[n]) % m;
  sort(as + 1, as + aslen + 1);
  printf("%d\n", aslen);
  for (int i = 1; i < aslen; i++) printf("%d ", as[i]);
  if (aslen != 0) printf("%d\n", as[aslen]);
  return 0;
}
