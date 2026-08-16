#include <bits/stdc++.h>
using namespace std;
vector<pair<int, int>> adj[100005];
int a[2000 + 10][2000 + 10], b[2000 + 10][2000 + 10];
int m[2000 + 10], color[100005];
int n;
bool Impossible;
bool vs[100005];
void dfs(int u, int currentColor) {
  if (color[u] != -1) {
    if (color[u] != currentColor) {
      Impossible = true;
      return;
    }
  }
  if (vs[u]) return;
  vs[u] = true;
  if (color[u] == -1) color[u] = currentColor;
  for (auto v : adj[u]) {
    if (v.second == 0)
      dfs(v.first, currentColor);
    else
      dfs(v.first, 1 - currentColor);
  }
}
int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < n; j++) a[i][j] = s[j] - '0';
  }
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < n; j++) b[i][j] = s[j] - '0';
  }
  string s;
  cin >> s;
  for (int i = 0; i < n; i++) m[i] = s[i] - '0';
  for (int i = 0; i < 2 * n; i++) color[i] = -1;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) {
      if (a[i][j] == b[i][j]) {
        if (m[i] == m[j] && m[i] == 1) {
          adj[i].push_back({j + n, 0});
          adj[j + n].push_back({i, 0});
        } else {
          if (m[j] == 1 && m[i] == 0) color[i] = 0;
          if (m[j] == 0 && m[i] == 1) color[j + n] = 0;
        }
      } else {
        if (m[i] == m[j] && m[i] == 1) {
          adj[i].push_back({j + n, 1});
          adj[j + n].push_back({i, 1});
        }
        if (m[i] == m[j] && m[i] == 0 && a[i][j] == 0) {
          cout << -1;
          return 0;
        }
        if (m[j] == 1 && m[i] == 0) {
          color[i] = 1;
        }
        if (m[j] == 0 && m[i] == 1) {
          color[j + n] = 1;
        }
      }
    }
  memset(vs, false, sizeof(vs));
  Impossible = false;
  for (int i = 0; i < 2 * n; i++)
    if (color[i] != -1) dfs(i, color[i]);
  for (int i = 0; i < 2 * n; i++)
    if (color[i] == -1) dfs(i, 0);
  if (Impossible) {
    cout << -1;
    return 0;
  }
  int cnt = 0;
  for (int i = 0; i < 2 * n; i++)
    if (color[i] == 1) cnt++;
  cout << cnt << endl;
  for (int i = 0; i < 2 * n; i++)
    if (color[i] == 1) {
      if (i < n)
        cout << "row"
             << " " << i << endl;
      else
        cout << "col"
             << " " << i - n << endl;
    }
}
