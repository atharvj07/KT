#include <bits/stdc++.h>
using namespace std;
const int maxn = 209;
struct node {
  int l, r;
  node() {}
  node(int l, int r) : l(l), r(r) {}
  bool operator<(const node& R) const { return l < R.l; }
};
set<node> S;
set<node>::iterator it;
int main() {
  S.insert(node(1, 2e9));
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    int l, len, r;
    scanf("%d%d", &l, &len);
    r = l + len - 1;
    int have = 0;
    for (it = S.begin(); it != S.end(); it++) {
      int L = (*it).l, R = (*it).r;
      if (L <= l && R >= r) {
        S.erase(it);
        printf("%d %d\n", l, r);
        if (l != L) {
          S.insert(node(L, l - 1));
        }
        if (r != R) {
          S.insert(node(r + 1, R));
        }
        have = 1;
        break;
      }
    }
    if (have) continue;
    for (it = S.begin(); it != S.end(); it++) {
      int L = (*it).l, R = (*it).r;
      if (R - L + 1 >= len) {
        l = L, r = L + len - 1;
        S.erase(it);
        printf("%d %d\n", l, r);
        if (l != L) {
          S.insert(node(L, l - 1));
        }
        if (r != R) {
          S.insert(node(r + 1, R));
        }
        break;
      }
    }
  }
}
