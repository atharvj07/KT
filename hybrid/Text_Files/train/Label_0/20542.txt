#include <bits/stdc++.h>
#pragma warning(disable : 4996)
using namespace std;
int IT_MAX = 1 << 17;
const long long MOD = 1000000007;
const int INF = 1034567890;
const long long LL_INF = 1234567890123456789ll;
const double PI = acos(-1);
const long double ERR = 1E-10;
long long par[6];
long long M[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
inline long long leapYearCount(long long x) {
  return x / 4 - x / 100 + x / 400;
}
long long countDays(long long x) {
  long long t = (x - 1970) * 365 + leapYearCount(x - 1) - leapYearCount(1969);
  return t;
}
bool isLeap(long long y) {
  return (y % 4 == 0 && y % 100 != 0) || y % 400 == 0;
}
long long whichDay(long long y, long long m, long long d) {
  long long u = countDays(y);
  if (isLeap(y))
    M[2] = 29;
  else
    M[2] = 28;
  for (long long i = 1; i < m; i++) u += M[i];
  u += d - 1;
  return (u + 3) % 7 + 1;
}
long long* ch(long long X) {
  long long* RV = new long long[6];
  long long st = 1971, en = INF, mi, rv = 1970;
  while (st <= en) {
    mi = (st + en) / 2;
    if (countDays(mi) * 86400 <= X) {
      rv = mi;
      st = mi + 1;
    } else
      en = mi - 1;
  }
  RV[5] = rv;
  X -= countDays(rv) * 86400;
  if (isLeap(RV[5]))
    M[2] = 29;
  else
    M[2] = 28;
  long long n = X / 86400;
  for (RV[4] = 1; RV[4] <= 12; RV[4]++) {
    if (n < M[RV[4]]) {
      RV[3] = n + 1;
      break;
    }
    n -= M[RV[4]];
  }
  long long t = X % 86400;
  RV[2] = t / 3600;
  RV[1] = (t % 3600) / 60;
  RV[0] = t % 60;
  return RV;
}
long long rch(long long* u) {
  long long rv = 0;
  rv += countDays(u[5]) * 86400;
  if (isLeap(u[5]))
    M[2] = 29;
  else
    M[2] = 28;
  long long i;
  for (i = 1; i < u[4]; i++) rv += M[i] * 86400;
  rv += (u[3] - 1) * 86400;
  rv += u[2] * 3600;
  rv += u[1] * 60;
  rv += u[0];
  return rv;
}
bool isValid(long long* u) {
  if (u[0] != -1 && par[0] != -1 && u[0] != par[0]) return false;
  if (u[1] != -1 && par[1] != -1 && u[1] != par[1]) return false;
  if (u[2] != -1 && par[2] != -1 && u[2] != par[2]) return false;
  if (u[4] != -1 && par[5] != -1 && u[4] != par[5]) return false;
  if (!isLeap(u[5]) && par[5] == 2 && par[4] == 29 && par[3] == -1)
    return false;
  if (isLeap(u[5]))
    M[2] = 29;
  else
    M[2] = 28;
  if (u[4] == -1) return true;
  long long st, en;
  if (u[3] != -1)
    st = en = u[3];
  else
    st = 1, en = M[u[4]];
  for (long long i = st; i <= en; i++) {
    if (par[3] == -1 && par[4] == -1) return true;
    if (par[3] != -1) {
      if (whichDay(u[5], u[4], i) == par[3]) return true;
    }
    if (par[4] != -1) {
      if (par[4] == i) return true;
    }
  }
  return false;
}
int main() {
  for (int i = 0; i < 6; i++) scanf("%lld", &par[i]);
  int T;
  scanf("%d", &T);
  while (T--) {
    long long X, i, j;
    scanf("%lld", &X);
    long long* in = ch(X);
    long long* ans = new long long[6];
    for (i = 0; i < 6; i++) ans[i] = in[i];
    for (i = 0; i < 6; i++) {
      long long st, en;
      if (i == 0 || i == 1)
        st = in[i] + 1, en = 59;
      else if (i == 2)
        st = in[i] + 1, en = 23;
      else if (i == 3) {
        if (isLeap(ans[5]))
          M[2] = 29;
        else
          M[2] = 28;
        st = in[i] + 1, en = M[ans[4]];
      } else if (i == 4)
        st = in[i] + 1, en = 12;
      else if (i == 5)
        st = in[i] + 1, en = LL_INF;
      for (j = st; j <= en; j++) {
        ans[i] = j;
        if (isValid(ans)) break;
      }
      if (j <= en) break;
      ans[i] = -1;
    }
    for (i = i - 1; i >= 0; i--) {
      long long st = 0;
      if (i >= 3) st = 1;
      for (j = st;; j++) {
        ans[i] = j;
        if (isValid(ans)) break;
      }
    }
    printf("%lld\n", rch(ans));
  }
  return 0;
}
