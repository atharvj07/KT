#include <bits/stdc++.h>
using namespace std;
template <typename T>
T abs(T a) {
  return a < 0 ? -a : a;
}
template <typename T>
T sqr(T a) {
  return a * a;
}
const int INF = (int)1e9;
const long double EPS = 1e-9;
const long double PI = 3.1415926535897932384626433832795;
const int N = 100500;
int n, m;
vector<int> g[N], rg[N];
bool used[N];
int c[N];
vector<int> q;
int minC;
void dfs(int v) {
  for (int i = 0; i < int(int((g[v]).size())); ++i) {
    int u = g[v][i];
    if (!used[u]) {
      c[u] = c[v] + 1;
      q.push_back(u);
      minC = min(minC, c[u]);
      used[u] = true;
      dfs(u);
    }
  }
  for (int i = 0; i < int(int((rg[v]).size())); ++i) {
    int u = rg[v][i];
    if (!used[u]) {
      c[u] = c[v] - 1;
      q.push_back(u);
      minC = min(minC, c[u]);
      used[u] = true;
      dfs(u);
    }
  }
}
bool check(int k) {
  for (int v = 0; v < int(n); ++v)
    for (int j = 0; j < int(int((g[v]).size())); ++j) {
      int u = g[v][j];
      if ((c[v] + 1) % k != c[u] % k) return false;
    }
  return true;
}
int ans = 1;
void update(int k) {
  if (k > ans && check(k)) ans = k;
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < int(m); ++i) {
    int x, y;
    scanf("%d %d", &x, &y);
    x--;
    y--;
    if (x == y) {
      puts("1");
      return 0;
    }
    g[x].push_back(y);
    rg[y].push_back(x);
  }
  for (int i = 0; i < int(n); ++i) {
    sort((g[i]).begin(), (g[i]).end());
    g[i].erase(unique((g[i]).begin(), (g[i]).end()), g[i].end());
  }
  memset(c, -1, sizeof(c));
  for (int i = int(n) - 1; i >= 0; --i) {
    int v = i;
    if (!used[v]) {
      c[v] = 0;
      q.clear();
      used[v] = true;
      q.push_back(v);
      minC = 0;
      dfs(v);
      for (int i = 0; i < int(int((q).size())); ++i) c[q[i]] -= minC;
    }
  }
  for (int v = 0; v < int(n); ++v) {
    for (int i = 0; i < int(int((g[v]).size())); ++i) {
      int u = g[v][i];
      if (c[v] + 1 != c[u]) {
        cerr << v << " " << u << " " << c[v] << " " << c[u] << endl;
        int d = abs(c[v] + 1 - c[u]);
        for (int i = 1; i * i <= d; ++i) {
          if (d % i == 0) {
            update(i);
            update(d / i);
          }
        }
        cout << ans << endl;
        return 0;
      }
    }
  }
  cout << n << endl;
  return 0;
}
