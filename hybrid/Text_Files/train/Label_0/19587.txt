#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    long long int n, k, p = 0, c = 0, ck;
    cin >> n >> k;
    if (k > n)
      cout << "NO" << endl;
    else {
      if ((k % 2 == 0 and n % 2 == 0) or (n % 2 == 1 and k % 2 == 1)) {
        if ((n - (k - 1)) % 2 == 1) {
          cout << "YES" << endl;
          for (int i = 0; i < k - 1; i++) {
            cout << 1 << ' ';
          }
          cout << n - (k - 1) << endl;
        } else
          cout << "NO" << endl;
      } else if (n % 2 == 0 and n >= k * 2) {
        cout << "YES" << endl;
        for (int i = 0; i < k - 1; i++) {
          cout << 2 << ' ';
        }
        cout << n - ((k - 1) * 2) << endl;
      } else
        cout << "NO" << endl;
    }
  }
}
