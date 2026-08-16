#include <bits/stdc++.h>
using namespace std;
class Solution {
 public:
  Solution(int n, int p, const string& s, vector<vector<int> > const& a)
      : _n(n), _p(p), _s(s), _a(a), _b(1 << p, 0), _t(1 << p, 0) {}
  int solve() {
    for (int a = 0; a < _p; ++a) {
      for (int b = 0; b < _p; ++b) {
        if (_a[a][b]) continue;
        f(a, b);
      }
    }
    vector<int> c(_p, 0);
    for (char si : _s) ++c[si - 'a'];
    int fz = 1 << _p, r = 0;
    vector<int> f(fz, -1);
    f[0] = 0;
    for (int x = 0; x < fz; ++x) {
      if (_b[x]) continue;
      for (int a = 0; a < _p; ++a) {
        if (!(x & (1 << a))) continue;
        if (f[x ^ (1 << a)] < 0) continue;
        f[x] = max(f[x], c[a] + f[x ^ (1 << a)]);
        r = max(r, f[x]);
      }
    }
    return _n - r;
  }

 private:
  void f(int a, int b) {
    int tz = 1 << _p;
    for (int i = 0; i < tz; ++i) _t[i] = 0;
    for (int i = 0, x = 0, ta = 0, tb = 0; i < _n; ++i) {
      int c = _s[i] - 'a';
      if (c == b && tb < ta) {
        tb = ta;
        f(x & ~(1 << a) & ~(1 << b), a, b);
      }
      if (c == a) {
        ++ta;
        x = 0;
      }
      x |= 1 << c;
    }
    for (int x = 0; x < tz; ++x) {
      _b[x] = _b[x] | _t[x];
    }
    _t.clear();
  }
  void f(int x, int a, int b) {
    if (_t[x]) return;
    _t[x] = 1;
    for (int k = 0; k < _p; ++k) {
      if (k == a || k == b || (x & (1 << k))) continue;
      f(x ^ (1 << k), a, b);
    }
  }

 private:
  int _n, _p;
  string const& _s;
  vector<vector<int> > const& _a;
  vector<bool> _b, _t;
};
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n, p;
  string s;
  cin >> n >> p >> s;
  vector<vector<int> > a;
  for (int i = 0; i < p; ++i) {
    a.emplace_back(p);
    for (int& ai : a.back()) cin >> ai;
  }
  cout << Solution(n, p, s, a).solve() << endl;
  return 0;
}
