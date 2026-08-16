#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m, t = 0;
  scanf("%d%d", &n, &m);
  vector<vector<int>> e(n + 1), l(n + 1);
  for (int i = 0; i < m; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    e[u].push_back(v);
    e[v].push_back(u);
  }
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%d", &x);
    l[i].resize(x);
    for (int j = 0; j < x; j++) {
      scanf("%d", &l[i][j]);
      t = max(t, l[i][j]);
    }
  }
  vector<int> T(n + 1), A(t + 1);
  for (int cnt = 0; cnt < m;) {
    cnt = 0;
    for (int i = 1; i <= n; i++) T[i] = l[i][rand() % l[i].size()];
    for (int i = 1; i <= t; i++) A[i] = rand() & 1;
    for (int u = 1; u <= n; u++)
      for (int v : e[u])
        if (A[T[u]] != A[T[v]]) cnt++;
  }
  for (int i = 1; i <= n; i++) printf(i == n ? "%d\n" : "%d ", T[i]);
  for (int i = 1; i <= t; i++) printf(i == t ? "%d\n" : "%d ", A[i] + 1);
}
