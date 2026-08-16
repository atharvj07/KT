#include <bits/stdc++.h>
using namespace std;
int read() {
  int x = 0, f = 1;
  char ch = getchar();
  while (ch - '0' < 0 || ch - '0' > 9) {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch - '0' >= 0 && ch - '0' <= 9) {
    x = x * 10 + ch - '0';
    ch = getchar();
  }
  return x * f;
}
int n;
struct P {
  long long x, y;
} p[500011 * 2], sum[500011 * 2];
P operator+(P a, P b) {
  return (P){(a.x + b.x) % 1000000007, (a.y + b.y) % 1000000007};
}
P operator-(P a, P b) { return (P){a.x - b.x, a.y - b.y}; }
P operator*(P a, long long b) { return (P){a.x * b, a.y * b}; }
long long operator*(P a, P b) { return a.x * b.y - a.y * b.x; }
unsigned long long All;
long long s[500011 * 2], ss[500011 * 2];
int main() {
  n = read();
  for (int i = 1; i <= n; i++) p[i].x = read(), p[i].y = read();
  for (int i = 1; i <= n; i++) All += (p[i % n + 1] - p[0]) * (p[i] - p[0]);
  for (int i = n + 1; i <= 2 * n; i++) p[i] = p[i - n];
  for (int i = 1; i <= 2 * n; i++) s[i] = p[i] * p[i - 1] % 1000000007;
  for (int i = 1; i <= 2 * n; i++) s[i] = (s[i] + s[i - 1]) % 1000000007;
  for (int i = 1; i <= 2 * n; i++) ss[i] = (ss[i - 1] + s[i]) % 1000000007;
  for (int i = 1; i <= 2 * n; i++) sum[i] = sum[i - 1] + p[i];
  int R = 1;
  unsigned long long S = 0;
  long long ans = 0;
  for (int i = 1; i <= n; i++) {
    while (S + p[R] * p[i] + p[R + 1] * p[R] + p[i] * p[R + 1] <= All / 2) {
      S += p[R] * p[i] + p[R + 1] * p[R] + p[i] * p[R + 1];
      R++;
    }
    if (i != R) {
      long long s1 = ((ss[R] - ss[i] - 1ll * (R - i) * s[i] % 1000000007 +
                       p[i] * (sum[R] - sum[i]) % 1000000007) %
                          1000000007 +
                      1000000007) %
                     1000000007;
      ans = (ans + (All % 1000000007 * (R - i - 1) % 1000000007 -
                    2 * s1 % 1000000007 + 1000000007) %
                       1000000007) %
            1000000007;
      S += p[i] * p[i + 1] + p[i + 1] * p[R] + p[R] * p[i];
    }
  }
  cout << ans;
  return 0;
}
