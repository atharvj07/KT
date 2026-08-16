#include <bits/stdc++.h>
using namespace std;
template <int POS, class TUPLE>
void deploy(std::ostream &os, const TUPLE &tuple) {}
template <int POS, class TUPLE, class H, class... Ts>
void deploy(std::ostream &os, const TUPLE &t) {
  os << (POS == 0 ? "" : ", ") << get<POS>(t);
  deploy<POS + 1, TUPLE, Ts...>(os, t);
}
template <class T, class U>
std::ostream &operator<<(std::ostream &os, std::pair<T, U> &p) {
  os << "(" << p.first << ", " << p.second << ")";
  return os;
}
template <class T>
std::ostream &operator<<(std::ostream &os, std::vector<T> &v) {
  int remain = v.size();
  os << "{";
  for (auto e : v) os << e << (--remain == 0 ? "}" : ", ");
  return os;
}
template <class T>
std::ostream &operator<<(std::ostream &os, std::set<T> &v) {
  int remain = v.size();
  os << "{";
  for (auto e : v) os << e << (--remain == 0 ? "}" : ", ");
  return os;
}
template <class T, class K>
std::ostream &operator<<(std::ostream &os, std::map<T, K> &make_pair) {
  int remain = make_pair.size();
  os << "{";
  for (auto e : make_pair)
    os << "(" << e.first << " -> " << e.second << ")"
       << (--remain == 0 ? "}" : ", ");
  return os;
}
using ll = long long;
pair<int, int> memo[2 * 1000100];
inline int getint() {
  int now = 0, s = 1;
  char d = ' ';
  while (d != '-' && (d < '0' || d > '9')) d = getchar();
  if (d == '-')
    s = -1;
  else
    now = d - '0';
  while (d = getchar(), d >= '0' && d <= '9') now = now * 10 + d - '0';
  return now * s;
}
int main() {
  int N = getint();
  int K = getint();
  {
    int x;
    for (int i = 0; i < (N); i++) {
      int l = getint(), r = getint();
      memo[x++] = make_pair(l, false);
      memo[x++] = make_pair(r, true);
    }
  }
  sort(memo, memo + 2 * N);
  int cnt = 0;
  vector<pair<int, int> > ans;
  int start = 0, end = 0;
  for (int i = 0; i < 2 * N; i++) {
    auto &t = memo[i];
    if (t.second) {
      if (cnt == K) {
        end = t.first;
        ans.push_back(make_pair(start, end));
      }
      cnt -= 1;
    } else {
      if (cnt == K - 1) {
        start = t.first;
      }
      cnt += 1;
    }
  }
  printf("%d\n", ((int)(ans).size()));
  for (auto &t : ans) {
    printf("%d %d\n", t.first, t.second);
  }
  return 0;
}
