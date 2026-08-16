#include <bits/stdc++.h>
using namespace std;
const int N = 10;
int n, k;
struct Node {
  int mx[N], mn[N], siz;
  bool operator<(const Node &a) const {
    for (int i = 0; i < k; ++i)
      if (mx[i] > a.mn[i]) return 0;
    return 1;
  }
} t;
set<Node> s;
set<Node>::iterator it;
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    t.siz = 1;
    for (int j = 0; j < k; ++j) scanf("%d", &t.mx[j]), t.mn[j] = t.mx[j];
    while ((it = s.find(t)) != s.end()) {
      t.siz += it->siz;
      for (int j = 0; j < k; ++j)
        t.mx[j] = max(t.mx[j], it->mx[j]), t.mn[j] = min(t.mn[j], it->mn[j]);
      s.erase(it);
    }
    s.insert(t);
    printf("%d\n", (--s.end())->siz);
  }
  return 0;
}
