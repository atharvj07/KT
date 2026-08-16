#include <bits/stdc++.h>
using namespace std;
constexpr long long int TEN(int n) { return (n == 0) ? 1 : 10 * TEN(n - 1); }
template <class T>
bool uin(T &a, T b) {
  return a > b ? (a = b, true) : false;
}
template <class T>
bool uax(T &a, T b) {
  return a < b ? (a = b, true) : false;
}
const int N = 3e5 + 5;
const int M = 1e9 + 7;
pair<int, int> p[N];
int n, w, v, u;
long double eps = 1e-8;
bool check(long double t, bool left) {
  long double m = (long double)u / v, sub = v * t, val;
  for (int i = 0; i < (int)(n); ++i) {
    val = p[i].second - m * (p[i].first - sub);
    if (left && val > eps) return false;
    if (!left && val < eps) return false;
  }
  return true;
}
int main() {
  cin >> n >> w >> v >> u;
  cout << fixed << setprecision(8);
  for (int i = 0; i < (int)(n); ++i) cin >> p[i].first >> p[i].second;
  if (check(0, true)) {
    cout << (double)w / u;
    return 0;
  }
  long double l = 0, r = 1e9 + 14, ans = 1e9 + 14;
  while (r - l > eps) {
    long double mid = (l + r) / 2;
    if (check(mid, false)) {
      ans = min(ans, mid);
      r = mid;
    } else
      l = mid;
  }
  cout << ans + (double)w / u;
}
