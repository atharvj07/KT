#include <bits/stdc++.h>
using namespace std;
const int N = 100010;
int n;
char s[N];
int f[N];
void getfail(char* a, int n) {
  int i, j;
  for (f[0] = j = -1, i = 1; i < n; f[i++] = j) {
    while (~j && a[j + 1] != a[i]) j = f[j];
    if (a[j + 1] == a[i]) ++j;
  }
}
vector<pair<int, int> > ans;
vector<int> G[N];
int sz[N];
void dfs(int u) {
  sz[u] = 1;
  for (int v : G[u]) dfs(v), sz[u] += sz[v];
}
int main() {
  scanf(" %s", s), n = strlen(s);
  getfail(s, n);
  for (int i = (0); i <= (n - 1); ++i) G[f[i] + 1].push_back(i + 1);
  dfs(0);
  int now = n - 1;
  while (~now) {
    now = f[now];
    if (now == -1)
      ans.push_back({n, 1});
    else
      ans.push_back({now + 1, sz[now + 1]});
  }
  sort(ans.begin(), ans.end());
  cout << ans.size() << '\n';
  for (pair<int, int> A : ans) cout << A.first << " " << A.second << endl;
  return 0;
}
