#include <bits/stdc++.h>
using namespace std;
const int MAX_N = 100000 + 2;
int main() {
  int n;
  int h[MAX_N], l[MAX_N], r[MAX_N];
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> h[i];
  }
  h[0] = 0;
  h[n + 1] = 0;
  l[0] = 0;
  for (int i = 1; i <= n; i++) {
    l[i] = min(l[i - 1] + 1, h[i]);
  }
  r[n + 1] = 0;
  for (int i = n; i > 0; i--) {
    r[i] = min(r[i + 1] + 1, h[i]);
  }
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    ans = max(ans, min(l[i], r[i]));
  }
  cout << ans << "\n";
  return 0;
}
