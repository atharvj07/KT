#include <bits/stdc++.h>
const int maxn = (1 << 20);
using namespace std;
long long a[maxn] = {0};
long long b[maxn] = {0};
long long val[40] = {0};
long long ans = 0;
long long n, m;
long long cnt;
long long en;
long long tot1, tot2;
void dfs(int cur, long long sum) {
  if (cur == en) {
    a[cnt++] = sum;
    return;
  }
  dfs(cur + 1, sum);
  dfs(cur + 1, sum + val[cur]);
}
void dfs1(int cur, long long sum) {
  if (cur == en) {
    b[cnt++] = sum;
    return;
  }
  dfs1(cur + 1, sum);
  dfs1(cur + 1, sum + val[cur]);
}
int main() {
  ios_base ::sync_with_stdio(false);
  cin >> n >> m;
  for (int i = 1; i <= n; ++i) cin >> val[i];
  cnt = 0;
  en = (n + 1) / 2 + 1;
  dfs(1, 0);
  tot1 = cnt;
  cnt = 0;
  en = n + 1;
  dfs1((n + 1) / 2 + 1, 0);
  tot2 = cnt;
  for (int i = 0; i < tot1; ++i) {
    a[i] %= m;
    ans = max(ans, a[i]);
  }
  for (int i = 0; i < tot2; ++i) {
    b[i] %= m;
    ans = max(ans, b[i]);
  }
  sort(a, a + tot1);
  sort(b, b + tot2);
  for (int i = 0; i < tot1; ++i) {
    int u = m - a[i];
    int v = 2 * m - a[i];
    int pos1 = lower_bound(b, b + tot2, u) - b;
    int pos2 = lower_bound(b, b + tot2, v) - b;
    if (pos1) {
      pos1--;
      ans = max(ans, (a[i] + b[pos1]) % m);
    }
    if (pos2) {
      pos2--;
      ans = max(ans, (a[i] + b[pos2]) % m);
    }
  }
  cout << ans << endl;
  return 0;
}
