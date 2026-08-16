#include <bits/stdc++.h>
using namespace std;
const long long inf = 1e9;
const long long MOD = 1e9 + 7;
const long long N = 1e5 + 5;
long long n, x, y, d;
long long pref[N], surf[N];
string s;
void solve() {
  cin >> n >> s;
  s = '3' + s;
  long long go = 0, si = 0;
  for (long long i = 1; i <= n; i++) {
    go += (s[i] == 'G');
    si += (s[i] == 'S');
  }
  if (go == n) {
    cout << go << "\n";
    return;
  }
  if (si == 1) {
    cout << n - 1 << "\n";
    return;
  }
  if (si == n) {
    cout << "0"
         << "\n";
    return;
  }
  for (long long i = 1; i <= n; i++) {
    if (s[i] == 'G') {
      pref[i] = pref[i - 1] + 1;
    } else
      pref[i] = 0;
  }
  for (long long i = n; i > 0; i--) {
    if (s[i] == 'G')
      surf[i] = surf[i + 1] + 1;
    else
      surf[i] = 0;
  }
  long long ans = 0;
  for (long long i = 1; i <= n; i++) {
    long long cnt = pref[i - 1] + surf[i + 1] + 1;
    ans = max(ans, cnt);
  }
  ans = min(ans, go);
  cout << ans << "\n";
}
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  long long t = 1;
  while (t--) solve();
  return 0;
}
