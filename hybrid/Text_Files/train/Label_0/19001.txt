#include <bits/stdc++.h>
using namespace std;
int main() {
  long long t;
  cin >> t;
  while (t--) {
    long long a, b;
    cin >> a >> b;
    if (2 * a <= b) {
      cout << a << endl;
    } else if (2 * b <= a) {
      cout << b << endl;
    } else {
      cout << (a + b) / 3 << endl;
    }
  }
  return 0;
}
