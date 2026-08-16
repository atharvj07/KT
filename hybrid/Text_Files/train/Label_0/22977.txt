#include <bits/stdc++.h>
using namespace std;
int jud(long long N, long long M, long long K) {
  int i;
  if (K < 40 && (1ll << K) < N) return 0;
  long long cnt = 0, sum = 0, x = 1;
  for (i = 0;; i++) {
    long long tmp = min(N - cnt, x);
    cnt += tmp;
    sum += tmp * i;
    if (cnt == N) break;
    x = x * (K - i) / (i + 1);
  }
  M = min(M, N - M);
  return (sum <= K * M);
}
int main() {
  int t, n, m;
  cin >> t;
  while (t--) {
    cin >> n >> m;
    m = min(n / 2, m);
    int l = 0, r = n - 1;
    while (l < r) {
      int d = l + r >> 1;
      if (jud(n, m, d))
        r = d;
      else
        l = d + 1;
    }
    printf("%d\n", l);
  }
  return 0;
}
