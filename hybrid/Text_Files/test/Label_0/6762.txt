#include <bits/stdc++.h>
using namespace std;
pair<int, long long> ans;
long long m;
inline void get_ready() { cin >> m; }
inline long long getmax(long long x) {
  if (x == 1) return 1;
  long long l = 1, r = 100007, maxx = 1;
  while (l <= r) {
    long long mid = (long long)(l + r) >> 1;
    if (mid * mid * mid <= x)
      maxx = mid, l = mid + 1;
    else
      r = mid - 1;
  }
  return maxx;
}
inline long long getpow(long long x) { return x * x * x; }
inline void dfs(long long m, int num, long long now) {
  if (m == 0) {
    ans = max(ans, make_pair(num, now));
    return;
  }
  long long x = getmax(m);
  dfs(m - getpow(x), num + 1, now + getpow(x));
  if (x >= 1) dfs(getpow(x) - getpow(x - 1) - 1, num + 1, now + getpow(x - 1));
}
inline void slove() {
  dfs(m, 0, 0);
  cout << ans.first << " " << ans.second << endl;
}
int main() {
  get_ready();
  slove();
  return 0;
}
