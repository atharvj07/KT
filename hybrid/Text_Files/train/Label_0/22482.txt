#include <bits/stdc++.h>
using namespace std;
vector<pair<int, int>> v1;
int v2[200200] = {0}, v3[200200];
int main() {
  int n, m, d;
  scanf("%d%d%d", &n, &m, &d);
  for (int i = 0; i < n; i++) {
    int x;
    scanf("%d", &x);
    v1.push_back(make_pair(x, i));
    v3[i] = x;
  }
  int len = v1.size(), j = 0, t = 0, ans = 0, cnt = 0;
  sort(v1.begin(), v1.end());
  sort(v3, v3 + len);
  while (cnt < len) {
    ans++;
    t = 1;
    int c = -(d + 1);
    for (int i = j; i < len; i++) {
      if (v2[v1[i].second]) continue;
      if (v1[i].first - c >= d) {
        v2[v1[i].second] = ans;
        c = v1[i].first + 1;
        i = lower_bound(v3, v3 + len, c + d) - v3 - 1;
        if ((i - j > 1) && t == 1)
          j = j + 1;
        else if (t == 1)
          j = i;
        cnt++;
        t = 0;
      }
    }
  }
  cout << ans << endl;
  for (int i = 0; i < len; i++) {
    printf("%d ", v2[i]);
  }
  return 0;
}
