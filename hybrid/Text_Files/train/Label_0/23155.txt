#include <bits/stdc++.h>
using namespace std;
int sz[100010];
vector<int> v[100010];
int s[100010];
int c[100010];
int res[100010];
int n, m;
vector<pair<int, int> > q[100010];
int ans[100010];
void calc(int x, int p) {
  sz[x] = 1;
  for (int i = 0; i < v[x].size(); i++) {
    int y = v[x][i];
    if (y == p) continue;
    calc(y, x);
    sz[x] += sz[y];
  }
}
void clear(int x, int p) {
  res[s[c[x]]--]--;
  for (int i = 0; i < v[x].size(); i++) {
    int y = v[x][i];
    if (y == p) continue;
    clear(y, x);
  }
}
void add(int x, int p) {
  res[++s[c[x]]]++;
  for (int i = 0; i < v[x].size(); i++) {
    int y = v[x][i];
    if (y == p) continue;
    add(y, x);
  }
}
void solve(int x, int p) {
  int mx = 0;
  for (int i = 0; i < v[x].size(); i++) {
    int y = v[x][i];
    if (y == p) continue;
    if (sz[y] > sz[mx]) mx = y;
  }
  if (mx) {
    for (int i = 0; i < v[x].size(); i++) {
      int y = v[x][i];
      if (y == p || y == mx) continue;
      solve(y, x);
      clear(y, x);
    }
    solve(mx, x);
    for (int i = 0; i < v[x].size(); i++) {
      int y = v[x][i];
      if (y == p || y == mx) continue;
      add(y, x);
    }
  }
  res[++s[c[x]]]++;
  for (int i = 0; i < q[x].size(); i++) {
    ans[q[x][i].second] = res[q[x][i].first];
  }
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) scanf("%d", c + i);
  for (int i = 1; i < n; i++) {
    int a, b;
    scanf("%d%d", &a, &b);
    v[a].push_back(b);
    v[b].push_back(a);
  }
  for (int i = 1; i <= m; i++) {
    int a, b;
    scanf("%d%d", &a, &b);
    q[a].push_back(make_pair(b, i));
  }
  calc(1, -1);
  solve(1, -1);
  for (int i = 1; i <= m; i++) printf("%d\n", ans[i]);
  return 0;
}
