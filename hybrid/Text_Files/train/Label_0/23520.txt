#include <bits/stdc++.h>
int main() {
  int n, i, j, m, sum, len;
  char a[101];
  while (scanf("%s", a) != EOF) {
    len = strlen(a);
    for (i = 1; i < len; i++) {
      if (a[i] < 'a')
        ;
      else
        break;
    }
    if (i != len)
      printf("%s\n", a);
    else {
      for (i = 0; i < len; i++)
        printf("%c", a[i] >= 'a' ? a[i] - 32 : a[i] + 32);
      printf("\n");
    }
  }
}
