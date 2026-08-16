#include <bits/stdc++.h>
using namespace std;
long int fib(long int n) {
  long int first = 0, second = 1, temp;
  temp = first + second;
  if (n == 1) return 0;
  if (n == 2) return 1;
  for (int i = 3; i <= n; i++) {
    temp = first + second;
    first = second;
    second = temp;
  }
  return temp;
}
int main() {
  long int n, index = 0;
  scanf("%ld", &n);
  printf("0 0 %d", n);
}
