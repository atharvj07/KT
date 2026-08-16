#include <bits/stdc++.h>
int main() {
  int n, k, i, j;
  int hols, arr[1000];
  int temp, loop, flag = 0;
  scanf("%d%d", &n, &k);
  scanf("%d", &hols);
  for (i = 0; i <= n; i++) {
    arr[i] = 0;
  }
  for (i = 0; i < hols; i++) {
    scanf("%d", &temp);
    arr[temp] = 2;
  }
  for (i = 0; i <= n;) {
    for (j = i; j < i + k; j++) {
      if (arr[j] == 2) {
        flag = 1;
        loop = j;
      }
    }
    if (flag == 1) {
      flag = 0;
      i = loop;
    } else {
      i = i + k;
    }
    arr[i] = 1;
  }
  int min = 0;
  for (i = 1; i <= n; i++) {
    if (arr[i] == 1 || arr[i] == 2) min++;
  }
  printf("%d", min);
  return 0;
}
