#include <bits/stdc++.h>
using namespace std;
const long long maxn = 1e3 + 5;
const long long mod = 1e9 + 7;
const long long p = 31;
void c_p_c() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
}
void solve() {
  long long n;
  cin >> n;
  long long a[n];
  for (long long i = (0); i < (n); i++) cin >> a[i];
  bool ok = true;
  while (ok) {
    for (long long i = 0; i < n - 1; i++) {
      if (a[i] > a[i + 1]) {
        swap(a[i], a[i + 1]);
        cout << i + 1 << " " << i + 2 << "\n";
        break;
      }
    }
    if (is_sorted(a, a + n)) ok = false;
  }
}
int32_t main() {
  c_p_c();
  solve();
}
