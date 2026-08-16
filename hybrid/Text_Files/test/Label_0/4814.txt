#include <bits/stdc++.h>
using namespace std;
const long long mod = 998244353;
long long n, m, r, k, xx[] = {1, -1, 0, 0}, yy[] = {0, 0, 1, -1}, stx, sty, num;
long long a[100005], b[100005];
long double ans;
map<pair<int, int>, int> mp;
priority_queue<pair<long long, pair<int, int> > > q;
long long giv(long long x, long long y) { return a[x] * b[y]; }
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n >> m >> r >> k;
  stx = (n + 1) / 2, sty = (m + 1) / 2;
  for (long long i = 1; i <= n; i++) {
    a[i] += a[i - 1];
    if (i + r - 1 <= n) {
      a[i]++;
      a[i + r]--;
    }
  }
  for (long long i = 1; i <= m; i++) {
    b[i] += b[i - 1];
    if (i + r - 1 <= m) {
      b[i]++;
      b[i + r]--;
    }
  }
  q.push({giv(stx, sty), {stx, sty}});
  while (q.size()) {
    pair<long long, pair<int, int> > p = q.top();
    q.pop();
    long long x = p.second.first, y = p.second.second;
    ans += p.first;
    num++;
    if (num == k) break;
    mp[{x, y}] = 1;
    for (int i = 0; i < 4; i++) {
      int nx = x + xx[i], ny = y + yy[i];
      if (nx <= 0 || n < nx || ny <= 0 || m < ny) continue;
      if (mp[{nx, ny}]) continue;
      mp[{nx, ny}] = 1;
      q.push({giv(nx, ny), {nx, ny}});
    }
  }
  long double x = (n - r + 1) * (m - r + 1);
  cout << fixed << setprecision(10) << ans / x;
}
