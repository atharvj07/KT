#include <bits/stdc++.h>
using namespace std;
typedef struct w_W {
  int a;
  int b;
  int sum;
} miao;
miao x[200100];
int main() {
  int m, n;
  while (~scanf("%d %d", &m, &n)) {
    int ge = 0;
    for (int i = 0; i < m + n; i++) {
      scanf("%d", &x[i].a);
      x[i].sum = 0;
    }
    for (int i = 0; i < m + n; i++) scanf("%d", &x[i].b);
    int start = -1;
    for (int i = 0; i < m + n; i++) {
      if (start == -1 && x[i].b == 1) {
        start = i;
        x[start].sum += i;
        continue;
      }
      if (start != -1 && x[i].b == 1) {
        int z = x[start].a + x[i].a;
        z = z / 2;
        for (int j = start + 1; j < i; j++) {
          if (x[j].a <= z)
            x[start].sum++;
          else
            x[i].sum++;
        }
        start = i;
      }
    }
    x[start].sum += m + n - start - 1;
    for (int i = 0; i < m + n; i++) {
      if (x[i].b == 1) printf("%d ", x[i].sum);
    }
    printf("\n");
  }
  return 0;
}
