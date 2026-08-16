#include <bits/stdc++.h>
using namespace std;
const int N = 80, N2 = (1 << 18) + 1;
int cnt, n, m, A, B, fa[N], sz[N], bl[N], dis[N][N2], inq[N][N2], ans[N];
queue<pair<int, int> > q;
vector<pair<int, int> > g[N];
int find(int x) { return fa[x] == x ? x : fa[x] = find(fa[x]); }
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> m >> A >> B;
  for (int i = 1; i <= n; ++i) fa[i] = i, sz[i] = 1;
  for (int i = 1; i <= m; ++i) {
    int x, y, z;
    cin >> x >> y >> z;
    g[x].emplace_back(y, z);
    g[y].emplace_back(x, z);
    if (z == A && (x = find(x)) != (y = find(y))) fa[x] = y, sz[y] += sz[x];
  }
  for (int i = 1; i <= n; ++i)
    if (sz[find(i)] >= 4) {
      if (!bl[find(i)]) bl[find(i)] = 1 << (cnt++);
      bl[i] = bl[find(i)];
    }
  memset(ans, 0x3f, sizeof ans);
  memset(dis, 0x3f, sizeof dis);
  dis[1][bl[1]] = 0;
  q.emplace(1, bl[1]);
  while (!q.empty()) {
    auto x = q.front();
    q.pop();
    inq[x.first][x.second] = 0;
    int d = dis[x.first][x.second];
    ans[x.first] = min(ans[x.first], d);
    for (auto i : g[x.first])
      if (i.second == A) {
        if (dis[i.first][x.second] > d + i.second) {
          dis[i.first][x.second] = d + i.second;
          if (!inq[i.first][x.second])
            inq[i.first][x.second] = 1, q.emplace(i.first, x.second);
        }
      } else if (find(x.first) != find(i.first) &&
                 ((x.second & bl[i.first]) == 0)) {
        if (dis[i.first][x.second | bl[i.first]] > d + i.second) {
          dis[i.first][x.second | bl[i.first]] = d + i.second;
          if (!inq[i.first][x.second | bl[i.first]])
            inq[i.first][x.second | bl[i.first]] = 1,
                                    q.emplace(i.first, x.second | bl[i.first]);
        }
      }
  }
  for (int i = 1; i <= n; ++i) cout << ans[i] << " \n"[i == n];
  return 0;
}
