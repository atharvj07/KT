#include <bits/stdc++.h>
using namespace std;
long long gcd(long long x, long long y) {
  if (x > y) {
    swap(x, y);
  }
  if (x == 0) {
    return y;
  } else {
    return gcd(x, y % x);
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    long long p, q, b;
    cin >> p >> q >> b;
    long long g = gcd(p, q);
    p /= g;
    q /= g;
    while (true) {
      g = gcd(q, b);
      if (g == 1) {
        break;
      } else {
        while (q % g == 0) {
          q /= g;
        }
      }
    }
    if (q == 1) {
      cout << "Finite\n";
    } else {
      cout << "Infinite\n";
    }
  }
  return 0;
}
