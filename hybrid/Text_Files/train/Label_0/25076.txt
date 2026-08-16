#include <bits/stdc++.h>
using namespace std;
int a[200];
int main() {
  int n;
  cin >> n;
  int pos = 0, maxx = 0;
  for (int i = 1; i <= n; i++) cin >> a[i];
  for (int i = 1; i <= n; i++) {
    if (maxx < a[i]) {
      maxx = a[i];
      pos = i;
    }
  }
  if (maxx == 0) return puts("0"), 0;
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    ans += 4 * a[i] * (i - 1);
  }
  cout << ans << endl;
  return 0;
}
