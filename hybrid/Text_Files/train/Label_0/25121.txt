#include <bits/stdc++.h>
int main() {
  char s[16] = {0};
  int n, m;
  while (scanf("%s", s) != EOF) {
    n = strlen(s);
    m = 0;
    for (int i = 0; i < n / 2; i++) {
      if (s[i] != s[n - i - 1]) {
        m += 1;
      }
    }
    if (m == 1)
      puts("YES");
    else {
      if (n % 2 == 1 && m == 0) {
        puts("YES");
      } else
        puts("NO");
    }
  }
  return 0;
}
