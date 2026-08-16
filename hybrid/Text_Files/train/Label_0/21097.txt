#include <bits/stdc++.h>
using namespace std;
const int N = 1e3 + 10;
const long double EPS = 1e-28;
using PII = pair<int, int>;
using LL = long long;
bool vis[N];
PII pos[8][N];
int k, n, used[8];
vector<vector<int> > v[8];
struct Point {
  long double ang;
  int x, y, id;
  long long dis;
  Point() {}
  Point(int x, int y) : x(x), y(y) {}
  void read() { scanf("%d%d", &x, &y); }
  bool operator<(const Point &b) const {
    return fabs(ang - b.ang) < EPS ? dis < b.dis : ang < b.ang;
  }
  Point operator-(const Point &b) const { return Point(x - b.x, y - b.y); }
} f[N], a[N];
bool dfs(int tot, set<int> st) {
  int u = *(st.begin());
  st.erase(st.begin());
  vis[u] = 1;
  for (int i = 1; i <= k; ++i) {
    if (!used[i]) {
      int x = pos[i][u].first, y = pos[i][u].second;
      set<int> rt = st;
      for (int j = 0; j < y; ++j) {
        if (!vis[v[i][x][j]]) rt.insert(v[i][x][j]);
        if (rt.size() >= tot) break;
      }
      used[i] = 1;
      if (rt.empty() || (rt.size() < tot && dfs(tot - 1, rt))) return 1;
      used[i] = 0;
    }
  }
  vis[u] = 0;
  return 0;
}
int main() {
  scanf("%d%d", &k, &n);
  for (int i = 1; i <= k; ++i) f[i].read(), f[i].id = i;
  for (int i = 1; i <= n; ++i) a[i].read(), a[i].id = i;
  for (int i = 1; i <= k; ++i) {
    for (int j = 1; j <= n; ++j) {
      Point c = a[j] - f[i];
      a[j].dis = (LL)c.x * c.x + (LL)c.y * c.y;
      a[j].ang = atan2(c.x, c.y);
    }
    sort(a + 1, a + n + 1);
    for (int j = 1; j <= n; ++j) {
      if (j == 1 || fabs(a[j].ang - a[j - 1].ang) > EPS)
        v[i].push_back(vector<int>());
      (*v[i].rbegin()).push_back(a[j].id);
      pos[i][a[j].id] = PII(v[i].size() - 1, (*v[i].rbegin()).size() - 1);
    }
  }
  int ret = 0;
  for (int i = 1; i <= n; ++i) {
    set<int> st;
    st.insert(i);
    memset(vis, 0, sizeof(vis));
    memset(used, 0, sizeof(used));
    ret += dfs(k, st);
  }
  printf("%d\n", ret);
  return 0;
}
