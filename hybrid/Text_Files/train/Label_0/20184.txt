#include <bits/stdc++.h>
using namespace std;
const int N = 55;
void solve(int n, int m, int a, int b) {
  int offset = 0;
  if (n * a == m * b) {
    cout << "YES" << endl;
    for (int i = 0; i < n; ++i) {
      string ans(m, '0');
      for (int j = 0; j < a; ++j) ans[(j + offset) % m] = '1';
      cout << ans << endl;
      offset = (offset + a) % m;
    }
  } else
    cout << "NO" << endl;
}
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n, m, a, b;
    cin >> n >> m >> a >> b;
    solve(n, m, a, b);
  }
  return 0;
}
