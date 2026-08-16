#include <bits/stdc++.h>
using namespace std;
const int N = 100005, M = 20;
int n, m, dep[N], f[N], mx[N], tp[N], lg[N], st[2][N][M];
bool vis[N];
vector<int> v[N], l{0};
void dfs(int pos, int fa) {
  dep[pos] = dep[fa] + 1;
  f[pos] = fa;
  for (auto &i : v[pos])
    if (i != fa) dfs(i, pos);
}
void dfs2(int pos, int fa, int top) {
  tp[pos] = top;
  dep[pos] = dep[fa] + 1;
  mx[top] = max(mx[top], dep[pos]);
  for (auto &i : v[pos])
    if (i != fa && !vis[i]) dfs2(i, pos, top);
}
int query(int k, int l, int r) {
  if (l > r) return INT_MIN / 4;
  int kk = lg[r - l + 1];
  return max(st[k][l][kk], st[k][r - (1 << kk) + 1][kk]);
}
int main() {
  ios::sync_with_stdio(false);
  cin >> n;
  for (int i = 2; i < N; i++) lg[i] = lg[i >> 1] + 1;
  int t1, t2;
  for (int i = 1; i < n; i++)
    cin >> t1 >> t2, v[t1].push_back(t2), v[t2].push_back(t1);
  cin >> m;
  dfs(1, 0);
  t1 = max_element(dep + 1, dep + n + 1) - dep;
  dfs(t1, 0);
  t2 = max_element(dep + 1, dep + n + 1) - dep;
  while (t2) vis[t2] = 1, l.push_back(t2), t2 = f[t2];
  int sz = l.size() - 1;
  dep[0] = -1;
  for (int i = 1; i <= sz; i++)
    dfs2(l[i], 0, i), st[0][i][0] = mx[i] + i, st[1][i][0] = mx[i] - i;
  for (int k = 0; k < 2; k++)
    for (int i = 1; i < M; i++)
      for (int j = 1; j + (1 << i) - 1 <= sz; j++)
        st[k][j][i] = max(st[k][j][i - 1], st[k][j + (1 << (i - 1))][i - 1]);
  while (m--) {
    int ans;
    cin >> t1 >> t2;
    if (tp[t1] > tp[t2]) swap(t1, t2);
    if (tp[t1] == tp[t2]) {
      ans = min(dep[t1], dep[t2]) + max(tp[t1] - 1, sz - tp[t1]);
      cout << ans << endl;
      continue;
    }
    int mid = tp[t1] + tp[t2] - dep[t1] + dep[t2];
    if (tp[t1] * 2 >= mid)
      ans = dep[t2] + max(tp[t2] - 1, sz - tp[t2]);
    else if (tp[t2] * 2 <= mid)
      ans = dep[t1] + max(tp[t1] - 1, sz - tp[t1]);
    else
      ans =
          max(max(query(0, tp[t1] + 1, mid / 2) - tp[t1], tp[t1] - 1) + dep[t1],
              max(sz - tp[t2], query(1, mid / 2 + 1, tp[t2] - 1) + tp[t2]) +
                  dep[t2]);
    cout << ans << endl;
  }
  return 0;
}
