#include <bits/stdc++.h>
using namespace std;
signed main() {
  long long t;
  cin >> t;
  while (t--) {
    long long n;
    cin >> n;
    long long k = n % 3, z = 0;
    if (n == 1)
      cout << "0" << endl;
    else if (k != 0)
      cout << "-1" << endl;
    else {
      while (n % 6 == 0) {
        n /= 6;
        z++;
      }
      while (n % 3 == 0) {
        n /= 3;
        z += 2;
      }
      if (n == 1)
        cout << z << endl;
      else
        cout << "-1" << endl;
    }
  }
  return 0;
}
