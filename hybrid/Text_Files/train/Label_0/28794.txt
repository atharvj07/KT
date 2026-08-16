#include <bits/stdc++.h>
using namespace std;
int a[15];
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  memset(a, 0, sizeof a);
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%d", &x);
    a[x]++;
  }
  int ans = 0;
  for (int i = 1; i <= m; i++) {
    for (int j = i + 1; j <= m; j++) {
      ans = ans + a[i] * a[j];
    }
  }
  printf("%d\n", ans);
  return 0;
}
