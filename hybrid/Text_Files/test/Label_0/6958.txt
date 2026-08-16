#include <bits/stdc++.h>
int main() {
  std::ios::sync_with_stdio(false);
  long long n, k;
  std::cin >> n >> k;
  std::vector<long long> answ;
  long long cur = 1;
  for (long long i = 63; i >= 1; --i) {
    long long power = (1LL << i) - 1;
    while (power <= n) {
      n -= power;
      for (long long j = 0; j < i; ++j) {
        answ.push_back(cur);
      }
      cur += k;
    }
  }
  std::cout << answ.size() << '\n';
  for (long long i = 0; i < answ.size(); ++i) {
    std::cout << answ[i] << ' ';
  }
}
