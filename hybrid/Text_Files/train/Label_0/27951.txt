#include <bits/stdc++.h>
long long n;
int main() {
  std::cin.tie(0);
  std::ios::sync_with_stdio(false);
  std::cin >> n;
  if (n <= 50000) std::cout << "3\n", exit(0);
  if (n >= 54000) std::cout << "1\n", exit(0);
  std::cout << "2\n";
  return 0;
}
