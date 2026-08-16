#include <bits/stdc++.h>
using namespace std;
struct __io_dev {
  __io_dev(const bool& __fastio = false) {
    if (__fastio) ios_base::sync_with_stdio(false), cin.tie(nullptr);
    srand(time(nullptr));
    if (!string("").empty())
      freopen(
          ""
          ".in",
          "r", stdin),
          freopen(
              ""
              ".out",
              "w", stdout);
  }
  ~__io_dev() { fprintf(stderr, "%.6f ms\n", 1e3 * clock() / CLOCKS_PER_SEC); }
} __io(false);
const long long inf = (long long)1e+9 + 7ll;
const long long linf = (long long)1e+18 + 7ll;
const long double eps = (long double)1e-9;
const long double pi = acosl((long double)-1.0);
const int alph = 26;
const int sqr = 3017;
static char buff[(int)2e6 + 17];
long long __p[3] = {29ll, 31ll, 33ll};
long long __mod[3] = {inf, inf + 2ll, 14881337ll};
const int maxn = (int)3e6 + 17;
int n;
long long a, b;
long long A[maxn], dp[maxn][3];
set<long long> D;
void add(long long x) {
  for (long long i = 2; i * i <= x; ++i)
    for (; x % i == 0; x /= i, D.insert(i))
      ;
  if (x != 1) D.insert(x);
}
long long solve(long long d) {
  dp[0][0] = 0, dp[0][1] = dp[0][2] = linf;
  for (long long i = (long long)1; i < (long long)n + 1; ++i) {
    if (A[i] % d == 0) {
      dp[i][0] = dp[i - 1][0];
      dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a;
      dp[i][2] = min(dp[i - 1][1], dp[i - 1][2]);
    }
    if ((A[i] + 1) % d == 0 || (A[i] - 1) % d == 0) {
      dp[i][0] = dp[i - 1][0] + b;
      dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a;
      dp[i][2] = min(linf, min(dp[i - 1][1], dp[i - 1][2]) + b);
    }
    if (A[i] % d != 0 && (A[i] + 1) % d != 0 && (A[i] - 1) % d != 0) {
      dp[i][0] = linf;
      dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a;
      dp[i][2] = linf;
    }
  }
  return min(dp[n][0], min(dp[n][1], dp[n][2]));
}
int main() {
  scanf("%d %lld %lld", &n, &a, &b);
  for (long long i = 0ll; i < (long long)n; ++i) scanf("%lld", A + i + 1);
  add(A[1] - 1), add(A[1]), add(A[1] + 1);
  add(A[n] - 1), add(A[n]), add(A[n] + 1);
  long long ans = linf;
  for (auto i : D) ans = min(ans, solve(i));
  printf("%lld\n", ans);
  return 0;
}
