#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, k, t;
  cin >> t;
  while (t--) {
    cin >> n >> k;
    if (n % 2 == 0) {
      cout << n + 2 * k << endl;
    } else {
      long long int c = 0, ans;
      for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
          ans = n + i;
          c++;
          break;
        }
      }
      if (c == 0) {
        k = k - 1;
        if (k == 0) {
          cout << 2 * n << endl;
        } else {
          cout << n + n + 2 * k << endl;
        }
      } else {
        ans += 2 * (k - 1);
        cout << ans << endl;
      }
    }
  }
}
