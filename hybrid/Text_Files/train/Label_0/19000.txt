#include <bits/stdc++.h>
int a[100010];
int main() {
  int n;
  scanf("%d", &n);
  int f = 0;
  for (int i = 0; i <= n; i++) {
    scanf("%d", &a[i]);
  }
  for (int i = 1; i <= n; i++) {
    if (a[i] != 1 && a[i - 1] != 1) {
      f = i;
      break;
    }
  }
  if (f) {
    int sum = 0;
    printf("ambiguous\n");
    for (int i = 0; i <= n; i++) {
      for (int j = 1; j <= a[i]; j++) {
        printf("%d ", sum);
      }
      sum += a[i];
    }
    sum = 0;
    printf("\n");
    for (int i = 0; i <= n; i++) {
      int j = 1;
      if (i == f) {
        j = 2;
        printf("%d ", sum - 1);
      }
      for (; j <= a[i]; j++) {
        printf("%d ", sum);
      }
      sum += a[i];
    }
  } else
    printf("perfect");
}
