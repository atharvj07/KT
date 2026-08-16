#include <bits/stdc++.h>
using namespace std;
int a[100005];
int main() {
  int i, n;
  int paid, e;
  while (scanf("%d", &n) == 1) {
    e = 0;
    paid = 0;
    a[0] = 0;
    for (i = 1; i <= n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n; i++) {
      e += (a[i] - a[i + 1]);
      if (e < 0) paid += -e, e = 0;
    }
    printf("%d\n", paid);
  }
  return 0;
}
