#include <bits/stdc++.h>
using namespace std;
long long gcd(long long a, long long b) { return a ? gcd(b % a, a) : b; }
bool test(long long q, long long b) {
  while (q != 1) {
    long long g = gcd(q, b);
    if (g == 1) {
      return false;
    }
    q /= g;
    b = g;
  }
  return true;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  while (n--) {
    long long p, q, b;
    cin >> p >> q >> b;
    q /= gcd(p, q);
    if (test(q, b)) {
      cout << "Finite\n";
    } else {
      cout << "Infinite\n";
    }
  }
}
