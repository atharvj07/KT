#include <bits/stdc++.h>
using namespace std;
namespace ufs {
int fa[400005];
int w[400005];
void makeset(int n) {
  for (int i = 1; i <= n; i++) fa[i] = i;
}
int findset(int x) {
  if (fa[x] == x) return x;
  int t = findset(fa[x]);
  w[x] ^= w[fa[x]];
  return fa[x] = t;
}
void merge(int u, int v, int ty) {
  swap(u, v);
  int a = findset(u);
  int b = findset(v);
  fa[a] = b;
  w[a] = w[u] ^ ty ^ w[v];
  w[b] = 0;
}
}  // namespace ufs
using namespace ufs;
int ty;
int n, cnt;
int lans;
map<int, int> hashh;
int opt, l, r, x;
void divide(int val, int *a) {
  for (int i = 0; i <= 30; i++) a[i] = 0;
  int len = 0;
  while (val) {
    a[len++] = (val & 1);
    val >>= 1;
  }
  len--;
}
int main() {
  ios::sync_with_stdio(false);
  cin >> n;
  makeset(2 * n);
  for (int i = 1; i <= n; i++) {
    cin >> opt >> l >> r;
    l ^= lans;
    r ^= lans;
    if (l > r) swap(l, r);
    l--;
    if (hashh.count(l) == 0) hashh[l] = ++cnt;
    if (hashh.count(r) == 0) hashh[r] = ++cnt;
    l = hashh[l];
    r = hashh[r];
    if (opt == 1) {
      cin >> x;
      x ^= lans;
      if (findset(l) != findset(r)) merge(l, r, x);
    } else {
      lans = 0;
      if (findset(l) != findset(r)) {
        lans = 1;
        cout << "-1\n";
      } else {
        lans = (w[l] ^ w[r]);
        cout << lans << '\n';
      }
    }
  }
  return 0;
}
