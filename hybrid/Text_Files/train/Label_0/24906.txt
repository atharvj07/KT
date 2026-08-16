#include <bits/stdc++.h>
using namespace std;
int N, L, R, C, s[1000005], l[1000005], f[1000005], d[1000005], p[1000005],
    q[1000005];
string S = "", a[1000005];
vector<int> e[1000005];
void init() {
  scanf("%d%d%d", &N, &R, &C), L = log(N) / log(2);
  for (int i = 1; i <= N; i++)
    cin >> a[i], S += a[i] + " ", l[i] = a[i].size() + 1;
  for (int i = 1; i <= N; i++) s[i] = s[i - 1] + l[i];
}
void dfs(int u, int k) {
  p[u] = k;
  for (int v : e[u]) q[u] = v, dfs(v, d[u] - d[k] < R ? k : q[k]);
}
void doit() {
  int ans = 0, o;
  for (int i = 1, j = 0; i <= N; i++) {
    for (; j < N && s[j + 1] - s[i - 1] - 1 <= C; j++)
      ;
    if (j >= i) f[i] = j + 1, e[j + 1].push_back(i);
  }
  for (int i = N; i; i--) d[i] = d[f[i]] + 1;
  for (int i = 1; i <= N + 1; i++)
    if (!f[i]) dfs(i, i);
  for (int i = 1; i <= N; i++)
    if (p[i] - i > ans) ans = p[i] - i, o = i;
  for (int i = o; i < o + ans; i = f[i])
    for (int j = i; j < f[i]; j++)
      printf("%s%c", a[j].c_str(), j == f[i] - 1 ? '\n' : ' ');
}
int main() {
  init();
  doit();
  return 0;
}
