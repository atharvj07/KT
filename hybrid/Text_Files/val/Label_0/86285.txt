#include <bits/stdc++.h>
using namespace std;
inline int mul(int a, int b) { return int(a * 1ll * b % 998244353); }
inline int norm(int a) {
  if (a >= 998244353) a -= 998244353;
  if (a < 0) a += 998244353;
  return a;
}
inline int binPow(int a, int k) {
  int ans = 1;
  while (k > 0) {
    if (k & 1) ans = mul(ans, a);
    a = mul(a, a);
    k >>= 1;
  }
  return ans;
}
inline int subtract(int a, int b) { return norm(a - b); }
inline int sum(int a, int b) { return int((a + b) % 998244353); }
inline int inv(int a) { return binPow(a, 998244353 - 2); }
long long ceil_int(long long a, long long b) { return a / b + (a % b != 0); }
long long gcd(long long a, long long b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}
long long lcm(long long a, long long b) { return (a * b) / gcd(a, b); }
int n, m;
vector<vector<int>> g;
vector<int> stp;
int main() {
  cin >> n >> m;
  g.resize(n);
  stp.resize(n);
  vector<int> used(n);
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    g[a].push_back(b);
    g[b].push_back(a);
    stp[a]++;
    stp[b]++;
  }
  if (m == 0) {
    cout << 0;
    return 0;
  }
  vector<vector<int>> d(6, vector<int>(6));
  int res = 0;
  vector<int> color(n);
  int change = 0;
  for (int i = 0; i < pow(6, n); i++) {
    int cur = 0;
    if (change) {
      for (int j = n - 1; j >= 0; j--) {
        if (color[j] == 5) {
          color[j] = 0;
        } else {
          color[j]++;
          break;
        }
      }
    }
    for (int j = 0; j < n; j++) {
      for (int t = 0; t < g[j].size(); t++) {
        int to = g[j][t];
        if (d[color[j]][color[to]] == 0) {
          cur++;
          d[color[j]][color[to]] = 1;
          d[color[to]][color[j]] = 1;
        }
      }
    }
    change = 1;
    res = max(res, cur);
    for (int j = 0; j < 6; j++) {
      for (int t = 0; t < 6; t++) {
        d[j][t] = 0;
      }
    }
  }
  cout << res;
  return 0;
}
