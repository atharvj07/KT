#include <bits/stdc++.h>
using namespace std;
template <class T>
T Bitcnt(T a) {
  int sum = 0;
  while (a) {
    if (a & 1) sum++;
    a /= 2;
  }
  return sum;
}
template <class T>
T Max3(T a, T b, T c) {
  return max(a, max(b, c));
}
template <class T>
T Lcm(T a, T b) {
  T tmp = __gcd(a, b);
  return (a / tmp) * b;
}
template <class T>
T Pow(T a, T b) {
  T ans = 1;
  T base = a;
  while (b) {
    if (b & 1) ans = (ans * base);
    base = (base * base);
    b /= 2;
  }
  return ans;
}
long long Bigmod(long long a, long long b) {
  long long res = 1;
  long long pw = a % 1000000007LL;
  while (b > 0) {
    if (b & 1) res = (res * pw) % 1000000007LL;
    pw = (pw * pw) % 1000000007LL;
    b /= 2;
  }
  return res;
}
int a_x[] = {1, -1, 0, 0};
int a_y[] = {0, 0, 1, -1};
long long X, Y;
void extend_euclid(long long a, long long b) {
  if (b == 0) {
    X = 1;
    Y = 0;
    return;
  }
  extend_euclid(b, a % b);
  long long x, y;
  x = Y;
  y = X - (a / b) * Y;
  X = x;
  Y = y;
}
long long inverse_modulo(long long a, long long b) {
  extend_euclid(a, b);
  return (X + 1000000007LL) % 1000000007LL;
}
int mn[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
string s, t;
int n, m;
int f[30000007];
int dp[30000007];
int solve(int x, int y) {
  if (x == m) {
    if (y == n) return 1;
    return 0;
  }
  int idx = (x * (n + 1) + y);
  int &res = dp[idx];
  if (res != -1) return res;
  res = 0;
  if (y == 0) {
    return res = solve(x + 1, y + (s[x] == t[y] || s[x] == '?'));
  } else {
    res = solve(x, f[y]);
    if (y == n)
      res += 1;
    else if (s[x] == t[y] || s[x] == '?') {
      res = max(res, solve(x + 1, y + 1));
    }
  }
  return res;
}
int main() {
  cin >> s >> t;
  m = s.size();
  n = t.size();
  f[0] = -1;
  int i = 0;
  int j = -1;
  while (i < n) {
    while (j >= 0 && t[j] != t[i]) {
      j = f[j];
    }
    f[++i] = ++j;
  }
  memset(dp, -1, sizeof dp);
  cout << solve(0, 0);
  return 0;
}
