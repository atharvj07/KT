#include <bits/stdc++.h>
int main() {
  long long base = 1, suma = 0, num, res;
  int one = 0;
  scanf("%I64d", &num);
  do {
    res = num % 8;
    num = num / 8;
    suma = suma + res * base;
    base = base * 10;
  } while (num > 0);
  while (suma > 0) {
    if (suma % 10 == 1) {
      one++;
    }
    suma /= 10;
  }
  printf("%d", one);
  return 0;
}
