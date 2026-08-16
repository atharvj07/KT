#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx")
using namespace std;
const int N = 100005;
int n, q, Min1[N], Min2[N], opt, l, r, k;
int main() {
  scanf("%d", &q);
  n = 1e5;
  for (int i = 1; i <= n; i++) Min1[i] = Min2[i] = 1e9 + 1;
  while (q--) {
    scanf("%d", &opt);
    if (opt == 1) {
      scanf("%d%d%d", &l, &r, &k);
      if (k < 0) {
        for (int i = l; i < r; i++)
          if (Min1[i] > -k) Min1[i] = -k;
      } else {
        for (int i = l; i < r; i++)
          if (Min2[i] > k) Min2[i] = k;
      }
    } else {
      scanf("%d%d", &l, &r);
      long long ans = 0;
      for (int i = l; i < r; i++)
        if (Min1[i] < 1e9 + 1 && Min2[i] < 1e9 + 1) ans += Min1[i] + Min2[i];
      printf("%lld\n", ans);
    }
  }
  return 0;
}
