#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
using pi3 = pair<int, pii>;
using INT = long long;
const int inf = 1e9;
const int MM = 10101;
const int KK = 1010;
int dp[MM][KK];
int a[MM];
int n, m;
int out(int first) { return first < 1 || first > m; }
int dx[] = {-1, 1};
int main() {
  cin >> n >> m;
  for (int i = 1; i <= m; i++) scanf("%d", a + i);
  sort(a + 1, a + m + 1);
  int R, G;
  cin >> G >> R;
  for (int i = 0; i <= m; i++) {
    for (int j = 0; j <= G; j++) {
      dp[i][j] = 1e9;
    }
  }
  a[m + 1] = n;
  for (int i = 1; i <= m + 1; i++) {
    if (a[i] - a[i - 1] > G) {
      puts("-1");
      return 0;
    }
  }
  dp[0][0] = 0;
  if (a[1] < G)
    dp[1][a[1]] = 0;
  else
    dp[1][0] = 1;
  priority_queue<pii, vector<pii>, greater<pii> > st;
  if (a[1] < G)
    st.push(pii(0, G + a[1]));
  else
    st.push(pii(1, G));
  while (!st.empty()) {
    auto p = st.top();
    st.pop();
    int dis = p.first, first = p.second;
    int u = first / G;
    int tp = first % G;
    for (int i = 0; i < 2; i++) {
      int v = u + dx[i];
      if (out(v)) continue;
      int dst = tp + abs(a[u] - a[v]);
      if (dst > G) continue;
      if (dst == G) {
        if (dp[v][0] > dp[u][tp] + 1) {
          dp[v][0] = dp[u][tp] + 1;
          st.push(pii(dp[v][0], v * G));
        }
        continue;
      }
      if (dp[v][dst] > dp[u][tp]) {
        dp[v][dst] = dp[u][tp];
        st.push(pii(dp[v][dst], v * G + dst));
      }
    }
  }
  INT ans = inf;
  for (int i = 1; i <= m; i++) {
    if (a[i] + G < n) continue;
    if (dp[i][0] > inf) continue;
    ans = min(ans, 1ll * dp[i][0] * (G + R) + n - a[i]);
  }
  if (ans == inf) ans = -1;
  cout << ans;
}
