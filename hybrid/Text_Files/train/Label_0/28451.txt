#include <bits/stdc++.h>
using namespace std;
const long long INF = 1e18;
const int32_t M = 1e9 + 7;
bool check(long long x, string t, string p, long long a[]) {
  for (long long i = 0; i < x; i++) {
    t[a[i] - 1] = '*';
  }
  if (x == 0) return true;
  long long i = 0, j = 0;
  while (i < t.length() && j < p.length()) {
    if (t[i] == p[j]) {
      i++;
      j++;
    } else
      i++;
  }
  return (j == p.length());
}
void solve() {
  string t, p;
  cin >> t >> p;
  long long n = t.size();
  long long a[n];
  for (long long i = 0; i < n; i++) cin >> a[i];
  long long st = 0, ed = n;
  while (st <= ed) {
    long long mid = st + (ed - st) / 2;
    if (check(mid, t, p, a))
      st = mid + 1;
    else
      ed = mid - 1;
  }
  if (check(st, t, p, a) == false) cout << st - 1;
}
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  long long t = 1;
  while (t--) solve();
  return 0;
}
