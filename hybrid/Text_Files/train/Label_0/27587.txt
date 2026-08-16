#include <bits/stdc++.h>
using namespace std;
int aa[100005], bb[100005];
int main() {
  int n, y1;
  scanf("%d %d", &n, &y1);
  for (int i = 1; i <= n; i++) scanf("%d", aa + i);
  int m, y2;
  scanf("%d %d", &m, &y2);
  for (int i = 1; i <= m; i++) scanf("%d", bb + i);
  int ans = 2;
  for (int k = 1; k < 30; k++) {
    int d = (1 << k);
    map<int, int> ma1, ma2;
    for (int i = 1; i <= n; i++) ma1[aa[i] % d]++;
    for (int i = 1; i <= m; i++) ma2[bb[i] % d]++;
    for (pair<int, int> p : ma1)
      ans = max(ans, p.second + ma2[(p.first + d / 2) % d]);
    for (pair<int, int> p : ma2)
      ans = max(ans, p.second + ma1[(p.first + d / 2) % d]);
  }
  printf("%d\n", ans);
  return 0;
}
