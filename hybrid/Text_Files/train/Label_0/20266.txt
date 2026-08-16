#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e3 + 5;
int a[maxn];
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  sort(a + 1, a + n + 1);
  int ans = 1e9, s, d;
  for (int i = 0; i <= 20000; i++) {
    int l = 1e9, r = -1e9;
    for (int j = 1; j <= n; j++) {
      l = min(l, i * (j - 1) - a[j]);
      r = max(r, i * (j - 1) - a[j]);
    }
    int tmp = (r - l + 1) / 2;
    if (ans > tmp) {
      ans = tmp;
      s = -r + tmp;
      d = i;
    }
  }
  printf("%d\n%d %d\n", ans, s, d);
  return 0;
}
