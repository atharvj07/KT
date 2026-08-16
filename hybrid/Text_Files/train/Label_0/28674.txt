#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
const int mod = 1e9 + 7;
int n;
long long ax[1010], ay[1010], bx[1010], by[1010];
long long ans = 0;
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
int calc(int id) {
  int A = abs(ax[id] - bx[id]);
  int B = abs(ay[id] - by[id]);
  return gcd(A, B) + 1;
}
struct Point {
  long long x, y;
  Point() {}
  Point(long long x, long long y) : x(x), y(y) {}
};
map<pair<long long, long long>, int> mp;
int sign(long long x) {
  if (x > 0) return 1;
  if (x == 0) return 0;
  return -1;
}
int mult(Point a, Point b, Point c) {
  return sign((a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y));
}
void solve(int i, int j) {
  if (max(ax[i], bx[i]) < min(ax[j], bx[j])) return;
  if (max(ax[j], bx[j]) < min(ax[i], bx[i])) return;
  if (max(ay[i], by[i]) < min(ay[j], by[j])) return;
  if (max(ay[j], by[j]) < min(ay[i], by[i])) return;
  Point aa(ax[i], ay[i]);
  Point bb(bx[i], by[i]);
  Point cc(ax[j], ay[j]);
  Point dd(bx[j], by[j]);
  if (mult(cc, bb, aa) * mult(bb, dd, aa) < 0) return;
  if (mult(aa, dd, cc) * mult(dd, bb, cc) < 0) return;
  long long a0 = ay[i] - by[i];
  long long b0 = bx[i] - ax[i];
  long long c0 = ax[i] * by[i] - bx[i] * ay[i];
  long long a1 = ay[j] - by[j];
  long long b1 = bx[j] - ax[j];
  long long c1 = ax[j] * by[j] - bx[j] * ay[j];
  long long D = a0 * b1 - a1 * b0;
  long long x = b0 * c1 - b1 * c0;
  long long y = a1 * c0 - a0 * c1;
  if (x % D != 0 || y % D != 0) return;
  x /= D, y /= D;
  ++mp[{x, y}];
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) {
    scanf("%lld%lld%lld%lld", &ax[i], &ay[i], &bx[i], &by[i]);
    if (ax[i] > bx[i]) {
      swap(ax[i], bx[i]);
      swap(ay[i], by[i]);
    }
    ans += calc(i);
  }
  for (int i = 1; i <= n; ++i)
    for (int j = i + 1; j <= n; ++j) solve(i, j);
  long long cnt[1000010];
  for (long long i = 1; i * (i - 1) / 2 <= 1000000; ++i)
    cnt[i * (i - 1) / 2] = i;
  for (auto &u : mp) ans -= cnt[u.second] - 1;
  printf("%lld\n", ans);
  return 0;
}
