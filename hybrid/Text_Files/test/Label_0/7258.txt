#include <bits/stdc++.h>
int main() {
  long long n, k, a = 1, c;
  std::cin >> n >> k;
  c = n;
  for (int i = 0; i < k; i++) a = a * 10;
  c *= a;
  while (n != 0 && a != 0) {
    if (n >= a)
      n = n % a;
    else
      a = a % n;
  }
  std::cout << c / (a + n);
  return 0;
}
