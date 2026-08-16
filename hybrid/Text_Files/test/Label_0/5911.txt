#include <bits/stdc++.h>
using namespace std;
int main() {
  int t, i, tot = 0, ji;
  scanf("%d", &t);
  long long int a[t], sum = 0;
  for (i = 0; i < t; i++) {
    scanf("%I64d", &a[i]);
    sum += a[i];
    if (tot == 0 && a[i] % 2 == 1) {
      ji = a[i];
      tot = 1;
    } else if (tot == 1 && a[i] % 2 == 1 && a[i] < ji) {
      ji = a[i];
    }
  }
  printf("%lld\n", sum % 2 == 0 ? sum : (sum - ji));
}
