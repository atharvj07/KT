#include <bits/stdc++.h>
using namespace std;
long long a, b, k;
long long d[360365];
const long long lcm = 360360;
long long giam(long long a, long long b) {
  d[0] = 0;
  for (int i = 1; i <= a - b; i++) {
    d[i] = d[i - 1] + 1;
    for (int j = 2; j <= k; j++)
      if ((b + i) % j <= i) d[i] = min(d[i], d[i - (b + i) % j] + 1);
  }
  return d[a - b];
}
int main() {
  scanf("%lld %lld %lld", &a, &b, &k);
  if ((a - b) < lcm)
    printf("%lld\n", giam(a, b));
  else
    printf("%lld\n", giam(a % lcm, 0) + giam(lcm, b % lcm) +
                         giam(lcm, 0) * (a / lcm - (b + lcm - 1) / lcm));
}
