#include <bits/stdc++.h>
using namespace std;
int dx[8] = {0, 0, 1, 1, 1, -1, -1, -1};
int dy[8] = {1, -1, -1, 0, 1, -1, 0, 1};
const long long mod = 1e9 + 7;
const long long N = 1e6 + 5;
signed main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  long long t = 1;
  cin >> t;
  while (t--) {
    long long n, k;
    cin >> n >> k;
    if (n - k + 1 > 0 && (n - k + 1) % 2) {
      cout << "YES"
           << "\n";
      cout << n - k + 1 << " ";
      while (--k) cout << 1 << " ";
    } else if (n - 2 * (k - 1) > 0 && (n - 2 * (k - 1)) % 2 == 0) {
      cout << "YES"
           << "\n";
      cout << n - 2 * (k - 1) << " ";
      while (--k) cout << 2 << " ";
    } else
      cout << "NO";
    cout << "\n";
  }
}
