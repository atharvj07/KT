#include <bits/stdc++.h>
using namespace std;
const int P = 1000000007;
int k, m, p, ans;
int main() {
  int i, t;
  scanf("%d%d", &p, &k);
  ans = 1;
  if (k == 0) {
    for (i = 1; i <= p - 1; i++) ans = 1ll * ans * p % P;
  } else if (k == 1) {
    for (m = 1, t = k; t != 1; m++, t = 1ll * t * k % p)
      ;
    t = (p - 1) / m + 1;
    for (i = 1; i <= t; i++) ans = 1ll * ans * p % P;
  } else {
    for (m = 1, t = k; t != 1; m++, t = 1ll * t * k % p)
      ;
    t = (p - 1) / m;
    for (i = 1; i <= t; i++) ans = 1ll * ans * p % P;
  }
  printf("%d\n", ans);
  return 0;
}
