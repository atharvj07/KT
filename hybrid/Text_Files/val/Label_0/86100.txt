#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5 + 100;
const long long mod = 1e9 + 7;
struct node {
  int s, e, next;
} edge[maxn * 2];
vector<int> p[maxn], s[maxn];
int d[maxn], vis[maxn];
void bfs(int t) {
  queue<int> q;
  q.push(t);
  vis[t] = 1;
  while (!q.empty()) {
    int x = q.front();
    q.pop();
    for (int i = 0; i < p[x].size(); i++) {
      int y = p[x][i];
      if (!vis[y]) {
        vis[y] = 1;
        d[y] = d[x] + 1;
        q.push(y);
      }
    }
  }
}
int a[maxn];
int main() {
  ios::sync_with_stdio(0);
  int n, m, k;
  cin >> n >> m;
  for (int i = 1, x, y; i <= m; i++) {
    cin >> x >> y;
    s[x].push_back(y);
    p[y].push_back(x);
  }
  cin >> k;
  for (int i = 1; i <= k; i++) cin >> a[i];
  bfs(a[k]);
  int ansin = 0, ansax = 0;
  for (int i = 1; i < k; i++) {
    int x = a[i], num = 0;
    for (int j = 0; j < s[x].size(); j++) {
      int y = s[x][j];
      if (d[y] == d[x] - 1) num++;
    }
    if (d[x] - 1 == d[a[i + 1]] && num == 1)
      continue;
    else if (d[x] - 1 == d[a[i + 1]] && num >= 2)
      ansax++;
    else
      ansin++, ansax++;
  }
  cout << ansin << " " << ansax << endl;
  return 0;
}
