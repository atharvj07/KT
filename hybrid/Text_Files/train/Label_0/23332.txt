#include <bits/stdc++.h>
using namespace std;
int t, n, a[100010], b[100010];
int f[1000010], exist[1000010];
int main() {
  for (int i = 0; i < 100010; ++i) {
    b[i] = -1;
  }
  scanf("%d ", &n);
  for (int j = 1; j <= n; ++j) {
    scanf("%d", &a[j]);
    exist[a[j]] = j;
    if (a[j] > j) {
      puts("-1");
      return 0;
    }
    if (j >= 2 && a[j - 1] < a[j]) {
      b[j] = a[j - 1];
      f[b[j]] = 1;
    }
  }
  int num = 0;
  for (int i = 1; i <= n; ++i) {
    if (b[i] != -1) continue;
    while (f[num] != 0) {
      num++;
    }
    if (i <= exist[num]) {
      b[i] = num + 1;
    } else {
      b[i] = num;
    }
    f[num] = 1;
  }
  for (int i = 1; i <= n; ++i) {
    printf("%d ", b[i]);
  }
  return 0;
}
