#include <bits/stdc++.h>
using namespace std;
long long POW(long long a, long long b, long long MMM = 1000000007) {
  long long ret = 1;
  for (; b; b >>= 1, a = (a * a) % MMM)
    if (b & 1) ret = (ret * a) % MMM;
  return ret;
}
long long gcd(long long a, long long b) {
  for (; b; a %= b, swap(a, b))
    ;
  return a;
}
long long lcm(long long a, long long b) { return a * b / gcd(a, b); };
int dr[] = {0, 1, 0, -1, 1, 1, -1, -1};
int dc[] = {1, 0, -1, 0, 1, -1, 1, -1};
int n, m, k, t;
long long a[200001];
long long b[200001];
int main() {
  ios::sync_with_stdio(0), cin.tie(NULL), cout.tie(NULL);
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    long long ma = 1e9, mb = 1e9;
    for (int i = 0; i < n; i++) {
      ma = min(a[i], ma);
      mb = min(b[i], mb);
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) {
      if (a[i] == ma && b[i] == mb) continue;
      if (a[i] != ma && b[i] != mb) {
        long long mn = min(a[i] - ma, b[i] - mb);
        ans += mn;
        a[i] -= mn;
        b[i] -= mn;
        ans += a[i] - ma + b[i] - mb;
      } else if (a[i] != ma) {
        ans += a[i] - ma;
      } else {
        ans += b[i] - mb;
      }
    }
    cout << ans << '\n';
  }
}
