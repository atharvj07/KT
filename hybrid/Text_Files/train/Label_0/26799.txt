#include <bits/stdc++.h>
using namespace std;
long long mod = 1000000007;
long long max(long long a, long long b) { return a > b ? a : b; }
bool r(long long p1, long long p2) { return (p2 < p1); }
long long min(long long a, long long b) { return a < b ? a : b; }
long long gcd(long long a, long long b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}
const int N = 9;
long long power(long long a, long long b) {
  long long ans = 1;
  while (b > 0) {
    if (b & 1) {
      ans = (ans * a);
    }
    a = (a * a);
    b >>= 1;
  }
  return ans;
}
void solve() {
  int n;
  cin >> n;
  int a[n], b[n], c[n];
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < n; i++) cin >> b[i];
  for (int i = 0; i < n; i++) cin >> c[i];
  int p[n];
  p[0] = a[0];
  for (int i = 1; i < n; i++) {
    p[i] = a[i];
    if (p[i] == p[i - 1]) p[i] = b[i];
  }
  if (p[n - 1] == p[0]) p[n - 1] = c[n - 1];
  if (p[n - 1] == p[n - 2]) p[n - 1] = b[n - 1];
  for (int i = 0; i < n; i++) cout << p[i] << " ";
  cout << '\n';
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
