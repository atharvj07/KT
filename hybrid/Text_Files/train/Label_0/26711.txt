#include <bits/stdc++.h>
using namespace std;
constexpr int inf = 0x3f3f3f3f;
class Solver {
 public:
  explicit Solver(vector<int>&& v)
      : n_(v.size()),
        v_(std::move(v)),
        gcd_(n_, vector<int>(n_ + 1, -1)),
        steps_(n_, vector<int>(n_ + 1, -1)) {}
  int solve() { return g(0, n_); }

 private:
  int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
  }
  int f(int i, int j) {
    if (i + 1 == j) return v_[i];
    int& ans = gcd_[i][j];
    if (ans != -1) return ans;
    return ans = gcd(v_[i], f(i + 1, j));
  }
  int g(int i, int j) {
    if (i + 1 == j) return v_[i] == 1 ? 0 : inf;
    int& ans = steps_[i][j];
    if (ans != -1) return ans;
    ans = inf;
    if (f(i + 1, j) == 1) {
      ans = min(ans, (v_[i] == 1 ? 0 : 1) + g(i + 1, j));
    }
    if (f(i, j - 1) == 1) {
      ans = min(ans, (v_[j - 1] == 1 ? 0 : 1) + g(i, j - 1));
    }
    if (f(i, j) == 1) {
      ans = min(ans, 2 * (j - i) - 2);
    }
    return ans;
  }
  int n_;
  vector<int> v_;
  vector<vector<int>> gcd_;
  vector<vector<int>> steps_;
};
int main() {
  int n;
  cin >> n;
  vector<int> v(n);
  for (int& e : v) cin >> e;
  Solver solver(std::move(v));
  int tmp = solver.solve();
  cout << (tmp == inf ? -1 : tmp) << endl;
  return 0;
}
