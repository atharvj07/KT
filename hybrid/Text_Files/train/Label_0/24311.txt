#include <bits/stdc++.h>
using namespace std;
int n, x, t, h, m, r[2], cv, cx;
struct K {
  int h, m;
  bool u;
  K(int H, int M) : h(H), m(M), u(0) {}
  bool operator<(const K &k) const { return h < k.h; }
};
vector<K> v[2];
int main() {
  scanf("%d%d", &n, &x);
  for (int i = 0; i < n; i++) {
    scanf("%d%d%d", &t, &h, &m);
    v[t].push_back(K(h, m));
  }
  cv = 0;
  cx = x;
  while (1) {
    int pp = -1;
    for (int i = 0; i < v[cv].size(); i++) {
      if (v[cv][i].u || v[cv][i].h > cx) continue;
      if (pp == -1 || v[cv][i].m > v[cv][pp].m) pp = i;
    }
    if (pp == -1) break;
    v[cv][pp].u = 1;
    r[0]++;
    cx += v[cv][pp].m;
    cv ^= 1;
  }
  for (int i = 0; i < v[0].size(); i++) v[0][i].u = 0;
  for (int i = 0; i < v[1].size(); i++) v[1][i].u = 0;
  cv = 1;
  cx = x;
  while (1) {
    int pp = -1;
    for (int i = 0; i < v[cv].size(); i++) {
      if (v[cv][i].u || v[cv][i].h > cx) continue;
      if (pp == -1 || v[cv][i].m > v[cv][pp].m) pp = i;
    }
    if (pp == -1) break;
    v[cv][pp].u = 1;
    r[1]++;
    cx += v[cv][pp].m;
    cv ^= 1;
  }
  printf("%d", max(r[0], r[1]));
}
