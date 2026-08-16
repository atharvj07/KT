#include <bits/stdc++.h>
using namespace std;
int highestPowerof2(int n) {
  int res = 0;
  for (int i = n; i >= 1; i--) {
    if ((i & (i - 1)) == 0) {
      res = i;
      break;
    }
  }
  return res;
}
bool isPowerOfTwo(int n) {
  if (n == 0) return false;
  return (ceil(log2(n)) == floor(log2(n)));
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    int ans = 0;
    for (int i = 0; i < n - 1; ++i) {
      if (a[i + 1] < a[i]) {
        int diff = a[i] - a[i + 1];
        int d = 0;
        if (diff == 1) {
          d = 0;
        } else {
          while (diff > 1) {
            diff >>= 1;
            d += 1;
          }
        }
        ans = max(ans, d + 1);
        a[i + 1] = a[i];
      }
    }
    cout << ans << "\n";
  }
}
