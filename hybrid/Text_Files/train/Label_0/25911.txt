#include <bits/stdc++.h>
using namespace std;
int n, m;
int a, b;
int D[100010];
int vis[100010];
vector<int> E[100010];
priority_queue<int> Q;
int main() {
  cin >> n >> m;
  for (int i = 1; i <= m; i++) {
    cin >> a >> b;
    D[a]++;
    E[b].push_back(a);
  }
  for (int i = n; i >= 1; i--)
    if (D[i] == 0) Q.push(i);
  int now = n;
  while (!Q.empty()) {
    int nd = Q.top();
    Q.pop();
    if (vis[nd]) continue;
    vis[nd] = now--;
    for (auto i : E[nd]) {
      D[i]--;
      if (!D[i] && !vis[i]) Q.push(i);
    }
  }
  for (int i = 1; i <= n; i++) cout << vis[i] << " ";
}
