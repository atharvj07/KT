#include <bits/stdc++.h>
long long max(long long a, long long b) { return a > b ? a : b; }
const int maxn = 500005;
int a[maxn];
int n, k;
long long S, s, d, D, p, L, R;
void t_main() {
  scanf("%d %d", &n, &k);
  for (int i = 0; i < n; i++) {
    scanf("%d", a + i);
    S += a[i];
  }
  std::sort(a, a + n);
  d = S / n;
  for (int i = 0; i < n; i++)
    if (a[i] < d) s += d - a[i];
  D = 0;
  d = (S + n - 1) / n;
  for (int i = 0; i < n; i++)
    if (a[i] > d) D += a[i] - d;
  if (D > s) s = D;
  if (s <= k) k = s;
  L = a[0];
  R = a[n - 1];
  s = k;
  for (int i = n - 1; i > 0; i--) {
    int N = n - i;
    int delta = a[i] - a[i - 1];
    if (s >= 1LL * delta * N) {
      s -= 1LL * delta * N;
      R = a[i - 1];
    } else {
      R -= s / N;
      break;
    }
  }
  s = k;
  for (int i = 0; i < n - 1; i++) {
    int N = i + 1;
    int delta = a[i + 1] - a[i];
    if (s >= 1LL * delta * N) {
      s -= 1LL * delta * N;
      L = a[i + 1];
    } else {
      L += s / N;
      break;
    }
  }
  printf("%d\n", (int)(R - L));
}
void run() {
  int t = 1;
  while (t--) t_main();
}
int main() {
  run();
  return 0;
}
