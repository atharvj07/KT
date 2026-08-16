#include <bits/stdc++.h>
using namespace std;
int n, m;
int a[100011 + 3], b[111000 + 3], w[111000 + 3], x[111000 + 3], y[111000 + 3];
int f[1001 + 3][1000 + 3];
double ans;
double work(int x, int y, int w) {
  double ans = x + y + w;
  if (abs(x - y) <= w) return double(ans / 2);
  if (x > y) return x;
  return y;
}
void qsort(int l, int r) {
  int i = l, j = r, k = x[(l + r) / 2];
  do {
    while (x[i] < k) i++;
    while (x[j] > k) j--;
    if (i <= j) {
      swap(x[i], x[j]);
      swap(y[i], y[j]);
      i++;
      j--;
    }
  } while (i <= j);
  if (l < j) qsort(l, j);
  if (i < r) qsort(i, r);
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      f[i][j] = 1000000000;
    }
  }
  for (int i = 1; i <= m; i++) {
    scanf("%d%d%d", &a[i], &b[i], &w[i]);
    f[a[i]][b[i]] = w[i];
    f[b[i]][a[i]] = w[i];
  }
  for (int i = 1; i <= n; i++) {
    m++;
    a[m] = i;
    b[m] = i;
    w[m] = 0;
  }
  for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if (i == j && j == k && i == k) continue;
        f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
      }
    }
  }
  for (int i = 1; i <= n; i++) {
    f[i][i] = 0;
  }
  ans = 1000000000;
  for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) x[j] = f[j][a[i]], y[j] = f[j][b[i]];
    qsort(1, n);
    for (int j = n - 1; j > 0; j--) y[j] = max(y[j], y[j + 1]);
    for (int j = 1; j <= n; j++) ans = min(ans, work(x[j], y[j + 1], w[i]));
  }
  printf("%.9lf\n", ans);
  return 0;
}
