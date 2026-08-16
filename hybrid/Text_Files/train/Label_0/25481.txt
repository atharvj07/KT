#include <bits/stdc++.h>
using namespace std;
const long long MAX_N = 1e3 + 10;
const long long INF = 1e9 + 10;
const long long mod = 1e18;
ofstream out("output.txt");
ifstream in("intput.txt");
long long bpow(long long t, long long n) {
  long long ans = 1;
  while (n > 0) {
    if (n & 1) ans = (ans * t) % mod;
    t = (t * t) % mod, n >>= 1;
  }
  return ans;
}
bool mark[MAX_N][MAX_N];
long long x[MAX_N], y[MAX_N], ans = 0;
int32_t main() {
  ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
  cout << fixed << setprecision(12);
  long long n, m;
  cin >> n >> m;
  for (long long i = 0; i < n; i++)
    for (long long j = 0; j < m; j++) {
      char a;
      cin >> a;
      if (a == '*') mark[i][j] = 1, x[i]++, y[j]++, ans++;
    }
  for (long long i = 0; i < n; i++)
    for (long long j = 0; j < m; j++) {
      if (ans == x[i] + y[j] - mark[i][j]) {
        cout << "YES\n" << i + 1 << " " << j + 1;
        return 0;
      }
    }
  cout << "NO";
}
