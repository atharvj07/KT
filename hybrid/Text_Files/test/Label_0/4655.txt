#include <bits/stdc++.h>
using namespace std;
namespace std {
template <class S, class T>
struct hash<pair<S, T>> {
  size_t operator()(const pair<S, T> &p) const {
    return ((size_t)1e9 + 7) * hash<S>()(p.first) + hash<T>()(p.second);
  }
};
template <class T>
struct hash<vector<T>> {
  size_t operator()(const vector<T> &v) const {
    size_t h = 0;
    for (auto i : v) h = h * ((size_t)1e9 + 7) + hash<T>()(i) + 1;
    return h;
  }
};
}  // namespace std
template <class T>
ostream &operator<<(ostream &os, const vector<T> &v) {
  os << "[ ";
  for (int i = 0; i < (int)v.size(); i++)
    os << v[i] << (i == v.size() - 1 ? " ]" : ", ");
  return os;
}
template <class T>
ostream &operator<<(ostream &os, const set<T> &v) {
  os << "{ ";
  for (const auto &i : v) os << i << ", ";
  return os << "}";
}
template <class T, class U>
ostream &operator<<(ostream &os, const map<T, U> &v) {
  os << "{";
  for (const auto &i : v) os << " " << i.first << ": " << i.second << ",";
  return os << "}";
}
template <class T, class U>
ostream &operator<<(ostream &os, const pair<T, U> &p) {
  return os << "(" << p.first << ", " << p.second << ")";
}
void dbgprint(const string &fmt) { cerr << endl; }
template <class H, class... T>
void dbgprint(const string &fmt, const H &h, const T &...r) {
  cerr << fmt.substr(0, fmt.find(",")) << "= " << h << " ";
  dbgprint(fmt.substr(fmt.find(",") + 1), r...);
}
const int inf = (int)1e9;
const double INF = 1e12, EPS = 1e-9;
int n, m, q;
vector<pair<pair<int, int>, pair<int, int>>> e;
int p[2000];
inline int root(int x) { return x == p[x] ? x : (p[x] = root(p[x])); }
int main() {
  scanf("%d%d%d", &n, &m, &q);
  for (int i = 0; i < (int)m; i++) {
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    a--;
    b--;
    e.emplace_back(make_pair(c, i), make_pair(a, b));
  }
  sort((e).begin(), (e).end());
  while (q--) {
    int l, r;
    scanf("%d%d", &l, &r);
    l--;
    int ans = -1;
    for (int i = 0; i < (int)2 * n; i++) p[i] = i;
    for (int i = (int)e.size() - 1; i >= 0; i--)
      if (l <= e[i].first.second && e[i].first.second < r) {
        int a = e[i].second.first, b = e[i].second.second;
        int a0 = root(a * 2), b1 = root(b * 2 + 1);
        if (a0 == b1) continue;
        p[b1] = a0;
        int b0 = root(b * 2), a1 = root(a * 2 + 1);
        p[b0] = a1;
        if (root(a * 2) == root(b * 2)) {
          ans = e[i].first.first;
          break;
        }
      }
    printf("%d\n", ans);
  }
  return 0;
}
