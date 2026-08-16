#include <bits/stdc++.h>
using namespace std;
const int MAXN = 200010;
const int inf = 1e9;
int p[MAXN], t[MAXN];
int n, w, k, l = 0, r = 0, t0 = 0, ans = 0, s = 0;
multiset<int> a;
multiset<int> b;
multiset<int>::iterator iter;
long long int max(long long int a, long long int b) {
  if (a > b)
    return a;
  else
    return b;
}
void init() {
  scanf("%d %d %d", &n, &w, &k);
  for (int i = 0; i < n; i++) {
    scanf("%d", &p[i]);
  }
  for (int i = 0; i < n; i++) {
    scanf("%d", &t[i]);
  }
}
void solve() {
  while (r < n) {
    a.insert(t[r]);
    t0 += (t[r] + 1) / 2;
    if (a.size() > w) {
      b.insert(*(a.begin()));
      t0 += *(a.begin()) / 2;
      a.erase(a.begin());
    }
    s += p[r++];
    while (l <= r && t0 > k) {
      if (t[l] >= *(a.begin())) {
        a.erase(a.find(t[l]));
        t0 -= (t[l] + 1) / 2;
        if (b.size()) {
          iter = b.end();
          iter--;
          a.insert(*iter);
          t0 -= *iter / 2;
          b.erase(iter);
        }
      } else {
        b.erase(b.find(t[l]));
        t0 -= t[l];
      }
      s -= p[l++];
    }
    ans = max(ans, s);
  }
}
int main() {
  init();
  solve();
  printf("%d\n", ans);
  return 0;
}
