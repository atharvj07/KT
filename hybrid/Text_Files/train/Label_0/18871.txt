#include <bits/stdc++.h>
using namespace std;
template <typename T>
struct outputer;
struct outputable {};
template <typename T>
inline auto sqr(T x) -> decltype(x * x) {
  return x * x;
}
template <typename T1, typename T2>
inline bool umx(T1& a, T2 b) {
  if (a < b) {
    a = b;
    return 1;
  }
  return 0;
}
template <typename T1, typename T2>
inline bool umn(T1& a, T2 b) {
  if (b < a) {
    a = b;
    return 1;
  }
  return 0;
}
const int N = 200000;
const int64_t mod = 1000000007;
struct Input {
  int n;
  int64_t a[N];
  bool read() {
    if (!(cin >> n)) {
      return 0;
    }
    for (int i = int(0); i < int(n); ++i) {
      scanf("%" SCNd64, &a[i]);
    }
    return 1;
  }
  void init(const Input& input) { *this = input; }
};
struct Data : Input {
  int64_t ans;
  void write() { cout << ans << endl; }
};
namespace Main {
struct Solution : Data {
  int64_t f[N + 1];
  int64_t rf[N + 1];
  int64_t c(int x, int y) { return f[x + y] * rf[x] % mod * rf[y] % mod; }
  int64_t pw(int64_t val, int64_t k) {
    int64_t res = 1;
    while (k) {
      if (k & 1) {
        res = res * val % mod;
      }
      val = val * val % mod;
      k >>= 1;
    }
    return res;
  }
  int sgn;
  void iteration() {
    ;
    --n;
    for (int i = int(0); i < int(n); ++i) {
      a[i] = (a[i] + sgn * a[i + 1] + mod) % mod;
      sgn *= -1;
    }
  }
  int64_t calc(int t) {
    int m = (n + 1 - t) / 2;
    int64_t res = 0;
    for (int i = int(0); i < int(m); ++i) {
      ;
      res = (res + a[t + 2 * i] * c(i, m - 1 - i)) % mod;
    };
    return res;
  }
  void solve() {
    f[0] = 1;
    for (int i = int(0); i < int(n); ++i) {
      f[i + 1] = f[i] * (i + 1) % mod;
    }
    for (int i = int(0); i < int(n + 1); ++i) {
      rf[i] = pw(f[i], mod - 2);
    }
    if (n == 1) {
      ans = a[0];
      return;
    }
    sgn = 1;
    if (n & 1) {
      iteration();
    };
    ;
    int64_t val0 = calc(0);
    int64_t val1 = calc(1);
    if (n / 2 % 2 == 0) {
      sgn *= -1;
    }
    ans = (val0 + sgn * val1 + mod) % mod;
  }
  void clear() { *this = Solution(); }
};
}  // namespace Main
Main::Solution sol;
int main() {
  cout.setf(ios::showpoint | ios::fixed);
  cout.precision(20);
  sol.read();
  sol.solve();
  sol.write();
  return 0;
}
