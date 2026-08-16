#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <vector>

const long long M = 1000000000 + 7;

int main() {
  int n, x;
  std::cin >> n >> x;
  std::vector<int> s(n);
  for (auto &a : s)
    std::cin >> a;
  std::sort(s.begin(), s.end());

  long long f[x + 1];
  for (int xi = 0; xi <= x; ++xi) {
    f[xi] = xi;
  }
  for (int ni = 0; ni < n; ++ni) {
    long long next[x + 1];
    for (int xi = 0; xi <= x; ++xi) {
      next[xi] = (f[xi % s[ni]] + f[xi] * ni) % M;
    }
    for (int xi = 0; xi <= x; ++xi) {
      f[xi] = next[xi];
    }
  }
  std::cout << f[x] << std::endl;
  return 0;
}