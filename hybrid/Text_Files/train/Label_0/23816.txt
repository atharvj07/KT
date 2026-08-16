#include <bits/stdc++.h>
using namespace std;
const int N = 5e4 + 10;
pair<pair<int, int>, pair<int, int> > p[N];
void solve() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i)
    scanf("%d%d%d", &p[i].first.first, &p[i].first.second, &p[i].second.first),
        p[i].second.second = i;
  sort(p + 1, p + 1 + n);
  vector<int> v;
  for (int i = 1; i <= n;) {
    int j = i;
    for (; j <= n; ++j)
      if (p[i].first.first != p[j].first.first) break;
    vector<int> vv;
    for (int k = i; k < j;)
      if (k == j - 1 || p[k].first.second != p[k + 1].first.second)
        vv.push_back(p[k].second.second), k++;
      else
        printf("%d %d\n", p[k].second.second, p[k + 1].second.second), k += 2;
    for (int k = 0; k < (int)(vv.size()) - 1; k += 2)
      printf("%d %d\n", vv[k], vv[k + 1]);
    if (vv.size() % 2) v.push_back(vv.back());
    i = j;
  }
  for (int i = 0; i < (int)v.size() - 1; i += 2)
    printf("%d %d\n", v[i], v[i + 1]);
}
int main() {
  int t = 1;
  while (t--) solve();
  return 0;
}
