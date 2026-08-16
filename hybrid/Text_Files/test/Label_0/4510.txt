#include <bits/stdc++.h>
int main() {
  int n;
  char st[10][9] = {"O-|-OOOO", "O-|O-OOO", "O-|OO-OO", "O-|OOO-O", "O-|OOOO-",
                    "-O|-OOOO", "-O|O-OOO", "-O|OO-OO", "-O|OOO-O", "-O|OOOO-"};
  scanf("%d", &n);
  if (n == 0) {
    printf("%s\n", st[n % 10]);
    return 0;
  }
  while (n) {
    printf("%s\n", st[n % 10]);
    n = n / 10;
  }
  return 0;
}
