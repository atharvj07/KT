#include <bits/stdc++.h>
int max(int a, int b) { return a > b ? a : b; }
int min(int a, int b) { return a > b ? b : a; }
int main() {
  int i;
  int a4, a7, a47, a74;
  scanf("%d %d %d %d", &a4, &a7, &a47, &a74);
  if (fabs(a47 - a74) > 1) {
    printf("-1\n");
    return 0;
  }
  if (a47 != a74) {
    if (min(a4, a7) < max(a47, a74)) {
      printf("-1\n");
      return 0;
    }
  }
  if (a47 == a74) {
    if (!((a4 > a47 && a7 >= a47) || (a4 >= a47 && a7 > a47))) {
      printf("-1\n");
      return 0;
    }
  }
  if (a47 > a74) {
    for (i = 1; i <= a4 - a47; i++) printf("4");
    for (i = 1; i <= a47; i++) printf("47");
    for (i = 1; i <= a7 - a47; i++) printf("7");
    printf("\n");
  } else if (a47 < a74) {
    printf("74");
    for (i = 1; i <= a4 - a74; i++) printf("4");
    for (i = 1; i <= a74 - 2; i++) printf("74");
    for (i = 1; i <= a7 - a74 + 1; i++) printf("7");
    printf("4\n");
  } else if (a47 == a74) {
    if (a4 == a47) {
      for (i = 1; i <= a47; i++) printf("74");
      for (i = 1; i <= a7 - a47; i++) printf("7");
      printf("\n");
    } else {
      for (i = 1; i <= a4 - a47 - 1; i++) printf("4");
      for (i = 1; i <= a47; i++) printf("47");
      for (i = 1; i <= a7 - a47; i++) printf("7");
      printf("4\n");
    }
  }
}
