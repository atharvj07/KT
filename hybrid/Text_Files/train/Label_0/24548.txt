#include <bits/stdc++.h>
using namespace std;
int main() {
  long long Q, q, n, i, nr, sum, x, a, b;
  cin >> Q;
  for (q = 1; q <= Q; q++) {
    cin >> n;
    sum = x = 0;
    for (i = 1; i <= n; i++) {
      cin >> nr;
      sum += nr;
      x = x ^ nr;
    }
    a = x;
    x = x ^ a;
    sum += a;
    b = sum;
    cout << 2 << "\n" << a << " " << b << "\n";
  }
  return 0;
}
