#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 5;
const double EPS = 1e-7;
const int INF = 1000000000 + 5;
const int MAXN2 = 5000 + 5;
int val[MAXN2][MAXN2];
int n, m;
int sz = 1;
int q[MAXN][3];
int res[MAXN];
int main() {
  cin >> n >> m;
  int t, l, r, d;
  for (int i = 0; i < n; i++) {
    res[i] = INF;
  }
  for (int i = 0; i < m; i++) {
    scanf("%d%d%d%d", &t, &l, &r, &d);
    if (t == 1) {
      l--;
      r--;
      for (int j = l; j <= r; j++) {
        val[sz][j] += d;
      }
    } else {
      l--;
      r--;
      q[sz][0] = l;
      q[sz][1] = r;
      q[sz][2] = d;
      sz++;
      for (int j = 0; j < n; j++) {
        val[sz][j] = val[sz - 1][j];
      }
    }
  }
  for (int i = 1; i < sz; i++) {
    for (int j = q[i][0]; j <= q[i][1]; j++) {
      res[j] = min(res[j], q[i][2] - val[i][j]);
    }
  }
  for (int i = 0; i < n; i++) {
    if (res[i] == INF) res[i] = 0;
  }
  int v;
  bool was, good;
  for (int i = 1; i < sz; i++) {
    was = false;
    good = true;
    for (int j = q[i][0]; j <= q[i][1]; j++) {
      v = res[j] + val[i][j];
      if (v == q[i][2]) was = true;
      if (v > q[i][2]) good = false;
    }
    if (!(was && good)) {
      printf("NO");
      return 0;
    }
  }
  printf("YES\n");
  for (int i = 0; i < n; i++) {
    printf("%d ", res[i]);
  }
  return 0;
}
