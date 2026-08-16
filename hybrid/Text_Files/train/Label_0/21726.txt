#include <bits/stdc++.h>
using namespace std;
const int N = 200 + 10;
const double eps = 1e-14;
struct node {
  int p, a;
};
double d[N][N][N], rd[N][N];
node in[N];
vector<node> ar;
vector<int> br;
int main() {
  memset(d, 0, sizeof d);
  memset(rd, 0, sizeof rd);
  int n, l, K, tok;
  scanf("%d%d%d", &n, &l, &K);
  if (K > n) K = n;
  for (int i = 1; i <= n; ++i) scanf("%d", &in[i].p);
  for (int i = 1; i <= n; ++i) scanf("%d", &in[i].a);
  for (int i = 1; i <= n; ++i) {
    if (in[i].a == -1)
      br.push_back(in[i].p);
    else
      ar.push_back(in[i]);
  }
  d[0][0][K] = 1;
  for (int i = 0; i < ar.size(); ++i)
    for (int j = 0; j <= i; ++j)
      for (int k = K; k <= n; ++k)
        if (d[i][j][k] > eps) {
          tok = k + ar[i].a;
          if (tok > n) tok = n;
          d[i + 1][j + 1][tok] += d[i][j][k] * (ar[i].p / 100.0);
          d[i + 1][j][k] += d[i][j][k] * (1 - ar[i].p / 100.0);
        }
  rd[0][0] = 1;
  for (int i = 0; i < br.size(); ++i)
    for (int j = 0; j <= i; ++j)
      if (rd[i][j] > eps) {
        rd[i + 1][j + 1] += rd[i][j] * (br[i] / 100.0);
        rd[i + 1][j] += rd[i][j] * (1.0 - br[i] / 100.0);
      }
  double ans = 0;
  for (int i = 0; i <= ar.size(); ++i)
    for (int j = K; j <= n; ++j)
      if (d[ar.size()][i][j] > eps)
        for (int k = 0; k <= br.size(); ++k)
          if (rd[br.size()][k] > eps && k <= j && i + k >= l) {
            ans += d[ar.size()][i][j] * rd[br.size()][k];
          }
  printf("%.10f\n", ans);
  return 0;
}
