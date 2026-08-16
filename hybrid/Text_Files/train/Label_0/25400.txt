#include <bits/stdc++.h>
int main() {
  int i = 0, a[100], b[27], s = 0, l;
  char c;
  c = getchar();
  while (c != '\n') {
    a[i] = c;
    i++;
    c = getchar();
  }
  i--;
  for (l = 0; l < 27; l++) b[l] = 0;
  for (l = 0; l <= i; l++) b[a[l] - 'a']++;
  for (i = 0; i < 27; i++) {
    if (b[i] != 0) s++;
  }
  if (s % 2 == 0)
    printf("CHAT WITH HER!\n");
  else
    printf("IGNORE HIM!\n");
  return 0;
}
