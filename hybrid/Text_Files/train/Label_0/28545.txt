#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:1000000000")
using namespace std;
const int maxn = (int)1e5 + 10;
int ver = -1;
int num = -1;
long long c[maxn];
vector<pair<int, int> > ed[maxn];
long long res[maxn];
int h[maxn];
vector<pair<int, int> > e[maxn];
void dfs(int v, int d) {
  h[v] = d;
  for (int i = 0; i < (int)ed[v].size(); i++) {
    int u = ed[v][i].first;
    if (h[u] == -1) {
      e[v].push_back(make_pair(u, ed[v][i].second));
      e[u].push_back(make_pair(v, ed[v][i].second));
      dfs(u, d + 1);
    }
  }
}
bool used[maxn];
long long go(int v) {
  used[v] = true;
  long long ans = c[v];
  for (int i = 0; i < (int)e[v].size(); i++) {
    int u = e[v][i].first;
    int w = e[v][i].second;
    if (w == num) {
      continue;
    }
    if (!used[u]) {
      long long now = go(u);
      res[w] = now;
      ans -= now;
    }
  }
  return ans;
}
pair<int, int> edg[maxn];
int main() {
  memset(h, -1, sizeof h);
  int n, m;
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    scanf("%lld", &c[i]);
  }
  for (int i = 0; i < m; i++) {
    int a, b;
    scanf("%d %d", &a, &b);
    edg[i] = make_pair(a, b);
    ed[a].push_back(make_pair(b, i));
    ed[b].push_back(make_pair(a, i));
  }
  dfs(1, 0);
  for (int i = 0; i < m; i++) {
    int a = edg[i].first;
    int b = edg[i].second;
    int dst = abs(h[a] - h[b]);
    if (dst % 2 == 0) {
      ver = a;
      num = i;
      break;
    }
  }
  if (ver == -1) {
    ver = 1;
  }
  long long ch = go(ver);
  if (ch == 0) {
    cout << "YES" << endl;
    for (int i = 0; i < m; i++) {
      printf("%lld\n", res[i]);
    }
    return 0;
  }
  if (num == -1 || ch % 2 != 0) {
    cout << "NO" << endl;
    return 0;
  }
  res[num] = ch / 2;
  c[edg[num].first] -= ch / 2;
  c[edg[num].second] -= ch / 2;
  memset(used, 0, sizeof used);
  ch = go(ver);
  if (ch != 0) {
    throw 1;
  }
  cout << "YES" << endl;
  for (int i = 0; i < m; i++) {
    printf("%lld\n", res[i]);
  }
  return 0;
}
