#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
const long long INF = 0x3f3f3f3f3f3f3f3f;
const double pi = acos(-1.0);
const int maxn = 100000 + 10;
const int mod = 1e9 + 7;
int n, m, w;
pair<int, int> que[600];
int lim[1200];
int check(int len) {
  vector<int> edg;
  edg.push_back(1), edg.push_back(n);
  int L = inf, R = -1, U = inf, D = -1;
  for (int i = 0; i < w; i++) {
    int u = que[i].first - len;
    int v = que[i].first + len - 1;
    if (u >= 1 && u <= n) edg.push_back(u);
    if (u + 1 >= 1 && u + 1 <= n) edg.push_back(u + 1);
    if (v >= 1 && v <= n) edg.push_back(v);
    if (v + 1 >= 1 && v + 1 <= n) edg.push_back(v + 1);
  }
  sort(edg.begin(), edg.end());
  int q = unique(edg.begin(), edg.end()) - edg.begin();
  for (int i = 0; i < q; i++) {
    vector<pair<int, int> > sub;
    for (int j = 0; j < w; j++) {
      int ll = que[j].second - len + 1;
      int rr = que[j].second + len;
      int u = que[j].first - len + 1;
      int v = que[j].first + len - 1;
      if (edg[i] >= u && edg[i] <= v) {
        sub.push_back(make_pair(max(ll, 1), -1));
        sub.push_back(make_pair(min(rr, m + 1), 1));
      }
    }
    sub.push_back(make_pair(m + 1, 1));
    sort(sub.begin(), sub.end());
    int sum = 0;
    int pre = 1;
    if (sub.size() <= 1) {
      L = min(L, 1);
      R = max(R, m);
      U = min(U, edg[i]);
      D = max(D, edg[i]);
    }
    for (int j = 0; sub[j].first <= m;) {
      while (sub[j].first == pre) sum += sub[j].second, j++;
      if (sum == 0) {
        L = min(L, pre);
        R = max(R, sub[j].first - 1);
        U = min(U, edg[i]);
        D = max(D, edg[i]);
      }
      pre = sub[j].first;
    }
  }
  if (R - L + 2 <= 2 * len && D - U + 2 <= 2 * len) return 1;
  return 0;
}
int main() {
  scanf("%d%d%d", &n, &m, &w);
  for (int i = 0; i < w; i++) {
    scanf("%d%d", &(que[i].first), &que[i].second);
  }
  sort(que, que + w);
  int l = 1, r = max(n, m);
  int ans = 0;
  while (l <= r) {
    int mid = (l + r) >> 1;
    if (check(mid))
      ans = mid, r = mid - 1;
    else
      l = mid + 1;
  }
  cout << ans - 1 << endl;
  return 0;
}
