#include <bits/stdc++.h>
using namespace std;
int n, ans;
int a[2510];
int p[20];
int dfs(int x) {
  if (x * 2 > p[n + 1] - 1) return 0;
  int res = 0;
  int c = dfs(2 * x) + a[2 * x];
  int b = dfs(2 * x + 1) + a[2 * x + 1];
  ans += max(c, b) - min(c, b);
  return max(c, b);
}
int main() {
  p[0] = 1;
  for (int i = 1; i < 15; i++) p[i] = p[i - 1] * 2;
  scanf("%d", &n);
  for (int i = 2; i <= p[n + 1] - 1; i++) scanf("%d", &a[i]);
  ans = 0;
  dfs(1);
  printf("%d\n", ans);
  return 0;
}
