#include <bits/stdc++.h>
using ll = long long;
using namespace std;
const int N = 2e5 + 10, E = 65;
int n, cnt[E];
ll a[N];
int main() {
  scanf("%d", &n);
  for (auto i = 0, _end = n - 1; i <= _end; ++i) {
    scanf("%lld", a + i);
    cnt[__builtin_ctzll(a[i])]++;
  }
  int ans = max_element(cnt, cnt + E) - cnt;
  printf("%d\n", n - cnt[ans]);
  for (auto i = 0, _end = n - 1; i <= _end; ++i)
    if (__builtin_ctzll(a[i]) != ans) printf("%lld ", a[i]);
  puts("");
}
