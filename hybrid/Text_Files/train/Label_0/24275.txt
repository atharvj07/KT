#include <bits/stdc++.h>
using namespace std;
const int N = (int)1e5 + 9;
long long power(long long x, long long y) {
  if (y == 0) return 1;
  long long temp = power(x, y / 2);
  if (y % 2 == 1)
    return temp * temp * x;
  else
    return temp * temp;
}
void solve() {
  long long n;
  cin >> n;
  long long s = 1;
  for (long long i = 2;;) {
    s += i;
    if (n % s == 0) {
      cout << n / s << "\n";
      return;
    }
    i = i << 1;
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
