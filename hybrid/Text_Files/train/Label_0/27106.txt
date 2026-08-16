#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, x, i = 1, j = 2, k, sum = 0;
  scanf("%I64d", &n);
  if (n % 2 == 0)
    printf("%I64d", n / 2 - 1);
  else
    printf("%I64d", n / 2);
  return 0;
}
