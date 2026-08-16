#include <bits/stdc++.h>
using namespace std;
const int inf = 987654321;
int N, K, R;
vector<int> A;
vector<vector<int> > adj;
vector<int> sz;
void dfs0(int now, int bf) {
  sz[now] = 1;
  for (int i = 0; i < adj[now].size(); i++) {
    int nxt = adj[now][i];
    if (nxt == bf) continue;
    dfs0(nxt, now);
    sz[now] += sz[nxt];
  }
}
void get_sz() {
  sz = vector<int>(N, 0);
  dfs0(R, -1);
}
int ans, X;
vector<int> xcnt;
void dfs(int now, int bf) {
  xcnt[now] = A[now] < X ? 1 : 0;
  for (int i = 0; i < adj[now].size(); i++) {
    int nxt = adj[now][i];
    if (nxt == bf) continue;
    dfs(nxt, now);
    xcnt[now] += xcnt[nxt];
  }
}
vector<int> dp, pos, alt;
void dfs2(int now, int bf) {
  if (A[now] < X)
    dp[now] = 0;
  else
    dp[now] = 1;
  int maxi = 0, maxi2 = 0, maxp = -1, maxp2 = -1;
  for (int i = 0; i < adj[now].size(); i++) {
    int nxt = adj[now][i];
    if (nxt == bf) continue;
    dfs2(nxt, now);
    if (A[now] < X) continue;
    if (xcnt[nxt] == 0)
      dp[now] += sz[nxt];
    else {
      if (maxi < dp[nxt]) {
        maxi2 = maxi;
        maxp2 = maxp;
        maxi = dp[nxt];
        maxp = nxt;
      } else if (maxi2 < dp[nxt]) {
        maxi2 = dp[nxt];
        maxp2 = nxt;
      }
    }
  }
  if (A[now] >= X) dp[now] += maxi;
  pos[now] = maxp;
  alt[now] = maxp2;
}
int ok;
vector<int> dp2;
void dfs3(int now, int bf) {
  if (ok) return;
  if (dp[now] >= K) {
    ok = 1;
    return;
  }
  if (now != R && A[bf] >= X && A[now] >= X) {
    if (A[bf] < X)
      dp2[now] = 1;
    else if (now == pos[bf]) {
      int maxi = alt[bf] == -1 ? 0 : dp[alt[bf]];
      if (dp2[bf] == N - sz[bf] + 1) {
        dp2[now] += dp2[bf] - 1;
      } else
        maxi = max(maxi, dp2[bf] - 1);
      dp2[now] += 1 + dp[bf] - dp[now] + maxi;
    } else {
      if (xcnt[now] == 0) {
        int maxi = pos[bf] == -1 ? 0 : dp[pos[bf]];
        dp2[now] -= maxi;
        if (dp2[bf] == N - sz[bf] + 1) {
          dp2[now] += dp2[bf] - 1;
        } else
          maxi = max(maxi, dp2[bf] - 1);
        dp2[now] += 1 + dp[bf] - dp[now] + maxi;
      } else {
        int maxi = pos[bf] == -1 ? 0 : dp[pos[bf]];
        dp2[now] -= maxi;
        if (dp2[bf] == N - sz[bf] + 1) {
          dp2[now] += dp2[bf] - 1;
        } else
          maxi = max(maxi, dp2[bf] - 1);
        dp2[now] += 1 + dp[bf] + maxi;
      }
    }
  }
  if (dp2[now] >= K) {
    ok = 1;
    return;
  }
  for (int i = 0; i < adj[now].size(); i++) {
    int nxt = adj[now][i];
    if (nxt == bf) continue;
    dfs3(nxt, now);
  }
}
bool f(int x) {
  if (A[R] < x) return false;
  X = x;
  xcnt = vector<int>(N, 0);
  dfs(R, -1);
  dp = pos = alt = vector<int>(N, 0);
  dfs2(R, -1);
  ok = 0;
  dp2 = vector<int>(N, 0);
  dfs3(R, -1);
  return ok;
}
void solve() {
  int s = 1, e = 1000002;
  while (s <= e) {
    int m = (s + e) >> 1;
    if (f(m)) {
      ans = m;
      s = m + 1;
    } else
      e = m - 1;
  }
}
int main() {
  scanf("%d %d", &N, &K);
  A.resize(N);
  int maxi = -inf;
  for (int i = 0; i < N; i++) {
    scanf("%d", &A[i]);
    if (maxi < A[i]) {
      maxi = A[i];
      R = i;
    }
  }
  adj.resize(N);
  for (int i = 0; i < N - 1; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    u--;
    v--;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  get_sz();
  solve();
  printf("%d", ans);
}
