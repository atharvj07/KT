#include <bits/stdc++.h>
int gcd(int a, int b) {
  while (b) {
    a %= b;
    std::swap(a, b);
  }
  return a;
}
int main() {
  std::cin.sync_with_stdio(false);
  std::cout.sync_with_stdio(false);
  int n;
  std::cin >> n;
  std::vector<int> xs(n);
  for (auto& x : xs) {
    std::cin >> x;
  }
  std::sort(xs.begin(), xs.end());
  std::vector<int> dists(n - 1);
  for (int i = 0; i < n - 1; ++i) {
    int x1 = xs.at(i);
    int x2 = xs.at(i + 1);
    dists.at(i) = x2 - x1;
  }
  int d = dists.at(0);
  for (const auto dx : dists) {
    d = gcd(d, dx);
  }
  int res = 0;
  for (const auto dx : dists) {
    res += dx / d - 1;
  }
  std::cout << res << std::endl;
  return 0;
}
