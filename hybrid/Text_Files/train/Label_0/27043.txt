#include <bits/stdc++.h>
using namespace std;
namespace ib {
char b[100];
}
inline void pi(int x) {
  if (x == 0) {
    putchar(48);
    return;
  }
  if (x < 0) {
    putchar('-');
    x = -x;
  }
  char *s = ib::b;
  while (x) *(++s) = x % 10, x /= 10;
  while (s != ib::b) putchar((*(s--)) + 48);
}
inline void ri(int &x) {
  x = 0;
  static char c;
  bool t(0);
  while (c = getchar(), c < '0' || c > '9')
    if (c == '-')
      t = 1;
    else
      t = 0;
  do x = x * 10 + c - '0';
  while (c = getchar(), c >= '0' && c <= '9');
  if (t) x = -x;
}
int main() {
  int i, n, m, k;
  long long s, l = 1, r = ~0u >> 2, x, y, mid;
  cin >> n >> m >> k;
  while (l + 1 < r) {
    mid = (l + r) >> 1;
    x = mid - k + 1;
    y = mid - (n - k);
    if (x < 1 && y < 1)
      s = (long long)mid * mid + n - mid - mid + 1;
    else if (x < 1)
      s = (long long)(mid - 1 + y) * (n - k) / 2 + (1 + mid) * mid / 2 + k -
          mid;
    else if (y < 1)
      s = (long long)(x + mid) * k / 2 + (long long)mid * (mid - 1) / 2 + n -
          (k + mid - 1);
    else
      s = (long long)(x + mid) * k / 2 + (long long)(mid - 1 + y) * (n - k) / 2;
    if (s > m)
      r = mid;
    else
      l = mid;
  }
  cout << l;
  return 0;
}
