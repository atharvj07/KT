#include <bits/stdc++.h>
using namespace std;
const int P = 1000000007;
int p, A;
int a[3500], cnt;
char s[1010];
void init_() {
  static int num[1010];
  int l = strlen(s);
  for (int i = 0; i <= l - 1; i++) num[i] = s[l - i - 1] - '0';
  for (;;) {
    bool zero = 1;
    for (int i = 0; i <= l - 1; i++)
      if (num[i]) zero = 0;
    if (zero) break;
    unsigned long long rest = 0;
    for (int i = l - 1; i >= 0; i--) {
      rest = rest * 10 + num[i];
      num[i] = rest / p;
      rest = rest % p;
    }
    a[++cnt] = rest;
  }
}
unsigned long long calc(unsigned long long l, unsigned long long r) {
  return (l + r) * (r - l + 1) / 2 % P;
}
unsigned long long f[2][3500][2];
unsigned long long g[2][3500][2];
void solve() {
  int cur = 0;
  f[cur][0][0] = 1;
  g[cur][0][0] = 1;
  for (int i = 1; i <= cnt; i++) {
    cur ^= 1;
    f[cur][0][0] =
        (f[cur ^ 1][0][0] * calc(0, p) + f[cur ^ 1][0][1] * calc(0, p - 1)) % P;
    g[cur][0][0] =
        (f[cur ^ 1][0][0] * calc(0, a[i]) + g[cur ^ 1][0][0] * (a[i] + 1) +
         f[cur ^ 1][0][1] * calc(0, a[i] - 1) + g[cur ^ 1][0][1] * a[i]) %
        P;
    for (int j = 1; j <= A; j++) {
      f[cur][j][0] =
          (f[cur ^ 1][j][0] * calc(0, p) + f[cur ^ 1][j][1] * calc(0, p - 1)) %
          P;
      g[cur][j][0] =
          (f[cur ^ 1][j][0] * calc(0, a[i]) + g[cur ^ 1][j][0] * (a[i] + 1) +
           f[cur ^ 1][j][1] * calc(0, a[i] - 1) + g[cur ^ 1][j][1] * a[i]) %
          P;
      f[cur][j][1] = (f[cur ^ 1][j - 1][0] * calc(0, p - 1) +
                      f[cur ^ 1][j - 1][1] * calc(0, p)) %
                     P;
      g[cur][j][1] = (f[cur ^ 1][j - 1][0] * calc(p - a[i], p - 1) +
                      g[cur ^ 1][j - 1][0] * (p - a[i] - 1) +
                      f[cur ^ 1][j - 1][1] * calc(p - a[i] + 1, p) +
                      g[cur ^ 1][j - 1][1] * (p - a[i])) %
                     P;
    }
    (f[cur][A][1] +=
     f[cur ^ 1][A][0] * calc(0, p - 1) + f[cur ^ 1][A][1] * calc(0, p)) %= P;
    (g[cur][A][1] += f[cur ^ 1][A][0] * calc(p - a[i], p - 1) +
                     g[cur ^ 1][A][0] * (p - a[i] - 1) +
                     f[cur ^ 1][A][1] * calc(p - a[i] + 1, p) +
                     g[cur ^ 1][A][1] * (p - a[i])) %= P;
  }
  cout << g[cur][A][0] << endl;
}
int main() {
  cin >> p >> A;
  if (A > 3450) {
    puts("0");
    return 0;
  }
  scanf("%s", s);
  init_();
  solve();
  return 0;
}
