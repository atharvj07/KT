#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 100;
int t, n, a[N], b[N];
bool solve() {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    b[i] = a[i];
  }
  sort(b + 1, b + n + 1);
  int mn = b[1];
  for (int i = 1; i <= n; i++) {
    if (a[i] == b[i]) continue;
    if (a[i] % mn) {
      return false;
    }
  }
  return true;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> t;
  while (t--) {
    if (solve()) {
      cout << "YES\n";
    } else {
      cout << "NO\n";
    }
  }
  return 0;
}
