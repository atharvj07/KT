#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
struct f {
  int l, r, index;
} a[N];
int main() {
  int t;
  cin >> t;
  while (t--) {
    memset(a, 0, sizeof(a));
    int c[N];
    int n, k = 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
      cin >> a[i].l >> a[i].r;
      k = max(k, a[i].r);
      a[i].index = i;
    }
    queue<f> b;
    int j = 1;
    for (int i = 1; i <= k; i++) {
      while (a[j].l == i) {
        b.push(a[j]);
        j++;
      }
      if (!b.empty()) {
        auto w = b.front();
        c[w.index] = i;
        b.pop();
      }
      if (!b.empty()) {
        auto w = b.front();
        while (w.r <= i) {
          c[w.index] = 0;
          b.pop();
          if (b.empty()) break;
          w = b.front();
        }
      }
    }
    for (int i = 1; i <= n; i++) {
      cout << c[i] << ' ';
    }
    puts("");
  }
}
