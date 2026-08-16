#include <bits/stdc++.h>
using namespace std;
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
long long mod = (long long)1e9 + 7;
void solve() {
  long long n, m;
  cin >> n >> m;
  string s, t;
  cin >> s >> t;
  long long ps1 = 0, ps2 = n - 1, pt1 = 0, pt2 = m - 1;
  long long d1 = 1, d2 = 1;
  while (true) {
    if (d1) {
      if (s[ps1] == t[pt1]) {
        ps1++;
        pt1++;
      } else if (s[ps1] == '*') {
        d1 = 0;
      } else {
        cout << "NO\n";
        return;
      }
    }
    if (d2) {
      if (s[ps2] == t[pt2]) {
        ps2--;
        pt2--;
      } else if (s[ps2] == '*') {
        d2 = 0;
      } else {
        cout << "NO\n";
        return;
      }
    }
    if (ps1 >= ps2) {
      break;
    }
    if (pt1 > pt2) {
      cout << "NO\n";
      return;
    }
  }
  long long c = 0;
  for (long long i = 0; i < n; i++)
    if (s[i] == '*') c++;
  if (c and n < m)
    cout << "YES\n";
  else if (n < m)
    cout << "NO\n";
  else if (!c and n == m)
    cout << "YES\n";
  else if (!c and n != m)
    cout << "NO\n";
  else
    cout << "YES\n";
}
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  long long t = 1;
  for (long long i = 0; i < t; i++) solve();
  return 0;
}
