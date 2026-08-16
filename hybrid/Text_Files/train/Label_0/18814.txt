#include <bits/stdc++.h>
using namespace std;
int N = 1e5;
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  long long n;
  cin >> n;
  int i;
  vector<int> a(2 * n);
  for (int i = 0; i < 2 * n; i++) {
    cin >> a[i];
  }
  long long l = 0, r = (2 * n - 1);
  long long mid = (l + r) / 2;
  long long left = mid, right = mid + 1;
  bool ok = true;
  sort(a.begin(), a.end());
  for (int i = 0; i < n && left >= 0 && right < 2 * n; i++) {
    if (a[left] == a[right]) {
      cout << "NO"
           << "\n";
      ok = false;
      return 0;
    } else {
      left--;
      right++;
    }
  }
  if (ok) {
    cout << "YES"
         << "\n";
  }
  return 0;
}
