#include <bits/stdc++.h>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int n;
    cin >> n;
    int a[(n)];
    for (int i = 0; i < n; i++) cin >> a[i];
    int lo = 0, mid, hi = n - 1, i, j, ans, k;
    while (lo != hi) {
      mid = lo + (hi - lo) / 2;
      i = mid;
      j = n - 1;
      ans = 1;
      while (i < j) {
        k = min(a[i], a[j]);
        if (a[(i + 1)] < k || a[j - 1] < k) {
          ans = 0;
          break;
        } else {
          if (a[i] == k)
            i++;
          else
            j--;
        }
      }
      if (ans == 0)
        lo = mid + 1;
      else
        hi = mid;
    }
    cout << hi << endl;
  }
}
