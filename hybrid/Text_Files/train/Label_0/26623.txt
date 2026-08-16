#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 3;
int n, m, vis[N], res;
vector<int> adj[N];
void read(int &val) {
  char c;
  do {
    c = getchar();
  } while (!isdigit(c));
  val = 0;
  while (isdigit(c)) {
    val = 10 * val + c - '0';
    c = getchar();
  }
}
int main() {
  read(n), read(m);
  for (int i = 1; i <= m; ++i) {
    int u, v;
    read(u), read(v);
    adj[u].push_back(v);
  }
  for (int i = 1; i <= n; ++i)
    if (!vis[i]) {
      vis[i] = 1;
      for (int v : adj[i])
        if (!vis[v]) vis[v] = -1;
    }
  for (int i = n; i >= 1; --i)
    if (vis[i] > 0) {
      ++res;
      for (int v : adj[i]) vis[v] = -1;
    }
  cout << res << '\n';
  for (int i = 1; i <= n; ++i)
    if (vis[i] > 0) cout << i << ' ';
}
