#include <bits/stdc++.h>
using namespace std;
int m, k, n, s, a[500005], mp[500005], x, kd, cnt, vi[500005], l, r, ed, i, rm,
    CNT;
map<int, int> mk;
vector<int> ans;
int main() {
  cin >> m >> k >> n >> s;
  for (i = 1; i <= m; i++) scanf("%d", &a[i]);
  for (i = 1; i <= s; i++) {
    scanf("%d", &x);
    if (!mp[x]) {
      kd++;
    }
    mp[x]++;
  }
  cnt = 0;
  for (l = 1; l <= m;) {
    while (cnt < kd && r <= m) {
      vi[a[++r]]++;
      if (vi[a[r]] == mp[a[r]]) cnt++;
    }
    if (r > m) break;
    if (cnt == kd) {
      ed = max(l + k - 1, r);
      if (ed <= m) {
        if ((l - 1) / k + (m - ed) / k >= n - 1) {
          rm = (l - 1) % k;
          for (i = 1; i <= rm; i++) ans.push_back(i);
          mk.clear();
          if (r > l + k - 1) {
            CNT = r - (l + k - 1);
            for (i = l; i <= ed; i++) {
              if (mp[a[i]] && mk[a[i]] < mp[a[i]]) {
                mk[a[i]]++;
              } else if (CNT) {
                ans.push_back(i);
                CNT--;
              }
            }
          }
          printf("%d\n", ans.size());
          for (i = 0; i < ans.size(); i++) printf("%d ", ans[i]);
          return 0;
        }
      }
    }
    if (vi[a[l]] == mp[a[l]]) cnt--;
    vi[a[l++]]--;
  }
  cout << -1;
}
