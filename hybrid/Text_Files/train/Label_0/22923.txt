#include <bits/stdc++.h>
using namespace std;
vector<vector<int> > adj(100001);
int m, subtreeSize[100001];
long long dp[100001][202], s[202][202], c[202], fact[202];
void DFS(int i, int p = 0) {
  dp[i][0] = 2;
  subtreeSize[i] = 1;
  for (int j : adj[i]) {
    if (j == p) {
      continue;
    }
    DFS(j, i);
    for (int z = min(m, subtreeSize[i] + subtreeSize[j] - 1); z > -1; --z) {
      long long val = 0;
      for (int x = min(z, subtreeSize[i] - 1), y = z - x;
           x > -1 && y <= subtreeSize[j]; --x, ++y) {
        val = (val + dp[i][x] * (dp[j][y] +
                                 ((y > 0) ? (dp[j][y - 1] - (y == 1)) : 0ll))) %
              1000000007;
      }
      dp[i][z] = val;
    }
    subtreeSize[i] += subtreeSize[j];
  }
  for (int x = min(m, subtreeSize[i]); x > -1; --x) {
    c[x] = (c[x] + dp[i][x]) % 1000000007;
  }
  for (int x = min(m, subtreeSize[i]); p != 0 && x > -1; --x) {
    c[x] = (c[x] - (dp[i][x] + ((x > 0) ? (dp[i][x - 1] - (x == 1)) : 0ll))) %
           1000000007;
  }
}
void Initialise() {
  s[1][1] = 1;
  for (int i = 2; i <= m; ++i) {
    for (int j = 1; j <= i; ++j) {
      s[i][j] = (s[i - 1][j - 1] + j * s[i - 1][j]) % 1000000007;
    }
  }
  fact[0] = 1;
  for (int i = 1; i <= m; ++i) {
    fact[i] = (i * fact[i - 1]) % 1000000007;
  }
}
int main() {
  int n;
  scanf("%d%d", &n, &m);
  for (int x = 1; x < n; ++x) {
    int i, j;
    scanf("%d%d", &i, &j);
    adj[i].push_back(j);
    adj[j].push_back(i);
  }
  Initialise();
  DFS(1);
  long long ans = 0;
  for (int x = 1; x <= m; ++x) {
    long long ansx = (s[m][x] * fact[x]) % 1000000007;
    ansx = (ansx * c[x]) % 1000000007;
    ans = (ans + 1000000007 + ansx) % 1000000007;
  }
  printf("%lld\n", ans);
  return 0;
}
