#include <bits/stdc++.h>
using namespace std;
const int N = 1e2 + 5, E = 5e3 + 5;
const double eps = 1e-9;
int link[N][N], X[E], Y[E], W[E];
int dad[N], n, m;
int M[N][N];
double S[N][N];
int find(int u) { return u == dad[u] ? u : dad[u] = find(dad[u]); }
void merge(int x, int y) {
  int fx = find(x), fy = find(y);
  if (fx != fy) dad[fx] = fy;
}
void Gauss() {
  int i, j, k, x, y, pos;
  double t, Sax;
  for (x = y = 1; x <= n; x++) {
    pos = x;
    for (Sax = 0, i = x; i <= n; i++)
      if ((t = fabs(S[i][x])) > Sax) pos = i, Sax = t;
    if (pos != x)
      for (i = x; i <= n + 1; i++) swap(S[pos][i], S[x][i]);
    if (fabs(S[x][x]) < eps) continue;
    for (i = 1; i <= n; i++) {
      if (i == x) continue;
      t = S[i][x] / S[x][x];
      for (j = x; j <= n + 1; j++) S[i][j] -= t * S[x][j];
    }
  }
  for (i = 1; i <= n; i++)
    if (fabs(S[i][i]) > eps)
      S[i][n + 1] /= S[i][i];
    else
      S[i][n + 1] = 0;
}
int main() {
  int i, j, k, x, y;
  scanf("%d%d", &n, &m);
  for (i = 1; i <= n; i++) dad[i] = i;
  for (i = 1; i <= m; i++) {
    scanf("%d%d%d", X + i, Y + i, W + i);
    merge(X[i], Y[i]);
    M[X[i]][Y[i]]--;
    M[Y[i]][X[i]]--;
    M[X[i]][X[i]]++;
    M[Y[i]][Y[i]]++;
  }
  if (find(1) != find(n)) {
    for (i = 0; i <= m; i++) printf("%.10lf\n", 0);
    return 0;
  }
  for (i = 1; i <= n; i++) M[1][i] = 0, M[n][i] = 0;
  M[1][1] = 1;
  M[n][n] = M[n][n + 1] = 1;
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= n + 1; j++) {
      S[i][j] = M[i][j];
    }
  }
  Gauss();
  double lim = 1e50, t, inf = 1e50, Ans = 0;
  for (i = 1; i <= m; i++)
    lim =
        min(lim,
            (t = fabs(S[Y[i]][n + 1] - S[X[i]][n + 1])) < eps ? inf : W[i] / t);
  for (i = 1; i <= n; i++) S[i][n + 1] *= lim;
  for (i = 1; i <= m; i++)
    if (X[i] == 1 || Y[i] == 1) Ans += fabs(S[X[i] ^ Y[i] ^ 1][n + 1]);
  printf("%.10lf\n", Ans);
  for (i = 1; i <= m; i++) {
    printf("%.10lf\n", S[Y[i]][n + 1] - S[X[i]][n + 1]);
  }
}
