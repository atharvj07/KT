#include <bits/stdc++.h>
using namespace std;
void read(long long &x) {
  x = 0;
  long long f = 1;
  char ch = getchar();
  for (; !isdigit(ch); ch = getchar())
    if (ch == '-') f = -f;
  for (; isdigit(ch); ch = getchar()) x = x * 10 + ch - '0';
  x *= f;
}
void print(long long x) {
  if (x < 0) putchar('-'), x = -x;
  if (!x) return;
  print(x / 10), putchar(x % 10 + 48);
}
void write(long long x) {
  if (!x)
    putchar('0');
  else
    print(x);
  putchar('\n');
}
const long long maxn = 1e6 + 10;
const long long inf = 1e9;
const double eps = 1e-8;
const long long mod = 1e9 + 7;
long long v[maxn], t[maxn], n, s, pps[maxn], _[2], pw[maxn];
signed main() {
  read(n);
  long long w = 0;
  pw[0] = 1;
  for (long long i = 1; i <= 100; i++) pw[i] = pw[i - 1] * 2;
  for (long long i = 1; i <= n; i++)
    read(v[i]), read(t[i]), w += v[i], pps[i] = t[i];
  for (long long r = 1; r < 62; r++) {
    long long sum = 0, p = 0;
    for (long long i = 1; i <= n; i++)
      if (pw[r - 1] <= t[i] && t[i] < pw[r]) {
        if (__builtin_popcountll(t[i]) & 1)
          sum -= v[i];
        else
          sum += v[i];
      }
    if ((sum < 0 && w > 0) || (sum > 0 && w < 0)) p = 1, s |= pw[r - 1];
    for (long long i = 1; i <= n; i++)
      if (!p)
        if (t[i] & (pw[r - 1])) t[i] ^= pw[r - 1];
  }
  write(s);
  return 0;
}
