#include <bits/stdc++.h>
#pragma warning(disable : 4996)
#pragma GCC optimize(3)
template <typename T>
T min(T x, T y) {
  return x < y ? x : y;
}
template <typename T>
T max(T x, T y) {
  return x > y ? x : y;
};
const int INF = 1000000000;
const int MAXN = 100005;
const int B = 500;
int N, M, Q;
int low[MAXN];
std::vector<int> V[MAXN], ID[MAXN], up[MAXN];
int ans[MAXN];
int f[MAXN];
void solve() {
  static int mx[MAXN][25];
  for (int l = 1, r; l <= N; l = r + 1) {
    r = min(l + B - 1, N);
    for (int i = l; i <= r; i++) {
      f[i] = i;
      for (int j = l; j <= i; j++)
        if (f[j] >= low[i] && low[i] >= j) f[j] = i;
      for (int j = 0; j < V[i].size(); j++) {
        if (V[i][j] >= l) {
          ans[ID[i][j]] = f[V[i][j]];
          continue;
        }
        ans[ID[i][j]] = f[V[i][j]];
        for (int k = l; k <= i; k++)
          if (low[k] >= V[i][j] && low[k] <= ans[ID[i][j]]) ans[ID[i][j]] = k;
      }
    }
    memset(mx, 0, sizeof(mx));
    memset(f, 0, sizeof(f));
    for (int i = r; i >= 1; i--) {
      f[i] = i;
      for (int j = 0; j < up[i].size(); j++) {
        if (up[i][j] > r) continue;
        int t = 0;
        while (1 << t <= up[i][j] - i) t++;
        t--;
        f[i] = max(f[i], max(mx[i + 1][t], mx[up[i][j] - (1 << t) + 1][t]));
      }
      mx[i][0] = f[i];
      for (int j = 1; j < 25; j++)
        mx[i][j] = max(mx[i][j - 1], mx[min(r, i + (1 << (j - 1)))][j - 1]);
    }
  }
  for (int i = 1; i <= Q; i++) printf("%d\n", ans[i]);
}
void init() {
  int l, r;
  scanf("%d %d", &N, &M);
  for (int i = 1; i <= M; i++) {
    scanf("%d %d", &l, &r);
    if (l == r) continue;
    low[r] = l;
    up[l].push_back(r);
  }
  scanf("%d", &Q);
  for (int i = 1; i <= Q; i++) {
    scanf("%d %d", &l, &r);
    V[r].push_back(l);
    ID[r].push_back(i);
  }
}
int main() {
  init();
  solve();
  return 0;
}
