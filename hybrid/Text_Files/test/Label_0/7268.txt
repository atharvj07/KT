#include <bits/stdc++.h>
using namespace std;
inline long long getint() {
  long long ssum = 0, ff = 1;
  char ch;
  for (ch = getchar(); !isdigit(ch) && ch != '-'; ch = getchar())
    ;
  if (ch == '-') ff = -1, ch = getchar();
  for (; isdigit(ch); ch = getchar()) ssum = ssum * 10 + ch - '0';
  return ssum * ff;
}
const long long M = 105, N = 22;
long long n, m, b, ans = 2e18, f[1 << N];
struct node {
  long long s, k, w;
  friend bool operator<(node x, node y) { return x.k < y.k; }
} a[M];
signed main() {
  cin >> n >> m >> b;
  for (long long i = 1; i <= n; i++) {
    a[i].w = getint();
    a[i].k = getint();
    long long T = getint();
    for (long long j = 1; j <= T; j++) a[i].s |= (1 << (getint() - 1));
  }
  sort(a + 1, a + n + 1);
  memset(f, 0x7f, sizeof(f));
  long long inf = f[0];
  f[0] = 0;
  for (long long i = 1; i <= n; i++) {
    for (long long s = (1 << m) - 1; s >= 0; s--) {
      if (f[s] == inf) continue;
      f[s | a[i].s] = min(f[s | a[i].s], f[s] + a[i].w);
    }
    if (f[(1 << m) - 1] != inf) ans = min(ans, f[(1 << m) - 1] + b * a[i].k);
  }
  cout << (ans == 2e18 ? -1 : ans) << endl;
  return 0;
}
