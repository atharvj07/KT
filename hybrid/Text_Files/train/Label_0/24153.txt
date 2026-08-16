#include <bits/stdc++.h>
using namespace std;
int n, a[30][30];
const int f[] = {288, 434, 152, 375, 304, 82,  439, 195, 103, 156,
                 109, 458, 115, 118, 194, 447, 344, 318, 493, 256};
int main() {
  scanf("%d", &n);
  for (int i = 0; i < (int)(n); i++)
    for (int j = 0; j < (int)(n); j++) {
      a[i][j] += f[i];
      a[j][i] += f[i];
    }
  for (int i = 0; i < (int)(n); i++) a[i][i] = 0;
  for (int i = 0; i < (int)(n); i++) {
    for (int j = 0; j < (int)(n); j++) {
      if (j) printf(" ");
      printf("%d", a[i][j]);
    }
    printf("\n");
  }
}
