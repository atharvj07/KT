#include <bits/stdc++.h>
using namespace std;
int main() {
  int q;
  long long int n, m, k, i, bar, left, diag;
  scanf("%d", &q);
  while (q--) {
    scanf("%lld %lld %lld", &n, &m, &k);
    if (n < m) {
      i = n;
      n = m;
      m = i;
    }
    if (n > k) {
      printf("-1\n");
      continue;
    } else {
      bar = n - m;
      if (bar % 2 == 1) {
        diag = k - 1;
      } else {
        diag = n - 1;
        left = k - n + 1;
        if (left % 2 == 0) {
          diag += left - 2;
        } else {
          diag += left;
        }
      }
      printf("%lld\n", diag);
    }
  }
  return 0;
}
