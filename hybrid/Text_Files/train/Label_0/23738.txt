#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
long long seg[5][10][N << 2];
int tp[5][10], n;
void update(int val, int v, int p = 1, int l = 1, int r = n) {
  if (l == r) {
    for (int j = 0; j < 5; j++)
      for (int i = 0; i < 2 + j * 2; i++) seg[j][i][p] = 1LL * val * tp[j][i];
    return;
  }
  int m = l + r >> 1;
  if (v <= m)
    update(val, v, p << 1, l, m);
  else
    update(val, v, p << 1 | 1, m + 1, r);
  for (int i = 0; i < 5; i++) {
    int md = 2 + i * 2;
    for (int j = 0; j < md; j++) {
      int len = m - l + 1;
      int nxt = (j + len) % md;
      seg[i][j][p] = seg[i][j][p << 1] + seg[i][nxt][p << 1 | 1];
    }
  }
}
int mod, len, z;
long long query(int L, int R, int p = 1, int l = 1, int r = n) {
  if (L <= l && R >= r) {
    long long ans = seg[z][len % mod][p];
    len += r - l + 1;
    return ans;
  }
  int m = l + r >> 1;
  long long ans = 0;
  if (L <= m) ans += query(L, R, p << 1, l, m);
  if (R > m) ans += query(L, R, p << 1 | 1, m + 1, r);
  return ans;
}
inline int cal(int z, int i) {
  int v = i % (2 * (z - 1));
  if (v == 0) return 2;
  if (v <= z) return v;
  if (v > z) return 2 * z - v;
}
int main() {
  static int num[N];
  for (int i = 2; i <= 6; i++) {
    for (int j = 0; j < i * 2 - 2; j++) {
      tp[i - 2][j] = cal(i, j + 1);
    }
  }
  cin >> n;
  for (int i = 1; i <= n; i++) {
    scanf("%d", &num[i]);
    update(num[i], i);
  }
  int m;
  cin >> m;
  while (m--) {
    int c, l, r;
    scanf("%d%d%d", &c, &l, &r);
    if (c == 1)
      update(r, l);
    else {
      scanf("%d", &c);
      z = c - 2;
      len = 0;
      mod = 2 * c - 2;
      cout << query(l, r) << endl;
      ;
    }
  }
}
