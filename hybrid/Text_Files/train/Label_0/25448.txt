#include <bits/stdc++.h>
using namespace std;
template <class T>
void _R(T &x) {
  cin >> x;
}
void _R(int &x) { scanf("%d", &x); }
void _R(long long &x) { scanf("%lld", &x); }
void _R(double &x) { scanf("%lf", &x); }
void _R(char &x) { scanf(" %c", &x); }
void _R(char *x) { scanf("%s", x); }
void R() {}
template <class T, class... U>
void R(T &head, U &...tail) {
  _R(head);
  R(tail...);
}
template <class T>
void _W(const T &x) {
  cout << x;
}
void _W(const int &x) { printf("%d", x); }
void _W(const long long &x) { printf("%lld", x); }
void _W(const double &x) { printf("%.16f", x); }
void _W(const char &x) { putchar(x); }
void _W(const char *x) { printf("%s", x); }
template <class T, class U>
void _W(const pair<T, U> &x) {
  _W(x.first);
  putchar(' ');
  _W(x.second);
}
template <class T>
void _W(const vector<T> &x) {
  for (auto i = x.begin(); i != x.end(); _W(*i++))
    if (i != x.cbegin()) putchar(' ');
}
void W() {}
template <class T, class... U>
void W(const T &head, const U &...tail) {
  _W(head);
  putchar(sizeof...(tail) ? ' ' : '\n');
  W(tail...);
}
int MOD = 1e9 + 7;
void ADD(long long &x, long long v) {
  x = (x + v) % MOD;
  if (x < 0) x += MOD;
}
const int SIZE = 1e6 + 10;
long long mypow(long long x, long long y) {
  long long res = 1;
  while (y) {
    if (y & 1) res = res * x % MOD;
    y >>= 1;
    x = x * x % MOD;
  }
  return res;
}
long long fac[SIZE], inv[SIZE];
long long C(int x, int y) {
  if (y < 0 || y > x) return 0;
  long long res = 1;
  for (int i = (1); i <= (y); ++i) res = res * (x + 1 - i) % MOD;
  return res * inv[y] % MOD;
}
int N, K, M;
long long cnt[15][100];
long long dp0[15][60][16];
long long dp[15][15][100];
void pre() {
  fac[0] = 1;
  for (int i = (1); i < (15); ++i) fac[i] = fac[i - 1] * i % MOD;
  inv[14] = mypow(fac[14], MOD - 2);
  for (int i = 13; i >= 0; i--) inv[i] = inv[i + 1] * (i + 1) % MOD;
  dp0[1][1][1] = 1;
  int mask = (1 << M) - 1;
  for (int i = (1); i < (K); ++i)
    for (int j = (1); j <= ((i - 1) * M + 1); ++j)
      for (int k = 1; k <= mask; k += 2) {
        for (int dd = (1); dd <= (M); ++dd) {
          int nxt_k = (k << (dd - 1)) & mask;
          ADD(dp0[i + 1][j + dd][((nxt_k << 1) | 1) & mask],
              dp0[i][j][k] * (__builtin_popcount(nxt_k) + 1));
        }
      }
  for (int i = (1); i <= (K); ++i)
    for (int j = (1); j <= ((i - 1) * M + 1); ++j)
      for (int k = 1; k <= mask; k += 2) {
        ADD(cnt[i][j], dp0[i][j][k]);
      }
}
int main() {
  R(N, K, M);
  pre();
  dp[0][0][0] = 1;
  for (int i = 0; i < (K); ++i) {
    for (int j = 0; j < (K); ++j) {
      for (int k = 0; k < (100); ++k) {
        if (!dp[i][j][k]) continue;
        for (int use_num = 1; use_num + j <= K; use_num++) {
          for (int dd = (1); dd <= ((use_num - 1) * M + 1); ++dd) {
            if (!i) {
              ADD(dp[i + 1][j + use_num][k + dd],
                  dp[i][j][k] * cnt[use_num][dd]);
            } else {
              ADD(dp[i + 1][j + use_num][k + dd + M],
                  dp[i][j][k] * cnt[use_num][dd]);
            }
          }
        }
      }
    }
  }
  long long an = 0;
  for (int i = (1); i <= (K); ++i) {
    for (int k = 0; k < (100); ++k) {
      if (!dp[i][K][k]) continue;
      if (k > N) continue;
      ADD(an, dp[i][K][k] * C(N - k + i, i));
    }
  }
  W(an);
  return 0;
}
