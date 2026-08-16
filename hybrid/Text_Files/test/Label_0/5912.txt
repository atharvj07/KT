#include <bits/stdc++.h>
using namespace std;
long long gcd(long long a, long long b) { return b ? gcd(b, a % b) : a; }
long long lcm(long long a, long long b) { return a / gcd(a, b) * b; }
int main() {
  srand(time(0));
  ios_base::sync_with_stdio(0);
  long long x, y, a, b;
  cin >> x >> y >> a >> b;
  long long l = lcm(x, y);
  long long n1 = (a - 1) / l;
  long long n2 = b / l;
  cout << (n2 - n1) << '\n';
  return 0;
}
