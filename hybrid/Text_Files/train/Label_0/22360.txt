#include <bits/stdc++.h>
namespace FastIO {
bool IOerror = 0;
inline char nc() {
  static char buf[100000], *p1 = buf + 100000, *pend = buf + 100000;
  if (p1 == pend) {
    p1 = buf;
    pend = buf + fread(buf, 1, 100000, stdin);
    if (pend == p1) {
      IOerror = 1;
      return -1;
    }
  }
  return *p1++;
}
inline bool blank(char ch) {
  return ch == ' ' || ch == '\n' || ch == '\r' || ch == '\t';
}
template <class T>
inline bool read(T& x) {
  bool sign = 0;
  char ch = nc();
  x = 0;
  for (; blank(ch); ch = nc())
    ;
  if (IOerror) return false;
  if (ch == '-') sign = 1, ch = nc();
  for (; ch >= '0' && ch <= '9'; ch = nc()) x = x * 10 + ch - '0';
  if (sign) x = -x;
  return true;
}
template <class T, class... U>
bool read(T& h, U&... t) {
  return read(h) && read(t...);
}
};  // namespace FastIO
using namespace std;
using namespace FastIO;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const long long INF = 0x3f3f3f3f;
long long L[22], R[22], cnt[22];
bool check(long long pos, long long lim, long long rim) {
  if (pos == 0) return true;
  if (!lim && !rim) return true;
  long long down = lim ? L[pos] : 0;
  long long up = rim ? R[pos] : 9;
  for (long long i = down; i <= up; i++) {
    if (cnt[i]) {
      cnt[i]--;
      bool ok = check(pos - 1, lim && i == down, rim && i == up);
      cnt[i]++;
      if (ok) return true;
    }
  }
  return false;
}
long long len, ans;
void dfs(long long num, long long sum) {
  if (num == 9) {
    cnt[9] = sum;
    if (check(len, 1, 1)) ans++;
    return;
  }
  for (long long i = 0; i <= sum; i++) {
    cnt[num] = i;
    dfs(num + 1, sum - i);
  }
}
void solve(long long l, long long r) {
  len = 0;
  while (l) {
    L[++len] = l % 10;
    l /= 10;
  }
  len = 0;
  while (r) {
    R[++len] = r % 10;
    r /= 10;
  }
  dfs(0, len);
}
signed main() {
  long long l, r;
  cin >> l >> r;
  solve(l, r);
  cout << ans << endl;
  return 0;
}
