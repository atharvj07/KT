#include <bits/stdc++.h>
long long n;
int main() {
  std::cin.tie(0);
  std::ios::sync_with_stdio(false);
  std::cin >> n;
  n = n / 1000;
  if (!(n & 1)) std::cout << "3\n", exit(0);
  std::cout << "1\n";
  return 0;
}
