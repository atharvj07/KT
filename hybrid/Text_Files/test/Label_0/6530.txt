#include <bits/stdc++.h>
using namespace std;
long long int ma = -1, mi = 1000000000000000;
inline long long int gcd(long long int a, long long int b) {
  return b ? gcd(b, a % b) : a;
}
inline long long int lcm(long long int a, long long int b, long long int MOD) {
  return a / gcd(a, b) * b % MOD;
}
long long int power(long long int x, unsigned int y) {
  if (y == 0)
    return 1;
  else if (y % 2 == 0)
    return power(x, y / 2) * power(x, y / 2);
  else
    return x * power(x, y / 2) * power(x, y / 2);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int i, j, k, a[100000] = {0}, n, m, b[100009] = {0}, c = 0, d = 0,
                         e[30] = {0}, x = 0;
  cin >> n >> m;
  for (i = 0; i < n; i++) {
    cin >> a[i];
  }
  for (i = 0; i < n - 1; i++) {
    if (a[i] + a[i + 1] < m) {
      d = m - a[i] - a[i + 1];
      a[i + 1] += d;
      c += d;
    }
  }
  cout << c << endl;
  for (i = 0; i < n; i++) cout << a[i] << " ";
}
