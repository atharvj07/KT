#include <bits/stdc++.h>
using namespace std;
const int MAXN = 444444;
int n, m, a[MAXN], b[MAXN], c[MAXN], tc[MAXN];
void read() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  scanf("%d", &m);
  for (int i = 1; i <= m; i++) scanf("%d", &b[i]);
}
long long go(int start, int dir) {
  for (int i = 1; i <= n; i++) tc[i] = c[i];
  long long res = 0;
  int pos = start, d = dir;
  for (int i = 1; i <= m; i++) {
    if (tc[pos] == 0) return -1;
    tc[pos]--;
    if (i < m) {
      if (d == 1 && pos == n)
        d = -1;
      else if (d == -1 && pos == 1)
        d = 1;
      long long delta = abs(a[pos] - a[pos + d]);
      res += delta;
      pos += d;
    }
  }
  return res;
}
bool update(long long &ans, long long tmp) {
  if (ans == -1) {
    ans = tmp;
    return true;
  } else {
    if (tmp != ans) return false;
    return true;
  }
}
long long solve() {
  memset(c, 0, sizeof(c));
  for (int i = 1; i <= m; i++) c[b[i]]++;
  long long ans = -1;
  bool f1 = false, f2 = false;
  for (int i = 3; i < n; i++)
    if (c[i] > c[i - 1]) {
      long long tmp = go(i, 1);
      if (tmp != -1) ans = tmp;
      f1 = true;
      break;
    }
  for (int i = n - 2; i > 1; i--)
    if (c[i] > c[i + 1]) {
      long long tmp = go(i, -1);
      if (tmp != -1) {
        if (!update(ans, tmp)) return -1;
      }
      f2 = true;
      break;
    }
  long long tmp;
  tmp = go(1, 1);
  if (tmp != -1) {
    if (!update(ans, tmp)) return -1;
  }
  tmp = go(2, 1);
  if (tmp != -1) {
    if (!update(ans, tmp)) return -1;
  }
  tmp = go(n, -1);
  if (tmp != -1) {
    if (!update(ans, tmp)) return -1;
  }
  tmp = go(n - 1, -1);
  if (tmp != -1) {
    if (!update(ans, tmp)) return -1;
  }
  if (n >= 4 && !f1 && !f2 && c[2] != 2) {
    long long x = a[3] - a[2];
    for (int i = 4; i < n; i++) {
      long long tmp = a[i] - a[i - 1];
      if (tmp != x) return -1;
    }
  }
  return ans;
}
int main() {
  read();
  long long ans = solve();
  printf("%I64d\n", ans);
  return 0;
}
