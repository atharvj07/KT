#include <bits/stdc++.h>
using namespace std;
long long N, M, a[300005], p[300005], diff, k;
long long gcd(long long x, long long y) {
  if (y == 0) return x;
  return gcd(y, x % y);
}
int main() {
  cin >> N >> M;
  for (long long i = 0; i < N; i++) cin >> a[i];
  for (long long i = 0; i < M; i++) cin >> p[i];
  for (long long i = 1; i < N; i++) {
    diff = a[i] - a[i - 1];
    k = gcd(k, diff);
  }
  for (long long i = 0; i < M; i++) {
    if (gcd(k, p[i]) == p[i]) {
      cout << "YES\n" << a[0] << " " << i + 1 << "\n";
      return 0;
    }
  }
  cout << "NO\n";
  return 0;
}
