#include <bits/stdc++.h>
int main() {
  int n, num[10], i, j;
  bool flag;
  char c;
  scanf("%d", &n);
  memset(num, 0, sizeof(num));
  for (i = 0; i < 4; i++) {
    getchar();
    for (j = 0; j < 4; j++) {
      scanf("%c", &c);
      if (isdigit(c)) num[c - 48]++;
    }
  }
  for (i = 1, flag = true; i < 10; i++) {
    if (n * 2 < num[i]) {
      printf("NO\n");
      flag = false;
      break;
    }
  }
  if (flag) printf("YES\n");
}
