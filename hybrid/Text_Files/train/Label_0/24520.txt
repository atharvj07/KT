#include <bits/stdc++.h>
using namespace std;
constexpr int64_t MOD = (int64_t)1e9 + 7LL;
struct quad {
  int64_t x1, y1;
  int64_t x2, y2;
  bool contains(const quad& other) {
    return (x1 <= other.x1 && other.x2 <= x2) ||
           (y1 <= other.y1 && other.y2 <= y2);
  }
  bool intersects(const quad& other) {
    return !(x2 < other.x1 || x1 > other.x2 || y2 < other.y1 || y1 > other.y2);
  }
};
int64_t contribute(int64_t L, int64_t R, int64_t k, int64_t n) {
  if (k < L) return 0;
  int64_t A = L + min(k, R);
  int64_t B = min(k, R) - L + 1;
  if (A % 2LL)
    B /= 2LL;
  else
    A /= 2LL;
  A %= MOD;
  B %= MOD;
  return (((A * B) % MOD) * n) % MOD;
}
int64_t dfs(quad space, int64_t L, int64_t R, quad target, int64_t k) {
  if (!target.intersects(space)) {
    return 0;
  }
  if (target.contains(space)) {
    int64_t n = min(min(target.x2, space.x2) - max(target.x1, space.x1) + 1,
                    min(target.y2, space.y2) - max(target.y1, space.y1) + 1);
    return contribute(L, R, k, n % MOD);
  }
  int64_t ans = 0;
  int64_t M = (L + R) / 2LL;
  int64_t m = (R - L) / 2LL;
  for (int i = 0; i < 2; ++i) {
    for (int j = 0; j < 2; ++j) {
      quad next_space;
      next_space.x1 = space.x1 + (i ? m + 1 : 0);
      next_space.x2 = (i ? space.x2 : space.x1 + m);
      next_space.y1 = space.y1 + (j ? m + 1 : 0);
      next_space.y2 = (j ? space.y2 : space.y1 + m);
      if (i ^ j) {
        ans += dfs(next_space, M + 1, R, target, k);
        ans %= MOD;
      } else {
        ans += dfs(next_space, L, M, target, k);
        ans %= MOD;
      }
    }
  }
  return ans;
}
void solve(int x1, int x2, int y1, int y2, int64_t k) {
  int64_t L = 1;
  int64_t R = 1LL << 31;
  quad space;
  space.x1 = space.y1 = L;
  space.x2 = space.y2 = R;
  quad target;
  target.x1 = x1;
  target.x2 = x2;
  target.y1 = y1;
  target.y2 = y2;
  cout << dfs(space, L, R, target, k) << endl;
}
int main() {
  int q;
  scanf("%d", &q);
  for (int i = 0; i < q; ++i) {
    int64_t x1, x2, y1, y2, k;
    cin >> x1 >> y1 >> x2 >> y2 >> k;
    solve(x1, x2, y1, y2, k);
  }
  return 0;
}
