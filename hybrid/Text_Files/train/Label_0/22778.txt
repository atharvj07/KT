#include <bits/stdc++.h>
using namespace std;
int a[510][510], b[510][510], x[510], d[510], n, m, r;
int ans[510][510], sum[510][510], as = 0;
long long sm = 0;
void init() {
  scanf("%d%d%d", &n, &m, &r);
  int dx = r;
  for (int i = (0); i <= (r); ++i) {
    while (((i) * (i)) + ((dx) * (dx)) > ((r) * (r))) dx--;
    x[i] = dx;
  }
  for (int i = (0); i <= (r + r); ++i) {
    int mm = 0;
    for (int j = (max(i - r, 0)); j <= (min(i, r)); ++j)
      mm = max(mm, x[j] + x[i - j] + 1);
    d[i] = mm;
  }
  for (int i = (1); i <= (n); ++i)
    for (int j = (1); j <= (m); ++j) {
      scanf("%d", &a[i][j]);
      a[i][j] += a[i][j - 1];
    }
  for (int i = (r + 1); i <= (n - r); ++i)
    for (int j = (r + 1); j <= (m - r); ++j) {
      int dx = n;
      for (int dy = (0); dy <= (r); ++dy) {
        dx = x[dy];
        b[i][j] += a[i - dy][dx + j] - a[i - dy][j - dx - 1];
        if (dy) b[i][j] += a[i + dy][dx + j] - a[i + dy][j - dx - 1];
      }
    }
  for (int i = (1); i <= (n); ++i)
    for (int j = (1); j <= (m); ++j) {
      ans[i][j] = ans[i][j - 1];
      sum[i][j] = sum[i][j - 1];
      if (b[i][j] == ans[i][j]) sum[i][j]++;
      if (b[i][j] > ans[i][j]) ans[i][j] = b[i][j], sum[i][j] = 1;
    }
}
void work() {
  for (int i = (r + 1); i <= (n - r); ++i)
    for (int j = (r + 1); j <= (m - r); ++j)
      for (int k = (r + 1); k <= (n - r); ++k)
        if (abs(i - k) > r + r) {
          if (ans[k][m] + b[i][j] >= as) {
            if (ans[k][m] + b[i][j] == as)
              sm += sum[k][m];
            else
              sm = sum[k][m];
            as = ans[k][m] + b[i][j];
          }
        } else {
          int q = j - d[abs(i - k)];
          if (q > r && ans[k][q] + b[i][j] >= as) {
            if (ans[k][q] + b[i][j] == as)
              sm += sum[k][q] * 2;
            else
              sm = sum[k][q] * 2;
            as = ans[k][q] + b[i][j];
          }
        }
  printf("%d %I64d", as, sm / 2);
}
int main() {
  init();
  work();
  return 0;
}
