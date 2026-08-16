#include <bits/stdc++.h>
using namespace std;
int a[5000];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> a[i];
  int cnt = 0, ans = 0;
  while (true) {
    for (int i = 0; i < n; i++)
      if (a[i] <= cnt) a[i] = n + 1, cnt++;
    if (cnt == n) break;
    ans++;
    for (int i = n - 1; i >= 0; --i)
      if (a[i] <= cnt) a[i] = n + 1, cnt++;
    if (cnt == n) break;
    ans++;
  }
  cout << ans;
  return 0;
}
