#include <bits/stdc++.h>
int main() {
  int i, j, l, m;
  int arr[5][5];
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
      scanf("%d", &arr[i][j]);
      if (arr[i][j] == 1) {
        l = i;
        m = j;
      }
    }
    printf("\n");
  }
  printf("%d", abs(l - 2) + abs(m - 2));
  return 0;
}
