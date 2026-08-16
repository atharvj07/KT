#include <bits/stdc++.h>
using namespace std;
int i, j, k, n, m, u, ty;
int f[100010][20], s[100010][30];
long long h[100010], g[100010], sum, ans, an, v[100010];
char p[100010];
inline long long get(int l, int r) { return h[r] - h[l - 1] * g[r - l + 1]; }
inline int cal(int l, int r, int x) { return s[r][x] - s[l - 1][x]; }
void dfs(int l, int r, long long hash) {
  long long len = r - l + 1, A = r + 1;
  an += len * len;
  if (A + len <= n && hash == get(A + 1, A + len) &&
      cal(A + 1, A + len, p[A] - 'a') == 0)
    dfs(l, A + len, hash * g[len + 1] + get(A, A + len));
  A = l - 1;
  if (A - len > 0 && get(A - len, A - 1) == hash &&
      cal(A - len, A - 1, p[A] - 'a') == 0)
    dfs(A - len, r, get(A - len, A) * g[len] + hash);
}
inline void prepare() {
  g[0] = 1;
  for (i = 1; i <= n; i++)
    h[i] = h[i - 1] * 10007 + p[i], g[i] = g[i - 1] * 10007;
  for (i = 1; i <= n; i++) {
    memcpy(s[i], s[i - 1], sizeof(s[i]));
    s[i][p[i] - 'a']++;
  }
  for (j = 1, k = 0; j <= n; k++, j = j * 2 + 1)
    for (u = 1; u <= n - j + 1; u++) {
      int r = u + j - 1, A = u + j / 2;
      if (!k || get(u, A - 1) == get(A + 1, r) && cal(u, r, p[A] - 'a') == 1 &&
                    f[u][k - 1] && f[A + 1][k - 1]) {
        long long s = (long long)j * j;
        sum += s;
        v[u] += s;
        v[r + 1] -= s;
        f[u][k] = 1;
      }
    }
  for (i = 1; i <= n; i++) v[i] += v[i - 1];
}
inline void work() {
  ans = sum;
  for (i = 1; i <= n; i++) {
    long long res = sum - v[i];
    for (u = 0; u <= 25; u++) {
      an = res;
      for (k = 0, j = 0;; j = j * 2 + 1, k++) {
        int l = i - j, r = i + j;
        if (l < 1 || r > n) break;
        if (!k || get(l, i - 1) == get(i + 1, r) &&
                      cal(l, i - 1, u) + cal(i + 1, r, u) == 0 && f[l][k - 1] &&
                      f[i + 1][k - 1])
          dfs(l, r,
              get(l, i - 1) * g[j + 1] + (u + 'a') * g[j] + get(i + 1, r));
        else
          break;
      }
      ans = max(ans, an);
    }
  }
}
int main() {
  scanf("%s", p + 1);
  n = strlen(p + 1);
  prepare();
  work();
  printf("%I64u\n", ans);
  return 0;
}
