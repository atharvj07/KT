#include <bits/stdc++.h>
using namespace std;
namespace output {
void __(short x) { cout << x; }
void __(unsigned x) { cout << x; }
void __(int x) { cout << x; }
void __(long long x) { cout << x; }
void __(unsigned long long x) { cout << x; }
void __(double x) { cout << x; }
void __(long double x) { cout << x; }
void __(char x) { cout << x; }
void __(const char* x) { cout << x; }
void __(const string& x) { cout << x; }
void __(bool x) { cout << (x ? "true" : "false"); }
template <class S, class T>
void __(const pair<S, T>& x) {
  __(1 ? "(" : ""), __(x.first), __(1 ? ", " : " "), __(x.second),
      __(1 ? ")" : "");
}
template <class T>
void __(const vector<T>& x) {
  __(1 ? "{" : "");
  bool _ = 0;
  for (const auto& v : x) __(_ ? 1 ? ", " : " " : ""), __(v), _ = 1;
  __(1 ? "}" : "");
}
template <class T>
void __(const set<T>& x) {
  __(1 ? "{" : "");
  bool _ = 0;
  for (const auto& v : x) __(_ ? 1 ? ", " : " " : ""), __(v), _ = 1;
  __(1 ? "}" : "");
}
template <class T>
void __(const multiset<T>& x) {
  __(1 ? "{" : "");
  bool _ = 0;
  for (const auto& v : x) __(_ ? 1 ? ", " : " " : ""), __(v), _ = 1;
  __(1 ? "}" : "");
}
template <class S, class T>
void __(const map<S, T>& x) {
  __(1 ? "{" : "");
  bool _ = 0;
  for (const auto& v : x) __(_ ? 1 ? ", " : " " : ""), __(v), _ = 1;
  __(1 ? "}" : "");
}
void pr() { cout << "\n"; }
template <class S, class... T>
void pr(const S& a, const T&... b) {
  __(a);
  if (sizeof...(b)) __(' ');
  pr(b...);
}
}  // namespace output
using namespace output;
const int MN = 33;
int h, q, i, x, y;
string s;
map<int, int> sm, val;
int main() {
  scanf("%d%d", &h, &q);
  for (; q; q--) {
    cin >> s;
    if (s == "add") {
      scanf("%d%d", &x, &y);
      val[x] += y;
      while (x) {
        sm[x] += y;
        x >>= 1;
      }
    } else {
      x = 1;
      int mx = 0;
      double prob = 1, ans = 0;
      for (i = 0; i < h; i++) {
        int lsum = val[x] + sm[x << 1], rsum = val[x] + sm[(x << 1) | 1];
        if (lsum > rsum) {
          ans += prob / 2.0 * max(mx, lsum);
          mx = max(mx, rsum);
          x = (x << 1);
        } else {
          ans += prob / 2.0 * max(mx, rsum);
          mx = max(mx, lsum);
          x = (x << 1) | 1;
        }
        prob /= 2;
      }
      ans += prob * max(mx, val[x]);
      printf("%.6lf\n", ans);
    }
  }
  return 0;
}
