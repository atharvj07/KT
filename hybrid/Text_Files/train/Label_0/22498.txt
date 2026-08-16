#include <bits/stdc++.h>
using namespace std;
long long power(long x, long n) {
  if (n == 0) return 1;
  if (n == 1) return x;
  long n2 = n / 2;
  long long po = power(x, n2);
  if (n % 2) return po * po * x;
  return po * po;
}
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  a %= b;
  return gcd(b, a);
}
class CAliceAndBob {
 public:
  void solve(std::istream &cin, std::ostream &cout) {
    long long n, i, mx = 0, x, gc = 0;
    cin >> n;
    for (i = 0; i < n; i++) cin >> x, mx = max(x, mx), gc = gcd(gc, x);
    if ((mx / gc - n) % 2)
      cout << "Alice\n";
    else
      cout << "Bob\n";
  }
};
int main() {
  ios_base::sync_with_stdio(false), cin.tie(0);
  CAliceAndBob solver;
  std::istream &in(std::cin);
  std::ostream &out(std::cout);
  solver.solve(in, out);
  return 0;
}
