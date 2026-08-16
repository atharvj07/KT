#include <bits/stdc++.h>
using namespace std;
int main() {
  int R, C;
  char str[501][501];
  scanf("%d%d", &R, &C);
  for (int i = 0; i < R; i++) {
    scanf("%s", str[i]);
  }
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (str[i][j] == 'S') {
        if (i != 0 && str[i - 1][j] == 'W') {
          printf("No\n");
          return 0;
        }
        if (j != C - 1 && str[i][j + 1] == 'W') {
          printf("No\n");
          return 0;
        }
        if (j != 0 && str[i][j - 1] == 'W') {
          printf("No\n");
          return 0;
        }
        if (i != R - 1 && str[i + 1][j] == 'W') {
          printf("No\n");
          return 0;
        }
      }
    }
  }
  printf("Yes\n");
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (str[i][j] == '.') {
        printf("D");
      } else {
        printf("%c", str[i][j]);
      }
    }
    printf("\n");
  }
}
