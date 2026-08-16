#include <bits/stdc++.h>
using namespace std;
long long int graph[4005][4005];
vector<long long int> v[4005];
long long int n, m;
int main() {
  scanf("%lld", &n);
  scanf("%lld", &m);
  long long int i, a, b, j, k;
  for (i = 0; i < m; i++) {
    scanf("%lld", &a);
    scanf("%lld", &b);
    graph[a][b] = 1;
    graph[b][a] = 1;
    v[a].push_back(b);
    v[b].push_back(a);
  }
  long long int mini = 1000000005;
  for (i = 1; i <= n; i++) {
    if (v[i].size() >= 2) {
      for (j = 0; j < v[i].size(); j++) {
        if (v[v[i][j]].size() >= 2) {
          for (k = 0; k < v[v[i][j]].size(); k++) {
            if (graph[v[v[i][j]][k]][i] == 1) {
              long long int temp =
                  v[i].size() + v[v[i][j]].size() + v[v[v[i][j]][k]].size();
              mini = min(mini, temp);
            }
          }
        }
      }
    }
  }
  if (mini != 1000000005)
    printf("%lld\n", mini - 6);
  else
    printf("-1\n");
  return 0;
}
