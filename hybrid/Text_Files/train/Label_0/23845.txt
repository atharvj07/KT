#include <bits/stdc++.h>
using namespace std;
long long n, k, l, r, bst[20000], m, t;
long long ar[10000];
int main() {
  ios_base::sync_with_stdio(0);
  cin >> n >> k;
  for (int i = 1; i <= n; i++) cin >> ar[i];
  l = 0;
  r = 2000000000;
  while (l < r) {
    m = (0ll + l + r) / 2;
    for (int i = 1; i <= n; i++) bst[i] = 1;
    for (int i = 1; i <= n; i++)
      for (int j = i + 1; j <= n; j++) {
        if (abs(ar[j] - ar[i]) <= m * (j - i)) bst[j] = max(bst[j], bst[i] + 1);
      }
    t = 0;
    for (int i = 1; i <= n; i++) t = max(t, bst[i]);
    if (t + k >= n)
      r = m;
    else
      l = m + 1;
  }
  cout << l << endl;
  cin.get();
  cin.get();
  return 0;
}
