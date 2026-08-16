#include <bits/stdc++.h>
using namespace std;
void readi(int &x) {
  int v = 0, f = 1;
  char c = getchar();
  while (!isdigit(c) && c != '-') c = getchar();
  if (c == '-')
    f = -1;
  else
    v = v * 10 + c - '0';
  while (isdigit(c = getchar())) v = v * 10 + c - '0';
  x = v * f;
}
void readll(long long &x) {
  long long v = 0ll, f = 1ll;
  char c = getchar();
  while (!isdigit(c) && c != '-') c = getchar();
  if (c == '-')
    f = -1;
  else
    v = v * 10 + c - '0';
  while (isdigit(c = getchar())) v = v * 10 + c - '0';
  x = v * f;
}
void readc(char &x) {
  char c;
  while ((c = getchar()) == ' ')
    ;
  x = c;
}
void writes(string s) { puts(s.c_str()); }
void writeln() { writes(""); }
void writei(int x) {
  if (!x) putchar('0');
  char a[25];
  int top = 0;
  while (x) {
    a[++top] = (x % 10) + '0';
    x /= 10;
  }
  while (top) {
    putchar(a[top]);
    top--;
  }
}
void writell(long long x) {
  if (!x) putchar('0');
  char a[25];
  int top = 0;
  while (x) {
    a[++top] = (x % 10) + '0';
    x /= 10;
  }
  while (top) {
    putchar(a[top]);
    top--;
  }
}
inline long long inc(int &x) { return ++x; }
inline long long inc(long long &x) { return ++x; }
inline long long inc(int &x, long long y) { return x += y; }
inline long long inc(long long &x, long long y) { return x += y; }
inline double inc(double &x, double y) { return x += y; }
inline long long dec(int &x) { return --x; }
inline long long dec(long long &x) { return --x; }
inline long long dec(int &x, long long y) { return x -= y; }
inline long long dec(long long &x, long long y) { return x -= y; }
inline double dec(double &x, double y) { return x -= y; }
inline long long mul(int &x) { return x = ((long long)x) * x; }
inline long long mul(long long &x) { return x = x * x; }
inline long long mul(int &x, long long y) { return x *= y; }
inline long long mul(long long &x, long long y) { return x *= y; }
inline double mul(double &x, double y) { return x *= y; }
inline long long divi(int &x) {
  long long ans, l, r, mid;
  ans = 0;
  l = 0;
  r = 0x3fffffff;
  while (l < r) {
    mid = (l + r) / 2;
    if (mid * mid < x) {
      ans = mid;
      l = mid + 1;
    } else
      r = mid;
  }
  return ans;
}
inline long long divi(long long &x) {
  long long ans, l, r, mid;
  ans = 0;
  l = 0;
  r = 0x3fffffff;
  while (l < r) {
    mid = (l + r) / 2;
    if (mid * mid < x) {
      ans = mid;
      l = mid + 1;
    } else
      r = mid;
  }
  return ans;
}
inline long long divi(int &x, long long y) { return x /= y; }
inline long long divi(long long &x, long long y) { return x /= y; }
inline double divi(double &x, double y) { return x /= y; }
inline long long mod(int &x, long long y) { return x %= y; }
inline long long mod(long long &x, long long y) { return x %= y; }
long long n, m, i, j, dp[205][205], px[205], py[205], s, p = 1e9 + 7;
long long mul(long long x, long long y, long long xx, long long yy) {
  return (x * yy - y * xx);
}
long long dfs(long long x, long long y) {
  if (dp[x][y] != -1) return dp[x][y];
  if (y - x <= 1) return 1;
  long long i;
  dp[x][y] = 0;
  if ((x + 1) <= (y - 1))
    for ((i) = (x + 1); (i) <= (y - 1); (i)++) {
      if (mul(px[i] - px[x], py[i] - py[x], px[y] - px[x], py[y] - py[x]) > 0) {
        (dp[x][y] += dfs(x, i) * dfs(i, y)) %= p;
      }
    }
  return dp[x][y];
}
int main() {
  ios_base::sync_with_stdio(false);
  ;
  cin >> n;
  if ((1) <= ((n)))
    for (((i)) = (1); ((i)) <= ((n)); ((i))++) cin >> px[i] >> py[i];
  if ((2) <= (n - 1))
    for ((i) = (2); (i) <= (n - 1); (i)++)
      s += mul(px[i] - px[1], py[i] - py[1], px[i + 1] - px[1],
               py[i + 1] - py[1]);
  if (s < 0) {
    reverse(px + 1, px + n + 1);
    reverse(py + 1, py + n + 1);
  }
  memset(dp, -1, sizeof(dp));
  cout << dfs(1, n);
  return 0;
}
