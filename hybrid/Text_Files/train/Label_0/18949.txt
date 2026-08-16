#include <bits/stdc++.h>
const int inf = (1ll << 30) - 1;
const int maxn = (int)1e5 + 10;
const int mod = (int)1e9 + 7;
using namespace std;
int n, m;
int x[100100];
int last[100100];
void solve() {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    int y;
    cin >> x[i] >> y;
    int ans = 0;
    for (int j = 1; j * j <= x[i]; j++) {
      if (x[i] % j == 0) {
        if (last[j] < i - y) ans++;
        if (x[i] != j * j) {
          if (last[x[i] / j] < i - y) ans++;
        }
        last[j] = i;
        last[x[i] / j] = i;
      }
    }
    cout << ans << "\n";
  }
}
int main() {
  int t = 1;
  for (int i = 1; i <= t; i++) {
    solve();
  }
  return 0;
}
