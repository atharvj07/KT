#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
void solve();
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long t;
  cin >> t;
  while (t--) {
    solve();
    cout << "\n";
  }
  cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl;
  return 0;
}
long long ceils(long long x, long long y) { return x / y + ((x % y) != 0); }
long long gcd(long long a, long long b) {
  if (b == 0)
    return a;
  else
    return gcd(b, a % b);
}
long long lcm(long long a, long long b) { return a / gcd(a, b) * b; }
void solve() {
  long long n;
  cin >> n;
  long long a[n], b[n], c[n];
  for (long long i = 0; i < n; i++) cin >> a[i];
  for (long long i = 0; i < n; i++) cin >> b[i];
  for (long long i = 0; i < n; i++) cin >> c[i];
  long long ans[n];
  ans[0] = a[0];
  for (long long i = 1; i < n; i++) {
    ans[i] = a[i];
    if (ans[i] == ans[i - 1]) ans[i] = b[i];
    if (ans[i] == ans[i - 1]) ans[i] = c[i];
  }
  long long ok = 0;
  for (long long i = 1; i < n; i++) {
    if (ans[i] == ans[i - 1]) {
      ok = 1;
      break;
    }
  }
  if (ok) {
    ans[0] = b[0];
    for (long long i = 1; i < n; i++) {
      ans[i] = b[i];
      if (ans[i] == ans[i - 1]) ans[i] = a[i];
      if (ans[i] == ans[i - 1]) ans[i] = c[i];
    }
    ok = 0;
    for (long long i = 1; i < n; i++) {
      if (ans[i] == ans[i - 1]) {
        ok = 1;
        break;
      }
    }
  }
  if (ok) {
    ans[0] = c[0];
    for (long long i = 1; i < n; i++) {
      ans[i] = c[i];
      if (ans[i] == ans[i - 1]) ans[i] = a[i];
      if (ans[i] == ans[i - 1]) ans[i] = b[i];
    }
    ok = 0;
    for (long long i = 1; i < n; i++) {
      if (ans[i] == ans[i - 1]) {
        ok = 1;
        break;
      }
    }
  }
  if (ans[n - 1] == ans[0]) {
    if (ans[n - 1] == a[n - 1]) {
      if (ans[n - 2] == b[n - 1])
        ans[n - 1] = c[n - 1];
      else
        ans[n - 1] = b[n - 1];
    } else if (ans[n - 1] == b[n - 1]) {
      if (ans[n - 2] == a[n - 1])
        ans[n - 1] = c[n - 1];
      else
        ans[n - 1] = a[n - 1];
    } else {
      if (ans[n - 2] == b[n - 1])
        ans[n - 1] = a[n - 1];
      else
        ans[n - 1] = b[n - 1];
    }
  }
  for (long long i = 0; i < n; i++) cout << ans[i] << " ";
}
