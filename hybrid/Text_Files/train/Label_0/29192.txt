#include <bits/stdc++.h>
using namespace std;
const long long mod = 1000000007;
long long gcd(long long a, long long b) {
  while (a && b) a > b ? a %= b : b %= a;
  return a + b;
}
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0),
      cin.exceptions(cin.failbit);
  long long x, a, b;
  cin >> x;
  if (x == 1) {
    cout << 1 << " " << 1 << '\n';
    return 0;
  }
  vector<long long> v;
  for (int i = 1; i <= sqrt(x) + 1; i++) {
    if (x % i == 0) {
      v.push_back(i);
      v.push_back(x / i);
    }
  }
  long long ans = 10000000000000000;
  for (int i = 0; i < v.size() - 1; i++) {
    long long x1 = v[i];
    long long x2 = v[i + 1];
    if (((x1 * 1ll * x2) / gcd(x1, x2)) == x) {
      long long mx = max(v[i], v[i + 1]);
      if (mx < ans) {
        a = v[i];
        b = v[i + 1];
        ans = mx;
      }
    }
  }
  cout << a << " " << b << '\n';
  return 0;
}
