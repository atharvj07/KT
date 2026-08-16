#include <bits/stdc++.h>
using namespace std;
const int MX = 1e5 + 5;
const long long int MOD = 1e9 + 7;
vector<int> adj[MX], child[MX];
int t, n, u, v, m;
bool visited[MX];
long long int p[MX], w[MX], SIZE[MX];
void getSize(int pos) {
  SIZE[pos] = 1;
  for (int next : child[pos]) {
    getSize(next);
    SIZE[pos] += SIZE[next];
  }
  w[pos - 1] = SIZE[pos] * (n - SIZE[pos]);
}
int main() {
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) child[i].clear(), adj[i].clear();
    for (int i = 0; i < n - 1; i++) {
      scanf("%d %d", &u, &v);
      adj[u].push_back(v);
      adj[v].push_back(u);
    }
    scanf("%d", &m);
    for (int i = 1; i <= m; i++) scanf("%lld", &p[i]);
    for (int i = m + 1; i < n; i++) p[i] = 1;
    m = max(m, n - 1);
    sort(p + 1, p + m + 1);
    for (int i = m; i >= n; i--) p[n - 1] = (p[i] * p[n - 1]) % MOD;
    fill(visited + 1, visited + n + 1, false);
    queue<int> q;
    q.push(1), visited[1] = true;
    while (!q.empty()) {
      int pos = q.front();
      q.pop();
      for (int next : adj[pos]) {
        if (visited[next]) continue;
        visited[next] = true;
        child[pos].push_back(next);
        q.push(next);
      }
    }
    getSize(1);
    sort(w + 1, w + n);
    long long int ans = 0;
    for (int i = 1; i < n; i++) ans = (ans + (w[i] % MOD) * p[i]) % MOD;
    printf("%lld\n", ans);
  }
}
