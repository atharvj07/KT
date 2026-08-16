#include <bits/stdc++.h>
using namespace std;
const long long infl = 1e18 + 5;
long long int m, n, p, q, x, y, cn, k, tmp1, tmp,
    mx = -1, f, val, sz, sm, cnt, ans = infl, t = 1, i, j, ind = -1, ci;
long long int a[104], mn[104][104];
long long int getmin(int start, int end) {
  int i;
  long long int y = infl;
  for (i = start; i < end + 1; i++) {
    y = min(y, a[i]);
  }
  return y;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  if (fopen("input.txt", "r")) {
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
  }
  long long int r1, c1, r2, c2;
  cin >> n;
  for (i = 0; i < n; i++) {
    cin >> a[i];
    a[i]++;
  }
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      mn[i][j] = infl;
    }
  }
  cin >> r1 >> c1 >> r2 >> c2;
  r1--;
  r2--;
  for (i = 0; i < n; i++) {
    for (j = i; j < n; j++) {
      if (j == 0)
        mn[i][j] = a[i];
      else
        mn[i][j] = min(mn[i][j - 1], a[j]);
      mn[j][i] = mn[i][j];
    }
  }
  for (i = 0; i < n; i++) {
    if (i >= r1)
      sm = min(c1, getmin(r1 + 1, i));
    else
      sm = min(c1, getmin(i, r1 - 1));
    if (i <= r2)
      val = abs(r1 - i) + abs(r2 - i) + abs(c2 - min(sm, getmin(i + 1, r2)));
    else
      val = abs(r1 - i) + abs(r2 - i) + abs(c2 - min(sm, getmin(r2, i - 1)));
    ans = min(ans, val);
  }
  cout << ans;
  return 0;
}
