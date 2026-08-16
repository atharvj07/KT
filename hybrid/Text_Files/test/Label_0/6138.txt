#include <bits/stdc++.h>
using namespace std;
const int inf = 1 << 30;
const long long INF = 1e18;
const int mod = 998244353;
const int maxn = 1e5 + 2;
const int mov[4][2] = {-1, 0, 1, 0, 0, 1, 0, -1};
const int Mov[8][2] = {-1, -1, -1, 0, -1, 1, 0, -1, 0, 1, 1, -1, 1, 0, 1, 1};
inline int read() {
  int x = 0, f = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = x * 10 + ch - '0';
    ch = getchar();
  }
  return x * f;
}
void read(int &x) {
  x = 0;
  int f = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = x * 10 + ch - '0';
    ch = getchar();
  }
  x *= f;
  return;
}
int main(void) {
  std::ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
  int n;
  while (cin >> n) {
    std::vector<long long> a(n);
    std::vector<int> b(n);
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
      cin >> b[i];
    }
    sort(b.begin(), b.end());
    for (int i = 0; i < n; ++i) {
      a[i] *= (long long)(i + 1) * (n - i);
    }
    sort(a.begin(), a.end());
    long long ans = 0;
    for (long long i = 0; i < n; ++i) {
      ans += (a[i] % mod * b[n - 1 - i]) % mod;
      ans %= mod;
    }
    cout << ans << endl;
  }
}
