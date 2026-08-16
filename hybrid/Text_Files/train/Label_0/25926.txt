#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100000;
int n, x[MAXN], y[MAXN];
set<int> p[MAXN + 1];
bool exist(int x, int y) { return p[x].find(y) != p[x].end(); }
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d %d", &x[i], &y[i]);
    p[x[i]].insert(y[i]);
  }
  int ans = 0;
  for (int i = 0; i <= MAXN; ++i) {
    int size = (int)p[i].size();
    if (size == 0 || size <= n / size) {
      for (set<int>::iterator j = p[i].begin(); j != p[i].end(); ++j) {
        int y1 = *j;
        for (set<int>::iterator k = p[i].begin(); k != j; ++k) {
          int y2 = *k;
          int len = abs(y2 - y1);
          if (i + len <= MAXN && exist(i + len, y1) && exist(i + len, y2)) {
            ans++;
          }
        }
      }
    } else {
      for (int j = 0; j < n; ++j) {
        int x1 = x[j];
        int y1 = y[j];
        if (i < x1) {
          int dx = x1 - i;
          if (y1 + dx <= MAXN && exist(i, y1) && exist(i, y1 + dx) &&
              exist(x1, y1 + dx)) {
            ans++;
          }
        }
      }
    }
  }
  printf("%d\n", ans);
  return 0;
}
