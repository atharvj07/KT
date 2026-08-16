#include <bits/stdc++.h>
using namespace std;
int n, m, j, k, i, l;
int Sp[505][505];
int x, y, z;
vector<pair<pair<int, int>, int> > V;
int W[505][505];
int main() {
  scanf("%d %d", &n, &m);
  for (i = 1; i <= n; i++)
    for (j = 1; j <= n; j++) Sp[i][j] = INT_MAX / 2;
  for (i = 1; i <= m; i++) {
    scanf("%d %d %d", &x, &y, &z);
    Sp[x][y] = z;
    Sp[y][x] = z;
    V.push_back(make_pair(make_pair(x, y), z));
  }
  for (i = 1; i <= n; i++) Sp[i][i] = 0;
  for (k = 1; k <= n; k++)
    for (i = 1; i <= n; i++)
      for (j = 1; j <= n; j++) Sp[i][j] = min(Sp[i][j], Sp[i][k] + Sp[k][j]);
  for (i = 1; i <= n; i++)
    for (j = 0; j < V.size(); j++) {
      if (Sp[i][V[j].first.first] + V[j].second == Sp[i][V[j].first.second])
        W[i][V[j].first.second]++;
      if (Sp[i][V[j].first.second] + V[j].second == Sp[i][V[j].first.first])
        W[i][V[j].first.first]++;
    }
  int ans = 0;
  for (i = 1; i <= n; i++)
    for (j = i + 1; j <= n; j++) {
      ans = 0;
      for (k = 1; k <= n; k++)
        if (Sp[i][k] + Sp[k][j] == Sp[i][j]) ans += W[i][k];
      cout << ans << ' ';
    }
  return 0;
}
