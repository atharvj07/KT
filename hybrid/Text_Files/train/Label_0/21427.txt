#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline void Int(T &n) {
  n = 0;
  int f = 1;
  register int ch = getchar();
  for (; !isdigit(ch); ch = getchar())
    if (ch == '-') f = -1;
  for (; isdigit(ch); ch = getchar()) n = (n << 3) + (n << 1) + ch - '0';
  n = n * f;
}
template <typename T>
T gcd(T a, T b) {
  return !b ? a : gcd(b, a % b);
}
template <typename T>
inline void umin(T &a, T b) {
  a = a < b ? a : b;
}
template <typename T>
inline void umax(T &a, T b) {
  a = a > b ? a : b;
}
template <typename T, typename W>
inline void Int(T &x, W &y) {
  Int(x), Int(y);
}
template <typename T, typename W, typename Q>
inline void Int(T &x, W &y, Q &z) {
  Int(x, y), Int(z);
}
const int N = 1e5 + 7;
const int inf = 1e9 + 7;
int n;
string num;
long long dp[23][4][5];
long long call(int i, bool isSmall, int cnt) {
  if (cnt > 3) return 0;
  if (i >= n) return cnt and cnt <= 3;
  long long &ret = dp[i][isSmall][cnt];
  if (~ret) return ret;
  ret = 0;
  int d = isSmall ? 9 : num[i] - '0';
  for (int j = 0; j <= d; ++j) {
    ret += call(i + 1, isSmall or (j < num[i] - '0'), cnt + (j > 0));
  }
  return ret;
}
void toString(long long n) {
  num = "";
  while (n) {
    num += n % 10 + '0';
    n /= 10;
  }
  reverse(num.begin(), num.end());
}
long long calc(long long x) {
  if (x == 0) return 0;
  toString(x);
  n = (int)num.size();
  memset(dp, -1, sizeof dp);
  return call(0, 0, 0);
}
int solve() {
  long long l, r;
  Int(l, r);
  printf("%lld\n", calc(r) - calc(l - 1));
  return 0;
}
int main() {
  int tests = 1, CaseNo = 0;
  Int(tests);
  while (tests--) {
    solve();
  }
  return 0;
}
