#include <bits/stdc++.h>
using namespace std;
const int N = 3e5 + 5;
int n, m;
int a[N];
bool ok(int x) {
  int pre;
  if (a[1] + x >= m)
    pre = 0;
  else
    pre = a[1];
  for (int i = 2; i <= n; ++i) {
    if (a[i] <= pre) {
      if (a[i] + x < pre) return 0;
    } else {
      if (a[i] + x >= m && (a[i] + x) - m >= pre)
        pre = pre;
      else
        pre = a[i];
    }
  }
  return 1;
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
  int ans, l = 0, r = m;
  while (l <= r) {
    int mid = l + r >> 1;
    if (ok(mid))
      ans = mid, r = mid - 1;
    else
      l = mid + 1;
  }
  printf("%d\n", ans);
  return 0;
}
