#include <bits/stdc++.h>
using vi = std::vector<int>;
using pii = std::pair<int, int>;
using ll = long long;
using vll = std::vector<ll>;
int solve() {
  int n;
  unsigned a, b, c, d;
  scanf("%d", &n);
  scanf("%u%u%u%u", &a, &b, &c, &d);
  int n6 = (n - n / 2 - n / 3 + n / 6) + 1024;
  unsigned* bit = new unsigned[n6 / 32]();
  auto index = [](int i) { return i - i / 2 - i / 3 + i / 6 + 2; };
  auto calc = [](int p, int n) -> unsigned {
    unsigned r = 0;
    while (n /= p) r += n;
    return r;
  };
  auto set_bit = [&](int i) { bit[i >> 5] |= (1u << (i & 31)); };
  auto get_bit = [&](int i) { return (bit[i >> 5] >> (i & 31)) & 1; };
  auto f = [=](unsigned p) {
    return (unsigned)(((a * p + b) * p + c) * p + d);
  };
  unsigned ans = 0;
  ans += calc(2, n) * f(2);
  ans += calc(3, n) * f(3);
  int n_sqrt = sqrt(n);
  for (int i = 5, k = 2; i <= n; i += k, k ^= 6) {
    if (!get_bit(index(i))) {
      ans += calc(i, n) * f(i);
      if (i <= n_sqrt) {
        for (int j = i * i; j <= n; j += i) {
          if (j % 2 == 0 || j % 3 == 0) continue;
          set_bit(index(j));
        }
      }
    }
  }
  printf("%u\n", ans);
  delete[] bit;
  return 0;
}
int main() {
  solve();
  return 0;
}
