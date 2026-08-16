#include <bits/stdc++.h>
using namespace std;
int main() {
  int x, k, a, b, p, s = 10e6, d, i;
  cin >> x >> k;
  for (i = 1; i <= x; i++) {
    cin >> a >> b;
    while (a < k) a = a + b;
    if (a < s) {
      s = a;
      d = i;
    }
  }
  cout << d << endl;
}
