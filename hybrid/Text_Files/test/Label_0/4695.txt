#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2e5 + 7;
int T;
int n, a[MAXN], f[MAXN][3], vis[MAXN];
vector<int> v;
inline int getid(int x) {
  return lower_bound(v.begin(), v.end(), x) - v.begin() + 1;
}
inline void solve() {
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()), v.end());
  for (int i = 1; i <= n; ++i) {
    a[i] = getid(a[i]);
  }
  for (int i = n; i >= 1; --i) {
    if (!vis[a[i]]) vis[a[i]] = i;
  }
  int ans = 0;
  for (int i = 1; i <= n; ++i) {
    f[a[i]][0] = f[a[i]][0] + 1;
    if (f[a[i]][1])
      f[a[i]][1] = f[a[i]][1] + 1;
    else {
      f[a[i]][1] = max(f[a[i] - 1][0] + 1, f[a[i]][1]);
      if (i > vis[a[i] - 1]) f[a[i]][1] = max(f[a[i] - 1][1] + 1, f[a[i]][1]);
    }
    f[a[i]][2] = max(f[a[i]][2] + 1, f[a[i] - 1][0] + 1);
    if (i > vis[a[i] - 1]) {
      f[a[i]][2] = max(f[a[i] - 1][1] + 1, f[a[i]][2]);
    }
    ans = max(f[a[i]][2], ans);
  }
  printf("%d\n", n - ans);
  v.clear();
  for (int i = 1; i <= n; ++i) {
    f[i][0] = 0;
    f[i][1] = 0;
    f[i][2] = 0;
    vis[i] = 0;
  }
}
int main() {
  scanf("%d", &T);
  while (T-- > 0) {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
      scanf("%d", &a[i]);
      v.push_back(a[i]);
    }
    solve();
  }
  return 0;
}
