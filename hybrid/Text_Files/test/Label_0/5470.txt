#include <bits/stdc++.h>
int n, a;
char s[3];
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%s", s);
    for (int j = 0; j < 3; j++) {
      if (s[j] == '+') {
        a++;
        break;
      } else if (s[j] == '-') {
        a--;
        break;
      }
    }
  }
  printf("%d", a);
  return 0;
}
