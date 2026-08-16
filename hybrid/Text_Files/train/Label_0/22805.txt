#include <bits/stdc++.h>
int unimodal(int d[], int k) {
  int j, c;
  c = 0;
  for (j = 0; j < k - 1; j++) {
    if (d[j] < 0) {
      if (d[j + 1] < 0 || d[j + 1] == 0 || d[j + 1] > 0) {
        c = c + 1;
      }
    } else {
      if (d[j] == 0) {
        if (d[j + 1] == 0 || d[j + 1] > 0) {
          c = c + 1;
        }
      } else {
        if (d[j + 1] > 0) {
          c = c + 1;
        }
      }
    }
  }
  if (c == k - 1) {
    return 1;
  } else {
    return 0;
  }
}
int main() {
  int n, i;
  scanf("%d", &n);
  int a[n];
  for (i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  if (n == 1) {
    printf("YES");
  } else {
    int d[n - 1];
    for (i = 0; i < n - 1; i++) {
      d[i] = a[i] - a[i + 1];
    }
    if (unimodal(d, n - 1)) {
      printf("YES");
    } else {
      printf("NO");
    }
  }
  return 0;
}
