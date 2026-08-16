#include <bits/stdc++.h>
using namespace std;
template <class T>
int size(const T &a) {
  return int(a.size());
}
template <class T>
T sqr(const T &a) {
  return a * a;
}
struct Edge {
  int l, h, a;
  void scan() { scanf("%d %d %d", &l, &h, &a); }
} a[6][6];
map<int, int> dp[6];
int t[6];
int b[6];
int w[6] = {6, 11, 16, 21, 26, 1};
int mw[6];
int geth(int *t) {
  int h = 0;
  for (int i = 0; i < 6; i++) {
    h += t[i];
    h *= w[i];
  }
  return h;
}
void extr(int *b, int h) {
  for (int i = 5; i >= 1; i--) {
    b[i] = h % w[i - 1];
    h /= w[i - 1];
  }
  b[0] = h;
}
void gen(int *b, int i, int j, int s) {
  if (i == j) {
    t[0] = 6;
    int h = geth(t);
    dp[j][h] = max(dp[j][h], s);
    return;
  }
  for (int w = a[i][j].l; w <= a[i][j].h && w <= b[i]; w++) {
    t[i] = b[i] - w;
    t[j] += w;
    gen(b, i + 1, j, s + w * w + (w ? a[i][j].a : 0));
    t[j] -= w;
  }
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n * (n - 1) / 2; i++) {
    int v1, v2;
    scanf("%d %d", &v1, &v2);
    v1--, v2--;
    a[v1][v2].scan();
  }
  t[0] = 6;
  dp[0][geth(t)] = 0;
  for (int i = 1; i < n; i++) {
    for (map<int, int>::iterator it = dp[i - 1].begin(); it != dp[i - 1].end();
         it++) {
      extr(b, it->first);
      gen(b, 0, i, it->second);
    }
  }
  for (int i = 0; i < 6; i++) {
    t[i] = 0;
  }
  t[0] = 6;
  for (int w = 0; w <= 5 * (n - 1); w++) {
    t[n - 1] = w;
    int h = geth(t);
    if (dp[n - 1].find(h) == dp[n - 1].end()) continue;
    printf("%d %d\n", w, dp[n - 1][h]);
    return 0;
  }
  printf("-1 -1\n");
  return 0;
}
