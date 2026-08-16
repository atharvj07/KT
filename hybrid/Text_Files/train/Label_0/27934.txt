#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000005;
int dsu[MAXN * 2], siz[MAXN * 2], mx[MAXN * 2], mx2[MAXN * 2];
int Root(int a) {
  if (dsu[a] == 0) return a;
  return dsu[a] = Root(dsu[a]);
}
void Union(int a, int b) {
  int r1 = Root(a), r2 = Root(b);
  if (r1 == r2) return;
  dsu[r1] = r2;
  siz[r2] += siz[r1];
  int tmp[4] = {mx[r1], mx2[r1], mx[r2], mx2[r2]};
  sort(tmp, tmp + 4);
  mx[r2] = tmp[3];
  mx2[r2] = tmp[2];
}
int n, m;
pair<int, int> A[MAXN];
int ti[MAXN * 2];
int cnt[MAXN * 2];
bool vis[MAXN];
bool check(int t) {
  memset(vis, 0, sizeof vis);
  int cnt1 = n, cnt2 = m;
  for (int i = 1; i <= n; i++)
    if (A[i].first <= t && A[i].second > t) {
      cnt1--;
      if (vis[A[i].first]) return false;
      vis[A[i].first] = true;
      cnt2--;
      if (!vis[A[i].second]) vis[A[i].second] = true, cnt2--;
    } else if (A[i].first > t)
      return false;
  return cnt2 >= cnt1;
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d%d", &A[i].first, &A[i].second);
    ti[i * 2 - 1] = A[i].first;
    ti[i * 2] = A[i].second;
  }
  sort(ti + 1, ti + 2 * n + 1);
  m = unique(ti + 1, ti + 2 * n + 1) - ti - 1;
  for (int i = 1; i <= m; i++) dsu[i] = 0, siz[i] = 1, mx[i] = i, mx2[i] = 0;
  for (int i = 1; i <= n; i++) {
    A[i].first = lower_bound(ti + 1, ti + m + 1, A[i].first) - ti;
    A[i].second = lower_bound(ti + 1, ti + m + 1, A[i].second) - ti;
    Union(A[i].first, A[i].second);
  }
  for (int i = 1; i <= n; i++) {
    int r1 = Root(A[i].first), r2 = Root(A[i].second);
    cnt[r1]++;
    if (r1 != r2) cnt[r2]++;
  }
  int ans = 0;
  for (int i = 1; i <= m; i++)
    if (dsu[i] == 0) {
      if (siz[i] < cnt[i]) {
        puts("-1");
        return 0;
      }
      if (siz[i] == cnt[i]) ans = max(ans, mx[i]);
      if (siz[i] > cnt[i]) ans = max(ans, mx2[i]);
    }
  printf("%d\n", ti[ans]);
  return 0;
}
