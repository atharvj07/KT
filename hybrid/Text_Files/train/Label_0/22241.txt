#include <bits/stdc++.h>
using namespace std;
int main(void) {
  int n, x;
  cin >> n;
  cin >> x;
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    if (x % i == 0 && (x / i) <= n) ans++;
  }
  cout << ans;
  return 0;
}
