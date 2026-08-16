#include <bits/stdc++.h>
using namespace std;
vector<int> E[100005];
int sz[100005];
double dp[100005];
void dfs(int x) {
  sz[x] = 1;
  for (int i = 0; i < E[x].size(); i++) {
    int y = E[x][i];
    dfs(y);
    sz[x] += sz[y];
  }
}
void redfs(int x) {
  dp[x]++;
  for (int i = 0; i < E[x].size(); i++) {
    int y = E[x][i];
    dp[y] = dp[x] + (sz[x] - sz[y] - 1) / 2.0;
    redfs(y);
  }
}
int main() {
  int n;
  cin >> n;
  for (int i = 2; i <= n; i++) {
    int f;
    scanf("%d", &f);
    E[f].push_back(i);
  }
  dfs(1);
  redfs(1);
  for (int i = 1; i <= n; i++) printf("%.8lf ", dp[i]);
  puts("");
  return 0;
}
