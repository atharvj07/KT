#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int x, y, z;
  while (~scanf("%lld%lld%lld", &x, &y, &z)) {
    long long n1 = x / z;
    long long m1 = x % z;
    long long n2 = y / z;
    long long m2 = y % z;
    long long sum = n1 + n2;
    long long k = 0;
    if (m1 + m2 >= z) {
      long long k1 = z - m1;
      long long k2 = z - m2;
      k = min(k1, k2);
      sum = sum + 1;
    }
    printf("%lld %lld\n", sum, k);
  }
  return 0;
}
