#include <bits/stdc++.h>
int num[110];
int x[110];
int main() {
  int n;
  while (scanf("%d", &n) != EOF) {
    int sum = 0;
    int people = 0;
    memset(x, 0, sizeof(x));
    memset(num, 0, sizeof(num));
    for (int i = 1; i <= n; i++) {
      scanf("%d", &num[i]);
    }
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        x[i] += (abs(i - j) + (i - 1) + (j - 1)) * num[j] * 2;
      }
    }
    int ans = x[1];
    for (int i = 1; i <= n; i++) {
      if (x[i] < ans) {
        ans = x[i];
      }
    }
    printf("%d\n", ans);
  }
  return 0;
}
