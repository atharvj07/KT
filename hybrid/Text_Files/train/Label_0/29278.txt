#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("no-stack-protector")
#pragma GCC target("sse,sse2,ssse3,sse3,sse4,popcnt,avx,mmx,abm,tune=native")
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
const long long MN = 1e5 + 5, MM = 61;
long long n, i, j, x, fl;
vector<long long> arr[MM], ans, tmp;
int main() {
  srand(time(0));
  for (scanf("%lld", &n), i = 1; i <= n; i++) {
    scanf("%lld", &x);
    for (j = MM - 1; j >= 0; j--) {
      if ((1LL << j) & x) {
        arr[j].push_back(x);
        break;
      }
    }
  }
  for (j = MM - 1; j >= 0; j--) {
    long long xr = 0;
    tmp.clear();
    i = 0;
    for (auto v : arr[j]) {
      if ((xr ^ v) <= xr) {
        while ((xr ^ v) <= xr && i < ans.size())
          xr ^= ans[i], tmp.push_back(ans[i++]);
        if ((xr ^ v) <= xr) {
          fl = 1;
          break;
        }
      }
      tmp.push_back(v);
      xr ^= v;
    }
    for (; i < ans.size(); i++) tmp.push_back(ans[i]);
    swap(ans, tmp);
  }
  if (fl)
    printf("No\n");
  else {
    printf("Yes\n");
    for (auto v : ans) printf("%lld ", v);
    printf("\n");
  }
  return 0;
}
