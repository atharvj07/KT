#include <bits/stdc++.h>
using namespace std;
void solve() {
  int a, b;
  cin >> a >> b;
  int mod = ((a - 1) % b + b) % b;
  long long int sum = 0;
  for (int i = a; i <= b; i++) {
    int num = i / b;
    int den = mod + 1;
    if (den >= b) den -= b;
    mod = den;
    if (den == 0) continue;
    if (num % den != 0) continue;
    if (num / den >= 1 && num / den <= a) {
      sum += i;
    }
  }
  printf("%lld\n", sum);
}
void solve1() {
  long long int mod = 1000000007;
  long long int a, b;
  cin >> a >> b;
  long long int sum = 0;
  for (long long int t = 1; t < b; t++) {
    sum =
        (sum + ((b * t) % mod * (((a * (a + 1L)) / 2L) % mod)) % mod + t * a) %
        mod;
    assert(sum >= 0);
  }
  printf("%lld\n", sum);
}
int main() {
  int T = 1;
  for (int i = 1; i <= T; i++) {
    solve1();
  }
  return 0;
}
