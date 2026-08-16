#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast")
int a[33];
string output[33];
inline string Str(int x) {
  string ret = "eax";
  ret[1] += x;
  return ret;
}
inline void dfs(int lim, int p, int n) {
  if (a[p] > n) return;
  if (p == lim) {
    if (a[p] != n) return;
    cout << p << '\n';
    for (register int i = (0); i <= (lim - 1); ++i) {
      cout << output[i] << '\n';
    }
    exit(0);
  }
  for (register int i = (0); i <= (p); ++i) {
    for (int j = 1; j <= 8; j <<= 1) {
      a[p + 1] = a[i] * j;
      if (a[p + 1] > n) continue;
      if (p + 1 == lim && a[p + 1] != n) continue;
      output[p] =
          "lea " + Str(p + 1) + ", [" + char('0' + j) + "*" + Str(i) + ']';
      dfs(lim, p + 1, n);
    }
  }
  for (register int i = (0); i <= (p); ++i) {
    for (register int j = (0); j <= (p); ++j) {
      for (int k = 1; k <= 8; k <<= 1) {
        a[p + 1] = a[i] + a[j] * k;
        if (a[p + 1] > n) continue;
        if (p + 1 == lim && a[p + 1] != n) continue;
        output[p] = "lea " + Str(p + 1) + ", [" + Str(i) + " + " +
                    char('0' + k) + '*' + Str(j) + ']';
        dfs(lim, p + 1, n);
      }
    }
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL), cout.tie(NULL);
  int n, m = 0;
  cin >> n;
  a[0] = 1;
  if (n == 1) {
    cout << 0 << '\n';
    return 0;
  }
  while (++m) dfs(m, 0, n);
  return 0;
}
