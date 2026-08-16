#include <bits/stdc++.h>
using namespace std;
template <typename Tp>
inline void read(Tp &x) {
  static char c;
  static bool neg;
  x = 0, c = getchar(), neg = false;
  for (; !isdigit(c); c = getchar()) {
    if (c == '-') {
      neg = true;
    }
  }
  for (; isdigit(c); c = getchar()) {
    x = x * 10 + c - '0';
  }
  if (neg) {
    x = -x;
  }
}
const int N = 3e5 + 5;
const int B = 19;
int n, a;
int d[N];
long long c[N];
namespace RMQ {
int log2[N];
long long bz[B][N];
inline void init() {
  log2[1] = 0;
  for (int i = 2; i < N; ++i) {
    log2[i] = log2[i >> 1] + 1;
  }
  memcpy(bz[0] + 1, c + 1, sizeof(long long) * n);
  for (int i = 1; i < B; ++i) {
    for (int j = 0; j + (1 << (i - 1)) < N; ++j) {
      bz[i][j] = std::min(bz[i - 1][j], bz[i - 1][j + (1 << (i - 1))]);
    }
  }
}
inline long long query(int l, int r) {
  int lg = log2[r - l + 1];
  l = std::max(l - 1, 0);
  r = std::min(r - 1, n);
  return std::min(bz[lg][l], bz[lg][r - (1 << lg) + 1]);
}
}  // namespace RMQ
int main() {
  read(n), read(a);
  for (int i = 1; i <= n; ++i) {
    read(d[i]), read(c[i]);
    c[i] = a - c[i];
  }
  long long ans = std::max(0LL, *max_element(c + 1, c + n + 1));
  for (int i = 1; i <= n; ++i) {
    c[i] += c[i - 1];
  }
  RMQ::init();
  stack<tuple<long long, int, long long>> sk;
  multiset<long long> st;
  for (int r = 2, l; r <= n; ++r) {
    long long cur = (long long)(d[r] - d[r - 1]) * (d[r] - d[r - 1]);
    while (!sk.empty() && get<0>(sk.top()) <= cur) {
      st.erase(st.find(get<2>(sk.top())));
      sk.pop();
    }
    l = sk.empty() ? 0 : get<1>(sk.top());
    sk.emplace(cur, r, RMQ::query(l, r) + cur);
    st.emplace(get<2>(sk.top()));
    ans = std::max(ans, c[r] - *st.begin());
  }
  printf("%lld\n", ans);
  return 0;
}
