#include <bits/stdc++.h>
using namespace std;
int t, d, m, memo[32];
int f(int pos) {
  if ((1LL << pos) > d) return 0;
  if (memo[pos] != -1) return memo[pos];
  int ret = 1, temp;
  for (int i = 1; (1LL << (i + pos - 1)) <= d; ++i) {
    temp = 1LL * f(pos + i) *
           min(1LL << (pos + i), d + 1 - (1LL << (pos + i))) % m;
    ret = (ret + temp) % m;
  }
  return memo[pos] = ret;
}
int main() {
  for (scanf("%d", &t); t--;) {
    scanf("%d %d", &d, &m);
    memset(memo, -1, sizeof memo);
    int ans = 0;
    for (int i = 0; (1LL << i) <= d; ++i)
      ans = (ans + (1LL * f(i) * min(1LL << i, d + 1 - (1LL << i)) % m)) % m;
    printf("%d\n", ans);
  }
}
