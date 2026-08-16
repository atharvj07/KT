#include <bits/stdc++.h>
#pragma GCC optimize( \
    "Ofast,no-stack-protector,unroll-loops,no-stack-protector,fast-math")
using namespace std;
const int N = 2e5 + 5, M = 2e5 + 5;
int get(int x) {
  if (!x) return 0;
  for (int j = 1; x >= 0; ++j)
    if (!(x -= j)) return j + 1;
  return -1;
}
int main() {
  int a00, a01, a10, a11;
  scanf("%d %d %d %d", &a00, &a01, &a10, &a11);
  if (!(a00 + a11 + a01 + a10)) exit(puts("1"));
  int one = get(a11);
  int zero = get(a00);
  if (zero == -1 || one == -1) exit(puts("Impossible"));
  if (one * zero != a01 + a10) {
    one = max(one, 1);
    zero = max(zero, 1);
    if (one * zero != a01 + a10) exit(puts("Impossible"));
  }
  int len = one + zero;
  for (int i = 0; i < len; ++i) {
    if (a10 >= zero) {
      --one;
      printf("1");
      a10 -= zero;
    } else {
      --zero;
      printf("0");
      a01 -= one;
    }
  }
}
