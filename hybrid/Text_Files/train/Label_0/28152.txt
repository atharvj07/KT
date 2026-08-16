#include <bits/stdc++.h>
int main() {
  int n;
  char ar[200000];
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    long long int a;
    scanf("%I64d", &a);
    ar[i] = a > 0 ? 1 : -1;
  }
  long long pluses = 0;
  long long minuses = 0;
  long long prevP = -1;
  long long prevM = -1;
  for (int i = 0; i < n; i++) {
    if (prevP == -1) {
      prevP = ar[i] == -1 ? 0 : 1;
      prevM = 1 - prevP;
      minuses += prevM;
      pluses += prevP;
      continue;
    }
    if (ar[i] == -1) {
      minuses += prevP + 1;
      pluses += prevM;
      int temp = prevM;
      prevM = prevP + 1;
      prevP = temp;
    }
    if (ar[i] == 1) {
      minuses += prevM;
      pluses += prevP + 1;
      prevM = prevM;
      prevP = prevP + 1;
    }
  }
  printf("%I64d %I64d", minuses, pluses);
  return 0;
}
