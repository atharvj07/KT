#include <bits/stdc++.h>
using namespace std;
int n, m;
long long u;
long long a[1000];
long long d[1000];
long long minn = -1e17;
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) {
    scanf("%lld", &a[i]);
    d[i] = minn;
  }
  for (int i = n; i >= 0; --i) {
    for (int j = n; j >= 0; --j) {
      if (j == 0) {
        u = minn;
      } else
        u = d[j - 1];
      d[j] = max(min(d[j] + a[i], 0LL), u);
    }
  }
  while (m--) {
    scanf("%lld", &u);
    int k = lower_bound(d, d + n + 1, -u) - d;
    cout << k << endl;
  }
  return 0;
}
