#include <bits/stdc++.h>
using namespace std;
int read() {
  int w = 0, f = 1;
  char c = ' ';
  while (c < '0' || c > '9') c = getchar(), f = c == '-' ? -1 : f;
  while (c >= '0' && c <= '9') w = w * 10 + c - 48, c = getchar();
  return w * f;
}
struct node {
  int l, r;
  bool operator<(const node& o) const { return r < o.l; }
};
set<node> s;
int n;
signed main() {
  n = read();
  while (n--) {
    node x;
    x.l = read(), x.r = read();
    while (s.find(x) != s.end()) {
      node tmp = *s.find(x);
      x.l = min(x.l, tmp.l);
      x.r = max(x.r, tmp.r);
      s.erase(tmp);
    }
    s.insert(x);
    printf("%d%c", (int)s.size(), n ? ' ' : '\n');
  }
  return 0;
}
