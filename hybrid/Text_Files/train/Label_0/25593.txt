#include <bits/stdc++.h>
using namespace std;
bool isPrime(long long int n) {
  if (n <= 1) return 0;
  if (n <= 3) return 1;
  if (n % 2 == 0 || n % 3 == 0) return 0;
  for (long long int i = 5; i * i <= n; i += 6)
    if (n % i == 0 || n % (i + 2) == 0) return 0;
  return 1;
}
long long int gcd(long long int a, long long int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
long long int lcm(long long int a, long long int b) {
  return (a * b) / (gcd(a, b));
}
void swap(int& a, int& b) {
  a = a ^ b;
  b = a ^ b;
  a = a ^ b;
}
inline void solve() {
  long long int a, b;
  cin >> a >> b;
  int x = 0, y = 0, z = 0;
  while (a % 2 == 0) {
    a = a / 2;
    x++;
  }
  while (a % 3 == 0) {
    a = a / 3;
    y++;
  }
  while (a % 5 == 0) {
    a = a / 5;
    z++;
  }
  while (b % 2 == 0) {
    b = b / 2;
    x--;
  }
  while (b % 3 == 0) {
    b = b / 3;
    y--;
  }
  while (b % 5 == 0) {
    b = b / 5;
    z--;
  }
  if (a != b)
    cout << -1 << '\n';
  else
    cout << abs(x) + abs(y) + abs(z) << '\n';
}
signed main() {
  auto start_time = clock();
  cerr << setprecision(3) << fixed;
  cout << setprecision(15) << fixed;
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  solve();
  auto end_time = clock();
  cerr << "Execution time: "
       << (end_time - start_time) * (int)1e3 / CLOCKS_PER_SEC << " ms\n";
  return 0;
}
