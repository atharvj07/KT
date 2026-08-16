#include <bits/stdc++.h>
using namespace std;
int n, t, p, sp[500000 + 10], sol[500000 + 10];
char s[500000 + 10];
bool isOK(int x) {
  sp[0] = x;
  for (int i = 1; i <= n; i++) sol[i] = 0;
  for (int i = 1; i <= n; i++) {
    if (s[i] == '.')
      sp[i] = sp[i - 1];
    else if (s[i] == 'H')
      sp[i] = sp[i - 1] - 1;
    else
      sp[i] = sp[i - 1] + 1;
  }
  int m = p;
  while (m <= n && sp[m] < 0) m++;
  if (m == n + 1) return false;
  int p1 = 1;
  while (s[p1] != 'H') p1++;
  int ans = m - p1, flag = 0, pr = 1;
  for (int i = 1; i <= m; i++) {
    if (i == m && !flag) ans = min(ans, sol[pr - 1]);
    if (sp[i] > 0)
      continue;
    else if (sp[i] < 0)
      flag = 1;
    else {
      if (!flag) {
        sol[i] = sol[pr - 1];
        pr = i + 1;
        continue;
      }
      ans = min(ans, 2 * m - i - pr + sol[pr - 1]);
      sol[i] = sol[pr - 1] + 2 * (i - pr);
      pr = i + 1;
      flag = 0;
    }
  }
  if (ans == 2000000000) ans = 0;
  return m + ans <= t;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> t >> (s + 1);
  for (int i = n; i; i--)
    if (s[i] == 'H') {
      p = i;
      break;
    }
  if (p > t) {
    cout << -1 << '\n';
    return 0;
  }
  int st = 0, dr = 500000, ans = 0;
  while (st <= dr) {
    int mij = (st + dr) / 2;
    if (isOK(mij)) {
      ans = mij;
      dr = mij - 1;
    } else
      st = mij + 1;
  }
  cout << ans << '\n';
  return 0;
}
