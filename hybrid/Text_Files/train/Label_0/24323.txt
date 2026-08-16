#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k;
  scanf("%d%d", &n, &k);
  k = 240 - k;
  int s = 0, ans = 0;
  for (int i = 1; i <= n; i++) {
    s += 5 * i;
    if (s > k) break;
    ans++;
  }
  printf("%d\n", ans);
  return 0;
}
