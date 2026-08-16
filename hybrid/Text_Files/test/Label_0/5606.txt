#include <bits/stdc++.h>
namespace io {
int F() {
  int F = 1, n = 0;
  char ch;
  while ((ch = getchar()) != '-' && (ch < '0' || ch > '9'))
    ;
  ch == '-' ? F = 0 : n = ch - '0';
  while ((ch = getchar()) >= '0' && ch <= '9') n = n * 10 + ch - '0';
  return F ? n : -n;
}
long long G() {
  long long F = 1, n = 0;
  char ch;
  while ((ch = getchar()) != '-' && (ch < '0' || ch > '9'))
    ;
  ch == '-' ? F = 0 : n = ch - '0';
  while ((ch = getchar()) >= '0' && ch <= '9') n = n * 10 + ch - '0';
  return F ? n : -n;
}
}  // namespace io
int R(int l, int r) { return (rand() << 15 | rand()) % (r - l + 1) + l; }
int main() {
  long long n = io::G(), l = io::G() - 1, r = io::G() - 1, k = io::G();
  long long B = l <= r ? r - l + 1 : n - (l - r - 1), S = n - B;
  long long ans = -1;
  int fl = 1;
start:;
  if ((k - B) / n <= 22000000) {
    int u = (k - B) / n;
    for (register int x = 0; x <= u; ++x) {
      long long re = k - B - x * n;
      if (x == 0) {
        if (re <= B && re >= 0)
          if (fl || re) (ans < (S + re) ? ans = (S + re), 1 : 0);
      } else {
        long long B1 = re % x, S1 = re / x - B1;
        if (B1 > B || S1 < 0) continue;
        if (S1 <= S) {
          if (fl || B1) (ans < (B1 + S1) ? ans = (B1 + S1), 1 : 0);
        } else {
          long long T = S1 - S;
          long long ex = (T + x) / (x + 1);
          B1 += ex * x;
          S1 -= ex * (x + 1);
          if (S1 >= 0 && B1 <= B)
            if (fl || B1) (ans < (B1 + S1) ? ans = (B1 + S1), 1 : 0);
        }
      }
    }
  } else {
    for (register long long S1 = 0; S1 <= S; ++S1)
      for (register long long B1 = 0; B1 <= B; ++B1) {
        long long y = k - B1 - B;
        long long a = S1 + B1 + n;
        if (y == 0 && a == 0 || a && y % a == 0 && y / a >= 0)
          if (fl || B1) (ans < (S1 + B1) ? ans = (S1 + B1), 1 : 0);
      }
  }
  if (fl) {
    k = k + 1;
    fl = 0;
    goto start;
  }
  printf("%lld\n", ans);
  return 0;
}
