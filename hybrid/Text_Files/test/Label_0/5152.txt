#include <bits/stdc++.h>
using namespace std;
inline long long read() {
  long long x = 0, f = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = (x << 1) + (x << 3) + (ch ^ 48);
    ch = getchar();
  }
  return x * f;
}
const int N = 1e6 + 7;
int n, ans[N];
long long m;
int main() {
  scanf("%d%lld", &n, &m);
  long long Max = m;
  for (int i = 1; i <= n; i++) {
    ans[i] = i;
    m -= i;
  }
  if (m < 0) {
    printf("-1\n");
    return 0;
  }
  for (int i = 1; i <= n / 2; i++) {
    int now = (n - i + 1) - i;
    if (m <= now) {
      swap(ans[n - i + 1 - (now - m)], ans[i]);
      m = 0;
      break;
    }
    swap(ans[n - i + 1], ans[i]);
    m -= now;
  }
  printf("%lld\n", Max - m);
  for (int i = 1; i <= n; i++) printf("%d ", i);
  printf("\n");
  for (int i = 1; i <= n; i++) printf("%d ", ans[i]);
  printf("\n");
  return 0;
}
