#include <bits/stdc++.h>
using namespace std;
const int N = 105;
int n, V, now;
int sl[N], sr[N], lens[N], h[N * 2];
double ans[N][N];
void add(int x, int l, int r, double y) {
  ans[x][l] += y;
  ans[x][r + 1] -= y;
}
void trans(int x, int c, double F[N][N]) {
  double g0 = sr[x] > now + 1
                  ? 1.0 * (h[sr[x]] - h[max(now + 1, sl[x])]) / lens[x]
                  : 0.0;
  double g1 =
      sl[x] < now ? 1.0 * (h[min(now, sr[x])] - h[sl[x]]) / lens[x] : 0.0;
  double g2 =
      sl[x] <= now && sr[x] > now ? 1.0 * (h[now + 1] - h[now]) / lens[x] : 0.0;
  for (int k = c + 1; k >= 1; k--) {
    for (int t = c + 1 - k; t >= 1; t--)
      F[k][t] = F[k][t] * g0 + F[k - 1][t] * g1 + F[k][t - 1] * g2;
    F[k][0] = F[k][0] * g0 + F[k - 1][0] * g1;
  }
  for (int t = c + 1; t >= 1; t--) F[0][t] = F[0][t] * g0 + F[0][t - 1] * g2;
  F[0][0] *= g0;
}
void solve(int l, int r, double F[N][N]) {
  if (l == r) {
    if (sl[l] > now || sr[l] <= now) return;
    double pn = 1.0 * (h[now + 1] - h[now]) / lens[l];
    for (int k = 0; k < n; k++)
      for (int t = 0; k + t < n; t++)
        add(l, k + 1, k + t + 1, F[k][t] * pn / (t + 1));
    return;
  }
  int mid = (l + r) >> 1;
  double FH[N][N];
  memcpy(FH, F, sizeof(FH));
  for (int i = r; i > mid; i--) trans(i, n - (i - l + 1), F);
  solve(l, mid, F);
  for (int i = l; i <= mid; i++) trans(i, n - (r - i + 1), FH);
  solve(mid + 1, r, FH);
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d%d", sl + i, sr + i);
  for (int i = 1; i <= n; i++)
    lens[i] = sr[i] - sl[i], h[++V] = sl[i], h[++V] = sr[i];
  sort(h + 1, h + V + 1);
  V = unique(h + 1, h + V + 1) - (h + 1);
  for (int i = 1; i <= n; i++)
    sl[i] = lower_bound(h + 1, h + V + 1, sl[i]) - h,
    sr[i] = lower_bound(h + 1, h + V + 1, sr[i]) - h;
  for (now = 1; now < V; now++) {
    double tmpf[N][N];
    memset(tmpf, 0, sizeof(tmpf));
    tmpf[0][0] = 1;
    solve(1, n, tmpf);
  }
  for (int i = 1; i <= n; i++, puts(""))
    for (int j = 1; j <= n; j++) printf("%.12lf ", ans[i][j] += ans[i][j - 1]);
  return 0;
}
