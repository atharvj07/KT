#include <bits/stdc++.h>
using namespace std;
template <class T>
inline void umax(T &a, T b) {
  if (a < b) a = b;
}
template <class T>
inline void umin(T &a, T b) {
  if (a > b) a = b;
}
template <class T>
inline T abs(T a) {
  return a > 0 ? a : -a;
}
template <class T>
inline T gcd(T a, T b) {
  return __gcd(a, b);
}
template <class T>
inline T lcm(T a, T b) {
  return a / gcd(a, b) * b;
}
const int inf = 1e9 + 143;
const long long longinf = 1e18 + 143;
inline int read() {
  int x;
  scanf(" %d", &x);
  return x;
}
const int N = 101010;
const int BLOCK = 200;
const int K = N / BLOCK + 10;
struct data {
  int a, b, id;
};
data a[N];
int opt[N];
long long pay[N];
bool bya(const data &a, const data &b) { return a.a > b.a; }
bool byb(const data &a, const data &b) { return a.b < b.b; }
struct line {
  long long m, n;
  line(long long _m = 0, long long _n = 0) {
    m = _m;
    n = _n;
  }
  long long calc(long long x) { return x * m + n; }
  bool operator<(const line &a) const {
    if (m == a.m) return n > a.n;
    return m < a.m;
  }
};
double cross(line L1, line L2) { return (double)(L1.n - L2.n) / (L2.m - L1.m); }
inline bool bad(line L1, line L2, line L3) {
  return cross(L1, L3) < cross(L1, L2);
}
class convex {
 public:
  line st[BLOCK + 5];
  int push, ptr;
  void clear() {
    push = 0;
    ptr = 1;
  }
  void add_line(line L) {
    while (push >= 2 && bad(st[push - 1], st[push], L)) push--;
    st[++push] = L;
  }
  pair<long long, int> get(int x) {
    if (push == 0) return make_pair(0ll, 0);
    if (ptr > push) ptr = push;
    while (ptr < push && st[ptr].calc(x) < st[ptr + 1].calc(x)) ++ptr;
    return make_pair(st[ptr].calc(x), st[ptr].m);
  }
};
class solver {
 public:
  convex cht;
  vector<int> vs;
  int add;
  solver() {
    add = 0;
    cht.clear();
    vs.clear();
  }
  void insert(int x) {
    vector<line> ls;
    cht.clear();
    vs.push_back(x);
    sort(vs.rbegin(), vs.rend());
    for (int i = 0; i < vs.size(); i++) {
      ls.push_back(line(vs[i], (long long)vs[i] * (i + 1)));
    }
    sort(ls.begin(), ls.end());
    for (int i = 0; i < ls.size(); i++) {
      if (i == 0 || ls[i - 1].m != ls[i].m) cht.add_line(ls[i]);
    }
  }
  pair<long long, int> getmax() {
    if (!vs.size()) return make_pair(-1, -1);
    return cht.get(add);
  }
};
solver T[K];
int main() {
  int n = read();
  int w = read();
  int maxb = 0;
  for (int i = 0; i < n; i++) {
    a[i].a = read();
    a[i].b = read();
    umax(maxb, a[i].b);
  }
  sort(a, a + n, bya);
  for (int i = 0; i < n; i++) {
    a[i].id = i;
  }
  sort(a, a + n, byb);
  printf("0 0\n");
  int ptr = 0;
  for (int c = 1; c <= maxb + 1; c++) {
    while (ptr < n && a[ptr].b < c) {
      T[a[ptr].id / BLOCK].insert(a[ptr].a);
      for (int i = a[ptr].id / BLOCK + 1; i < K; i++) ++T[i].add;
      ptr++;
    }
    pair<long long, int> res;
    res = make_pair(0, 0);
    for (int i = 0; i < K; i++) umax(res, T[i].getmax());
    printf("%I64d %d\n", res.first + 1ll * c * w * (n - ptr), res.second);
  }
  return 0;
}
