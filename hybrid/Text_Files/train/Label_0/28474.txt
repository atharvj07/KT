#include <bits/stdc++.h>
using namespace std;
long long funk(long long x, long long y) {
  bool used[10000];
  long long res = 1;
  for (long long i = 1; i <= 100; i++) used[i] = 0;
  for (long long i = x + 1; i <= y; i++) {
    res *= i;
    for (long long j = 2; j <= y - x; j++) {
      if (!used[j] && res % j == 0) {
        res /= j;
        used[j] = 1;
      }
    }
  }
  return res;
}
int main() {
  long long n, m, t, i, j;
  cin >> n >> m >> t;
  long long s = 0;
  for (i = 4; i < t && i <= n; i++) {
    if (t - i <= m) {
      s += (funk(i, n) * funk(t - i, m));
    }
  }
  cout << s << "\n";
}
