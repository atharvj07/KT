#include <bits/stdc++.h>
using namespace std;
template <typename A>
inline std::istream& IN(A& a) {
  return std::cin >> a;
}
template <typename A, typename... Args>
inline std::istream& IN(A& a, Args&... rest) {
  std::cin >> a;
  return IN(rest...);
}
inline std::ostream& OUT() { return std::cout << std::endl; }
template <typename A>
inline std::ostream& _OUT(const A& a) {
  return std::cout << a;
}
template <typename A, typename... Args>
inline std::ostream& _OUT(const A& a, const Args&... rest) {
  std::cout << a << " ";
  return _OUT(rest...);
}
template <typename... Args>
inline std::ostream& OUT_(const Args&... args) {
  _OUT(args...);
  return std::cout << " ";
}
template <typename... Args>
inline std::ostream& OUT(const Args&... args) {
  _OUT(args...);
  return std::cout << std::endl;
}
template <typename T, typename U>
inline bool cmax(T& a, const U& b) {
  return b > a ? a = b, true : false;
}
template <typename T, typename U>
inline bool cmin(T& a, const U& b) {
  return b < a ? a = b, true : false;
}
const int _ = int(2e5 + 10);
long long n, N;
int a[_];
vector<int> v[_];
int rb[_];
long long ans[_];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  IN(n);
  for (long long i = (long long)(1); i < (long long)(n + 1); ++i) {
    IN(a[i]);
    cmax(N, a[i]);
    for (int d = 1; d * d <= a[i]; ++d)
      if (a[i] % d == 0) {
        v[d].push_back(i);
        int t = a[i] / d;
        if (d != t) v[t].push_back(i);
      }
    rb[i] = i;
  }
  ans[N] = n * (n + 1) / 2;
  for (long long i = (long long)(N)-1; i >= (long long)(1); --i) {
    ans[i] = ans[i + 1];
    if ((int((v[i + 1]).size())) <= 1) continue;
    int newrb = n + 1;
    for (long long j = (long long)(v[i + 1][1] + 1); j < (long long)(n + 1);
         ++j) {
      if (rb[j] >= newrb) break;
      ans[i] -= newrb - rb[j];
      rb[j] = newrb;
    }
    newrb = v[i + 1].back();
    for (long long j = (long long)(v[i + 1][0] + 1);
         j < (long long)(v[i + 1][1] + 1); ++j) {
      if (rb[j] >= newrb) break;
      ans[i] -= newrb - rb[j];
      rb[j] = newrb;
    }
    newrb = v[i + 1][(int((v[i + 1]).size())) - 2];
    for (long long j = (long long)(1); j < (long long)(v[i + 1][0] + 1); ++j) {
      if (rb[j] >= newrb) break;
      ans[i] -= newrb - rb[j];
      rb[j] = newrb;
    }
  }
  if (rb[1] <= n - 1) ++ans[0];
  if (rb[1] <= n) ++ans[0];
  if (rb[2] <= n) ++ans[0];
  long long ret = 0;
  for (long long i = (long long)(1); i < (long long)(N + 1); ++i) {
    ret += (ans[i] - ans[i - 1]) * i;
  }
  OUT(ret);
  return 0;
}
