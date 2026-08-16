#include <bits/stdc++.h>
using namespace std;
class sp {
 public:
  int q;
  sp *w;
  sp(int e, sp *r) {
    q = e;
    w = r;
  }
};
int main() {
  int q, w, w1 = 0, e, r, t, y, u, a[5000], d[5000], f[5000];
  sp *s[5000], *c;
  cin >> q >> w;
  for (e = 0; e < q; e++) {
    a[e] = 500000000;
    f[e] = 0;
    s[e] = 0;
  }
  for (e = 0; e < w; e++) {
    cin >> r >> t >> y >> u;
    t--;
    if (r == 1)
      for (; t < y; t++) {
        a[t] += u;
        f[t] += u;
      }
    else {
      d[w1] = 0;
      for (; t < y; t++) {
        if (a[t] > u) {
          a[t] = u;
          for (c = s[t]; c; c = c->w) d[c->q]--;
          s[t] = new sp(w1, 0);
          d[w1]++;
        }
        if (a[t] == u) {
          s[t] = new sp(w1, s[t]);
          d[w1]++;
        }
      }
      w1++;
    }
  }
  for (w = 0; w < w1; w++)
    if (d[w] == 0) {
      cout << "NO";
      goto stop;
    }
  cout << "YES\n";
  for (w = 0; w < q; w++) cout << a[w] - f[w] << " ";
stop:
  return 0;
}
