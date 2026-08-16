#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int x = 0, f = 1;
  char c = getchar();
  while (c != '-' && (c < '0' || c > '9')) c = getchar();
  if (c == '-') f = -1, c = getchar();
  while (c >= '0' && c <= '9') x = x * 10 + c - '0', c = getchar();
  return f * x;
}
const int maxn = 2e5 + 10;
const int inf = 0x3f3f3f3f;
const int mod = 1e9 + 7;
const double eps = 1e-7;
int n;
int a[maxn], belong[maxn], c[maxn], f[maxn];
struct P {
  int a, id;
  bool operator<(const P &rhs) const { return a < rhs.a; }
} p[maxn];
int pre[maxn];
int main() {
  n = read();
  for (int i = 1; i <= n; ++i) {
    a[i] = read();
    p[i].a = a[i];
    p[i].id = i;
  }
  sort(a + 1, a + 1 + n);
  sort(p + 1, p + 1 + n);
  int sum = 0;
  for (int i = 2; i <= n; ++i) sum += c[i] = a[i] - a[i - 1];
  for (int i = 1; i <= n; ++i) f[i] = 0;
  f[1] = f[2] = f[3] = -inf;
  int mx = 0, xx = 0, pp = 0, last = 0;
  for (int i = 4; i <= n - 2; ++i) {
    if (f[i - 3] > mx) mx = f[i - 3], pp = i - 3;
    f[i] = mx + c[i];
    pre[i] = pp;
    if (f[i] > xx) xx = f[i], last = i;
  }
  vector<int> pos;
  while (last) pos.push_back(last), last = pre[last];
  sort(pos.begin(), pos.end());
  pos.push_back(n + 1);
  printf("%d %d\n", sum - xx, int(pos.size()));
  int tpos = 1;
  for (int i = 0; i < pos.size(); ++i) {
    while (tpos < pos[i]) belong[p[tpos].id] = i + 1, tpos++;
  }
  for (int i = 1; i <= n; ++i) printf("%d%c", belong[i], " \n"[i == n]);
}
