#include <bits/stdc++.h>
using namespace std;
vector<int> a[150001];
bool visited[150002];
long long cnt;
void dfs(int start) {
  cnt++;
  visited[start] = true;
  for (int i = 0; i < a[start].size(); i++) {
    int next = a[start][i];
    if (!visited[next]) dfs(next);
  }
}
int main() {
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    a[u].push_back(v);
    a[v].push_back(u);
  }
  long long ans = 0;
  for (int i = 1; i <= n; i++) {
    cnt = 0;
    if (!visited[i]) {
      dfs(i);
      ans += cnt * (cnt - 1) / 2;
    }
  }
  if (ans == m)
    printf("YES");
  else
    printf("NO");
  return 0;
}
