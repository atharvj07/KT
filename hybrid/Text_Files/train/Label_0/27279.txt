#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e5 + 5;
int a[MAX];
int main() {
  int n, k;
  scanf("%d%d", &n, &k);
  int st = 1, nd = 100000, r = 0;
  while (st <= nd) {
    int mid = (st + nd) >> 1;
    long long v = mid * 1LL * (mid + 1) / 2LL;
    if (v < k) {
      r = max(r, (int)v);
      st = mid + 1;
    } else
      nd = mid - 1;
  }
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  printf("%d\n", a[k - r]);
  return 0;
}
