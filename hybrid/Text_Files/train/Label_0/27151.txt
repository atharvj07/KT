#include <bits/stdc++.h>
using namespace std;
long long n, m, k, t, i, j, sig = 0, h, num;
long long a[5005];
long long dis[5005];
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  memset(a, 0, sizeof(a));
  ;
  for (i = 1; i <= 5000; i++) dis[i] = 0x3f3f3f3f;
  cin >> n >> m;
  int x, y;
  for (i = 0; i < m; i++) {
    cin >> x >> y;
    a[x]++;
    long long tmp;
    if (y < x)
      tmp = y + n - x;
    else
      tmp = y - x;
    dis[x] = min(dis[x], tmp);
  }
  long long maxx = 0, time = 0;
  for (i = 1; i <= n; i++) {
    maxx = max(maxx, a[i]);
  }
  time = (maxx - 1) * n;
  for (i = 1; i <= n; i++) {
    num = 0;
    t = 0;
    for (j = i;; j++) {
      num++;
      if (j > n) j = 1;
      if (a[j] == maxx) t = max(num - 1 + dis[j], t);
      if (a[j] == maxx - 1 && dis[j] < 0x3f3f3f3f && maxx > 1) {
        if (j < i)
          t = max(dis[j] - i + j, t);
        else {
          t = max(dis[j] - n + j - i, t);
        }
      }
      if (num >= n) break;
    }
    if (sig++) cout << ' ';
    cout << time + t;
  }
  return 0;
}
