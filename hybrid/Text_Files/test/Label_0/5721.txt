#include <bits/stdc++.h>
using namespace std;
const int N = 50;
int x[N][N], y[N], True[N], False[N], ans;
int n, m;
bool flag = false;
void dfs(int pos) {
  if (pos > n) {
    ans++;
    return;
  }
  bool f = true;
  for (int i = 1; i <= m; i++) {
    if (!x[i][pos])
      True[i]++;
    else
      False[i]++;
    if (True[i] > y[i] || False[i] > n - y[i]) f = false;
  }
  if (f) dfs(pos + 1);
  f = true;
  for (int i = 1; i <= m; i++) {
    if (!x[i][pos])
      True[i]--, False[i]++;
    else
      False[i]--, True[i]++;
    if (True[i] > y[i] || False[i] > n - y[i]) f = false;
  }
  if (f) dfs(pos + 1);
  for (int i = 1; i <= m; i++) {
    if (!x[i][pos])
      False[i]--;
    else
      True[i]--;
  }
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) scanf("%1d", &x[i][j]);
    scanf("%d", &y[i]);
  }
  dfs(1);
  printf("%d", ans);
}
