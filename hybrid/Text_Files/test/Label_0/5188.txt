#include <bits/stdc++.h>
using namespace std;
const int ml = 200000;
int n, i, j, k, v, la, x, y, m, ans, p;
vector<pair<pair<int, int>, int> > a;
int main() {
  scanf("%d", &n);
  ans = 0;
  for (i = 1; i <= n; ++i) {
    p = la = 0;
    scanf("%d%d%d%d%d", &k, &v, &x, &y, &m);
    for (j = 1; j <= k; ++j) {
      if (v < la) ++p;
      if (a.size() <= ml) a.push_back(make_pair(make_pair(p, v), i));
      la = v, v = ((long long)v * x + y) % m;
    }
    ans = max(ans, p);
  }
  printf("%d\n", ans);
  if (a.size() <= ml) {
    sort(a.begin(), a.end());
    for (i = 0; i < a.size(); ++i)
      printf("%d %d\n", a[i].first.second, a[i].second);
  }
  return 0;
}
