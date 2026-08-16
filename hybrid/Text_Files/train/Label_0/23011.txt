#include <bits/stdc++.h>
const int N = (int)1e3 + 5;
int n;
int a[N];
int b[N];
int u[N];
int gcd(int a, int b) { return !b ? a : gcd(b, a % b); }
int main() {
  int ts;
  scanf("%d", &ts);
  while (ts--) {
    for (int i = 0; i < N; ++i) {
      u[i] = 0;
    }
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &a[i]);
    }
    int g = 0;
    for (int p = 1; p <= n; ++p) {
      int mx = -1;
      int ind = -1;
      for (int i = 0; i < n; ++i) {
        if (!u[i]) {
          if (mx < gcd(g, a[i])) {
            mx = gcd(g, a[i]);
            ind = i;
          }
        }
      }
      assert(ind != -1);
      u[ind] = 1;
      g = gcd(g, a[ind]);
      b[p] = a[ind];
    }
    for (int i = 1; i <= n; ++i) {
      printf("%d ", b[i]);
    }
    printf("\n");
  }
}
