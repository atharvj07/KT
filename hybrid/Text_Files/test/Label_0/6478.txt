#include <bits/stdc++.h>
using namespace std;
int n;
long long m, ans;
int main() {
  scanf("%d%lld", &n, &m), m--;
  for (int i = 0; i <= n - 1; i++) {
    bool ka = ((m >> i) & 1), kb = ((m >> (i + 1)) & 1);
    if (i == n - 1) {
      if (ka)
        ans += (1LL << (i + 1));
      else
        ans++;
    } else {
      if (ka == kb)
        ans += (1LL << (i + 1));
      else
        ans++;
    }
  }
  printf("%lld\n", ans);
  return 0;
}
