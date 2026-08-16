#include <bits/stdc++.h>
using namespace std;
const int maxn = 105, maxm = 5006;
const double eps = 1e-10;
int n, m, i, j, k;
double a[maxn][maxn], b[maxn], flow, tp;
int U[maxm], V[maxm], W[maxm];
int main() {
  scanf("%d%d", &n, &m);
  for (i = 1; i <= m; i++) {
    scanf("%d%d%d", U + i, V + i, W + i);
    a[U[i]][U[i]]++;
    a[U[i]][V[i]]--;
    a[V[i]][V[i]]++;
    a[V[i]][U[i]]--;
  }
  for (i = 2; i <= n; i++) a[1][i] = 0.;
  a[1][1] = a[n][n + 1] = 1.;
  for (i = 1; i <= n; i++) {
    for (k = i, j = i + 1; j <= n; j++)
      if (fabs(a[j][i]) > fabs(a[k][i])) k = j;
    if (fabs(a[k][i]) < eps) continue;
    for (j = i; j <= n + 1; j++) swap(a[k][j], a[i][j]);
    for (j = i + 1; j <= n; j++)
      if (fabs(a[j][i]) > eps) {
        tp = a[j][i] / a[i][i];
        for (k = i; k <= n + 1; k++) a[j][k] -= tp * a[i][k];
      }
  }
  for (i = n; i; i--) {
    if (fabs(a[i][i]) > eps) {
      b[i] = a[i][n + 1] / a[i][i];
      for (j = i - 1; j; j--)
        if (fabs(a[j][i]) > eps) a[j][n + 1] -= a[j][i] * b[i];
    } else
      b[i] = 0.;
  }
  if (b[n] < eps)
    flow = 0.;
  else {
    flow = 1e30;
    for (i = 1; i <= m; i++) {
      tp = fabs(b[U[i]] - b[V[i]]);
      if (tp < eps) continue;
      flow = min(flow, W[i] / tp);
    }
  }
  printf("%.10f\n", flow);
  for (i = 1; i <= m; i++) printf("%.10f\n", flow * (b[V[i]] - b[U[i]]));
  return 0;
}
