#include <bits/stdc++.h>
using namespace std;
struct itree {
  int L, R;
  itree *l = 0, *r = 0;
  int info = 0;
  itree(int L, int R) : L(L), R(R) {}
  itree() : L(0), R(INT_MAX) {}
  void update(int i) {
    info++;
    if (R > L + 1) {
      int M = (L + R) / 2;
      if (l == 0) l = new itree(L, M);
      if (r == 0) r = new itree(M, R);
      itree *t = (i < M) ? l : r;
      t->update(i);
    }
  }
  void dndate(int i) {
    info--;
    if (R > L + 1) {
      int M = (L + R) / 2;
      if (l == 0) l = new itree(L, M);
      if (r == 0) r = new itree(M, R);
      itree *t = (i < M) ? l : r;
      t->dndate(i);
    }
  }
  int count(int _L, int _R) {
    if ((L == _L && R == _R)) return info;
    int M = (L + R) / 2;
    int answ = 0;
    if (_L < M && l != 0) answ += l->count(_L, min(_R, M));
    if (_R > M && r != 0) answ += r->count(max(_L, M), _R);
    return answ;
  }
};
int main() {
  int n;
  scanf("%d", &n);
  const int inf = 1e9 + 100;
  unordered_map<int, itree *> a;
  for (int i = 0; i < n; i++) {
    int tp, x, t;
    scanf("%d %d %d", &tp, &t, &x);
    if (a.count(x) == 0) a[x] = new itree(0, inf);
    switch (tp) {
      case 1:
        a[x]->update(t);
        break;
      case 2:
        a[x]->dndate(t);
        break;
      case 3:
        printf("%d\n", a[x]->count(0, t + 1));
        break;
    }
  }
}
