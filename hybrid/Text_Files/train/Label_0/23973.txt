#include <bits/stdc++.h>
using namespace std;
const long long INF = 0x3f3f3f3f;
const int N = 3e5 + 100;
bool debug = false;
vector<pair<int, int> > vc[N];
set<pair<long long, int> > gg1[N], gg2[N], gg3[N];
set<pair<long long, int> >::iterator iit;
int in[N], vis[N], ord[N];
long long dp[N][2], sum[N];
bool cmp(pair<int, int> a, pair<int, int> b) {
  return in[a.first] > in[b.first];
}
bool cmp1(int a, int b) { return in[a] > in[b]; }
void dfs(int o, int u, int op) {
  vis[o] = op;
  dp[o][1] = 0;
  while (!vc[o].empty()) {
    pair<int, int> it = vc[o].back();
    if (in[it.first] != op) break;
    gg2[o].insert({it.second, it.first});
    sum[o] += it.second;
    vc[o].pop_back();
  }
  while (gg2[o].size() > in[o] - op) {
    if (gg2[o].rbegin()->first < 0) break;
    sum[o] -= gg2[o].rbegin()->first;
    gg2[o].erase(--gg2[o].end());
  }
  for (auto it : vc[o]) {
    if (vis[it.first] == op) continue;
    dfs(it.first, o, op);
    dp[o][1] += dp[it.first][0];
    long long now = min(dp[it.first][1] - dp[it.first][0], 0ll) + it.second;
    gg1[o].insert({now, it.first});
    gg2[o].insert({now, it.first});
    sum[o] += now;
  }
  while (gg2[o].size() > in[o] - op) {
    if (gg2[o].rbegin()->first < 0) break;
    sum[o] -= gg2[o].rbegin()->first;
    gg3[o].insert(*(gg2[o].rbegin()));
    gg2[o].erase(--gg2[o].end());
  }
  dp[o][0] = dp[o][1] + sum[o];
  dp[o][1] = dp[o][0] - gg2[o].rbegin()->first;
  for (auto it : gg3[o]) {
    gg2[o].insert(it);
    sum[o] += it.first;
  }
  for (auto it : gg1[o]) {
    gg2[o].erase(it);
    sum[o] -= it.first;
  }
  gg1[o].clear(), gg3[o].clear();
}
vector<long long> ret;
int main() {
  int n;
  scanf("%d", &n);
  long long ans = 0;
  for (int i = 1; i <= n; ++i) ord[i] = i;
  for (int i = 1, u, v, x; i < n; ++i) {
    scanf("%d %d %d", &u, &v, &x);
    vc[u].emplace_back(v, x);
    vc[v].emplace_back(u, x);
    in[u]++, in[v]++;
    ans += x;
  }
  sort(ord + 1, ord + n + 1, cmp1);
  for (int i = 1; i <= n; ++i) sort(vc[i].begin(), vc[i].end(), cmp);
  ret.push_back(ans);
  int cnt = 0;
  for (int i = 1; i < n; ++i) {
    ans = 0;
    for (int j = 1; j <= n; ++j) {
      if (in[ord[j]] <= i) break;
      if (vis[ord[j]] != i) {
        dfs(ord[j], 0, i);
        ans += dp[ord[j]][0];
      }
    }
    ret.push_back(ans);
  }
  for (auto it : ret) printf("%I64d ", it);
  return 0;
}
