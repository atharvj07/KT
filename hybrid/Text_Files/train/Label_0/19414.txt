#include <bits/stdc++.h>
using namespace std;
struct NOOD {
  int a;
  int b;
} num[105];
int v[105], f[105][200005];
int n, k;
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; i++) scanf("%d", &num[i].a);
  for (int i = 1; i <= n; i++) scanf("%d", &num[i].b);
  for (int i = 1; i <= n; i++) v[i] = num[i].a - k * num[i].b;
  for (int i = 0; i <= 300000; i++) f[0][i] = -(1 << 30);
  f[0][100000] = 0;
  for (int i = 1; i <= n; i++)
    for (int j = 200000; j >= max(v[i], 0); j--)
      f[i][j] = max(f[i - 1][j], f[i - 1][j - v[i]] + num[i].a);
  if (f[n][100000] == 0)
    printf("-1\n");
  else
    printf("%d\n", f[n][100000]);
}
