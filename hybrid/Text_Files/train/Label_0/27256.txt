#include <bits/stdc++.h>
const int N = 1e6 + 5;
using namespace std;
long long gcd(long long a, long long b) { return (b == 0 ? a : gcd(b, a % b)); }
int lcm(int a, int b) { return (a * b) / gcd(a, b); }
int n, m, a[N], ans[N], cnt, vis[101], now;
char temp;
vector<int> mp[101];
struct Node {
  int pathsum, dis;
  Node() { pathsum = 0, dis = INT_MAX; }
} node[101][101];
void dfs(int t, int s, int e) {
  vis[t] = 1;
  for (int i = 0; i < mp[t].size(); ++i) {
    if (vis[mp[t][i]]) continue;
    now++;
    if (now >= node[s][e].dis) {
      vis[t] = 0;
      now--;
      return;
    }
    if (mp[t][i] == e) {
      vis[t] = 0;
      node[s][e].dis = now;
      now--;
      return;
    }
    dfs(mp[t][i], s, e);
    now--;
  }
  vis[t] = 0;
  return;
}
int main() {
  ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      cin >> temp;
      if (temp == '1') mp[i].push_back(j);
    }
  }
  cin >> m;
  for (int i = 0; i < m; ++i) cin >> a[i];
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (i == j) continue;
      now = 0;
      dfs(i, i, j);
    }
  }
  int i;
  for (i = 0; i < m - 2;) {
    if (node[a[i]][a[i + 2]].dis == 2) {
      if (i + 3 < m) {
        int j, flag = 1;
        for (j = i + 3; j < m && flag;) {
          if (node[a[i]][a[j]].dis != j - i) flag = 0;
          if (flag) ++j;
        }
        if (flag) {
          ans[cnt++] = a[m - 1];
          i = m - 1;
        } else {
          ans[cnt++] = a[j - 1];
          i = j - 1;
        }
      } else {
        ans[cnt++] = a[i + 2];
        i = m - 1;
      }
    } else {
      ans[cnt++] = a[i + 1];
      ++i;
    }
  }
  cout << cnt + 1 + (i == m - 2) << endl << a[0] << ' ';
  for (int i = 0; i < cnt; ++i) cout << ans[i] << ' ';
  if (i == m - 2) cout << a[m - 1];
  return 0;
}
