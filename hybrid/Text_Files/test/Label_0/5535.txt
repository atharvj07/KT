#include <bits/stdc++.h>
using namespace std;
int w[100005];
int main() {
  int n, l, r, ql, qr;
  scanf("%d %d %d %d %d", &n, &l, &r, &ql, &qr);
  w[0] = 0;
  for (int i = 1; i <= n; i++) {
    scanf("%d", &w[i]);
    w[i] += w[i - 1];
  }
  int ans = 0x7fffffff;
  for (int i = 0; i <= n; i++) {
    int tmp = w[i] * l + (w[n] - w[i]) * r;
    if (i < n - i) tmp += (n - 2 * i - 1) * qr;
    if (i > n - i) tmp += (2 * i - n - 1) * ql;
    ans = min(ans, tmp);
  }
  printf("%d\n", ans);
  return 0;
}
