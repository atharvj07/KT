#include <bits/stdc++.h>
using namespace std;
const int maxn = 110;
int n, m, k, a[maxn][maxn], b[maxn][maxn], ans = 110, flag[maxn];
int check1(int pos1, int pos2) {
  int res1 = 0, res2 = 0;
  for (int i = 1; i <= m; i++)
    if (a[pos1][i] != a[pos2][i]) res1++;
  for (int i = 1; i <= m; i++)
    if (a[pos1][i] == a[pos2][i]) res2++;
  return min(res1, res2);
}
void solve11() {
  int res = 0;
  for (int i = 1; i <= m; i++)
    if (flag[i]) {
      res++;
      a[1][i] ^= 1;
    }
  for (int i = 2; i <= n; i++) res += check1(1, i);
  ans = min(ans, res);
  for (int i = 1; i <= m; i++)
    if (flag[i]) a[1][i] ^= 1;
}
void dfs1(int dep) {
  if (dep == m + 1) {
    solve11();
    return;
  }
  flag[dep] = 1;
  dfs1(dep + 1);
  flag[dep] = 0;
  dfs1(dep + 1);
}
int check2(int pos1, int pos2) {
  int res1 = 0, res2 = 0;
  for (int i = 1; i <= m; i++)
    if (b[pos1][i] == b[pos2][i]) res1++;
  for (int i = 1; i <= m; i++)
    if (b[pos1][i] != b[pos2][i]) res2++;
  return min(res1, res2);
}
void solve22() {
  int res = 0;
  for (int i = 1; i <= m; i++)
    if (flag[i]) {
      res++;
      b[1][i] ^= 1;
    }
  for (int i = 2; i <= n; i++) res += check2(1, i);
  ans = min(ans, res);
  for (int i = 1; i <= m; i++)
    if (flag[i]) b[1][i] ^= 1;
}
void dfs2(int dep) {
  if (dep == m + 1) {
    solve22();
    return;
  }
  flag[dep] = 1;
  dfs2(dep + 1);
  flag[dep] = 0;
  dfs2(dep + 1);
}
void solve1() {
  if (k < n) {
    for (int i = 1; i <= n; i++) {
      int res = 0;
      for (int j = 1; j <= n; j++)
        if (i != j) res += check1(i, j);
      ans = min(ans, res);
    }
  } else {
    swap(n, m);
    dfs2(1);
    swap(n, m);
  }
}
void solve2() {
  swap(n, m);
  if (k < n) {
    for (int i = 1; i <= n; i++) {
      int res = 0;
      for (int j = 1; j <= n; j++)
        if (i != j) res += check2(i, j);
      ans = min(ans, res);
    }
  } else {
    swap(n, m);
    dfs1(1);
    swap(n, m);
  }
}
int main() {
  scanf("%d%d%d", &n, &m, &k);
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++) {
      scanf("%d", &a[i][j]);
      b[j][i] = a[i][j];
    }
  solve1();
  solve2();
  if (ans > k)
    puts("-1");
  else
    printf("%d\n", ans);
  return 0;
}
