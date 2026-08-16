#include <bits/stdc++.h>
using namespace std;
inline long long rd() {
  long long _x = 0;
  int _ch = getchar(), _f = 1;
  for (; !isdigit(_ch) && (_ch != '-') && (_ch != EOF); _ch = getchar())
    ;
  if (_ch == '-') {
    _f = 0;
    _ch = getchar();
  }
  for (; isdigit(_ch); _ch = getchar()) _x = _x * 10 + _ch - '0';
  return _f ? _x : -_x;
}
void write(long long _x) {
  if (_x >= 10)
    write(_x / 10), putchar(_x % 10 + '0');
  else
    putchar(_x + '0');
}
inline void wrt(long long _x, char _p) {
  if (_x < 0) putchar('-'), _x = -_x;
  write(_x);
  if (_p) putchar(_p);
}
struct matrix {
  int a[1 << 7 | 5][1 << 7 | 5], len;
  matrix operator*(const matrix &B) const {
    matrix ans;
    memset(ans.a, 0, sizeof ans.a);
    for (int i = int(0); i <= (int)(len); i++) {
      for (int j = int(0); j <= (int)(len); j++) {
        for (int k = int(0); k <= (int)(len); k++) {
          ans.a[i][j] = (ans.a[i][j] + 1ll * a[i][k] * B.a[k][j]) % 1000000007;
        }
      }
    }
    ans.len = len;
    return ans;
  }
};
int calc(int A, int B, int n) {
  int dp[8][2];
  memset(dp, 0, sizeof dp);
  dp[0][1] = 1;
  for (int i = int(1); i <= (int)(n); i++) {
    if ((A & (1 << (i - 1))) == 0 && (B & (1 << (i - 1))) == 0) {
      dp[i][1] = dp[i - 1][0];
      dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 1000000007;
    } else {
      dp[i][1] = dp[i - 1][0] + dp[i - 1][1];
      dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
    }
  }
  return dp[n][1];
}
int a[8];
int dp[1 << 7 | 5], tmp[1 << 7 | 5];
matrix qpow(matrix X, int k) {
  matrix ans;
  memset(ans.a, 0, sizeof ans.a);
  ans.len = X.len;
  for (int i = int(0); i <= (int)(X.len); i++) {
    ans.a[i][i] = 1;
  }
  for (; k; k >>= 1, X = X * X)
    if (k & 1) ans = ans * X;
  return ans;
}
int main() {
  for (int i = int(1); i <= (int)(7); i++) a[i] = rd();
  int la = 0;
  dp[0] = 1;
  for (int i = int(1); i <= (int)(7); i++)
    if (a[i]) {
      memset(tmp, 0, sizeof tmp);
      matrix now;
      memset(now.a, 0, sizeof now.a);
      for (int A = int(0); A <= (int)((1 << i) - 1); A++) {
        for (int B = int(0); B <= (int)((1 << i) - 1); B++) {
          now.a[A][B] = calc(A, B, i);
        }
      }
      now.len = (1 << i) - 1;
      now = qpow(now, a[i]);
      for (int j = int(0); j <= (int)((1 << i) - 1); j++) {
        for (int k = int(0); k <= (int)((1 << i) - 1); k++) {
          tmp[j] = (tmp[j] + 1ll * dp[k] * now.a[k][j]) % 1000000007;
        }
      }
      memcpy(dp, tmp, sizeof dp);
      la = i;
    }
  wrt(dp[0], '\n');
}
