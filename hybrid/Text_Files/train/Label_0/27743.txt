#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e3 * 2 + 10;
vector<int> adj[maxn];
int p[maxn];
int mark[maxn];
void bfs(int v) {
  mark[v] = 0;
  queue<int> q;
  q.push(v);
  while (q.size()) {
    int x = q.front();
    q.pop();
    for (int i : adj[x]) {
      if (mark[i] == -1) {
        mark[i] = mark[x] + 1;
        q.push(i);
      }
    }
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  ;
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    x--;
    if (x >= 0) {
      adj[x].push_back(i);
    }
    p[i] = x;
  }
  for (int i = 0; i < n; i++) {
    mark[i] = -1;
  }
  for (int i = 0; i < n; i++) {
    if (mark[i] == -1 && p[i] < 0) {
      bfs(i);
    }
  }
  int ans = 0;
  for (int i = 0; i < n; i++) {
    ans = max(ans, mark[i]);
  }
  cout << ans + 1;
  return 0;
}
