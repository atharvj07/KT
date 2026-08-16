#include <bits/stdc++.h>
char in[1000005];
int st[1000005];
int val[1000005];
int cst;
int maxx = 0;
int ct = 1;
int main() {
  int i;
  scanf("%s", in + 1);
  for (i = 1; in[i] != '\0'; i++) {
    if (in[i] == '(')
      st[cst++] = i;
    else if (cst > 0) {
      cst--;
      val[i] = i - st[cst] + 1 + val[st[cst] - 1];
      if (val[i] > maxx)
        maxx = val[i], ct = 1;
      else if (val[i] == maxx)
        ct++;
    }
  }
  printf("%d %d\n", maxx, ct);
}
