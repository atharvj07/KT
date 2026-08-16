#include <bits/stdc++.h>
int ifa[4] = {0, 1, 1, 0};
int b[4] = {0, 0, 0, 0};
int main(void) {
  int n, flag = 1, spec = 3, lose = 2;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    int winner;
    scanf("%d", &winner);
    memset(b, 0, sizeof(b));
    b[winner] = 1;
    b[spec] = 1;
    for (int i = 1; i <= 3; i++)
      if (b[i] == 0) lose = i;
    if (ifa[winner]) {
      ifa[spec] = 1;
      ifa[lose] = 0;
      int tem = lose;
      lose = spec;
      spec = tem;
    } else {
      flag = 0;
      break;
    }
  }
  if (flag)
    printf("YES\n");
  else
    printf("NO\n");
  return 0;
}
