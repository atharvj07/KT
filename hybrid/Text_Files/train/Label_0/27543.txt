#include <bits/stdc++.h>
using namespace std;
int n, m, x, y;
int a[111111], b[111111];
int p, q;
vector<pair<int, int> > ans;
bool fits(int man, int suit) {
  if (suit >= man - x && suit <= man + y) return true;
  return false;
}
int main() {
  scanf("%d%d%d%d", &n, &m, &x, &y);
  for (int i = 0; i < n; i++) scanf("%d", &a[i]);
  for (int i = 0; i < m; i++) scanf("%d", &b[i]);
  p = q = 0;
  ans.clear();
  while (p < n && q < m) {
    if (fits(a[p], b[q])) {
      p++;
      q++;
      ans.push_back(make_pair(p, q));
      continue;
    }
    if (p == n)
      q++;
    else if (q == m)
      p++;
    else if (a[p] < b[q])
      p++;
    else
      q++;
  }
  printf("%d\n", ans.size());
  for (int i = 0; i < ans.size(); i++)
    printf("%d %d\n", ans[i].first, ans[i].second);
  return 0;
}
