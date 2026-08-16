#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:836777216")
using namespace std;
bool a[705][705];
int b[705][705];
int cnt[705];
int main(void) {
  int n, m;
  scanf("%d%d", &n, &m);
  memset((cnt), (0), sizeof((cnt)));
  memset((a), (0), sizeof((a)));
  memset((b), (0), sizeof((b)));
  for (int(i) = 0; (i) < (m); (i)++) {
    int x, y;
    scanf("%d%d", &x, &y);
    x--, y--;
    a[x][y] = 1;
    a[y][x] = 1;
    cnt[x]++;
    cnt[y]++;
  }
  for (int(i) = 0; (i) < (n); (i)++) {
    for (int(j) = (i + 1); (j) < (n); (j)++) {
      int cnt = 0;
      for (int(k) = 0; (k) < (n); (k)++) {
        if (a[i][k] && a[k][j]) {
          cnt++;
        }
      }
      b[i][j] = b[j][i] = cnt;
    }
  }
  long long ans = 0;
  for (int(i) = 0; (i) < (n); (i)++) {
    for (int(j) = (i + 1); (j) < (n); (j)++) {
      if (a[i][j] == 1) {
        for (int(k) = 0; (k) < (n); (k)++) {
          if (i != k && j != k) {
            int q1 = b[i][k];
            int q2 = b[j][k];
            if (a[i][k]) {
              q2--;
            }
            if (a[j][k]) {
              q1--;
            }
            ans += (long long)q1 * q2;
            if (a[i][k] && a[k][j]) {
              ans -= (long long)(cnt[k] - 2);
            }
          }
        }
      }
    }
  }
  ans /= 5;
  printf("%lld\n", ans);
}
