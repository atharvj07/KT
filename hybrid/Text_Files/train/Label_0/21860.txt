#include <bits/stdc++.h>
using namespace std;
int n, mp[10001];
int main() {
  while (scanf("%d", &n) != EOF) {
    memset(mp, 0, sizeof(mp));
    for (int i = 1; i <= n - 1; i++) {
      int a, b;
      scanf("%d%d", &a, &b);
      mp[a]++;
      mp[b]++;
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) {
      ans += mp[i] * (mp[i] - 1) / 2;
    }
    printf("%d\n", ans);
  }
  return 0;
}
