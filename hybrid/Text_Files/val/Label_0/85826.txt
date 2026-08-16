#include <bits/stdc++.h>
using namespace std;
int a[100007];
int binary_search(int l, int r, int q) {
  int m;
  while (r - l > 1) {
    m = (l + r) / 2;
    if (a[m] > q)
      r = m;
    else
      l = m;
  }
  if (a[r] <= q)
    return r;
  else
    return l;
}
int main() {
  int n, d;
  cin >> n >> d;
  if (n < 3) {
    cout << "0";
    return 0;
  }
  for (int i = 1; i <= n; i++) cin >> a[i];
  long long ans = 0;
  for (int i = 1; i <= n - 2; i++) {
    long long t = binary_search(i, n, a[i] + d);
    t = t - i - 1;
    t = (t * (t + 1)) / 2;
    if (t >= 0) ans += t;
  }
  cout << ans;
  return 0;
}
