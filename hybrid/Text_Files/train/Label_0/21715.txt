#include <bits/stdc++.h>
using namespace std;
const int N = 102;
const int MOD = 1e9 + 7;
long long int powmod(long long int a, long long int b) {
  if (b == 0) return 1;
  long long int x = powmod(a, b / 2);
  long long int y = (x * x) % MOD;
  if (b % 2) return (a * y) % MOD;
  return y % MOD;
}
vector<string> p;
bool vis[102][102];
bool lake;
int cnt, ans;
int n, m, k;
vector<pair<int, pair<int, int> > > q;
void dfs(int i, int j) {
  if (i < 0 || i >= n || j < 0 || j >= m || vis[i][j] || p[i][j] == '*') return;
  if (i == 0 || i == n - 1 || j == 0 || j == m - 1) lake = false;
  vis[i][j] = true;
  cnt++;
  dfs(i + 1, j);
  dfs(i, j + 1);
  dfs(i - 1, j);
  dfs(i, j - 1);
}
void dfsclean(int i, int j) {
  if (i < 0 || i >= n || j < 0 || j >= m || vis[i][j] || p[i][j] == '*') return;
  vis[i][j] = true;
  p[i][j] = '*';
  dfsclean(i + 1, j);
  dfsclean(i, j + 1);
  dfsclean(i - 1, j);
  dfsclean(i, j - 1);
}
int main() {
  scanf("%d", &n);
  scanf("%d", &m);
  scanf("%d", &k);
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    p.push_back(s);
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (p[i][j] == '.' && !vis[i][j]) {
        cnt = 0;
        lake = true;
        dfs(i, j);
        if (lake) q.push_back(make_pair(cnt, make_pair(i, j)));
      }
    }
  }
  memset(vis, false, sizeof(vis));
  sort((q).begin(), (q).end());
  while ((int)(q.size()) > k) {
    ans += q[0].first;
    dfsclean(q[0].second.first, q[0].second.second);
    q.erase(q.begin());
  }
  printf("%d\n", ans);
  for (int i = 0; i < n; i++) cout << p[i] << '\n';
  return 0;
}
