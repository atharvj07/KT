#include <bits/stdc++.h>
const double eps = 1e-9;
const int oo = 1000000000;
const double E = 2.7182818284590452353602874713527;
const double pi = 3.1415926535897932384626433832795;
using namespace std;
struct case1 {
  int son[26];
  int v, f;
} p[50002];
int f[50002][101];
string a[101];
int n, k;
void dfs(int now, int dis) {
  for (int i = 0; i < 26; i++)
    if (p[now].son[i]) {
      int t = p[now].son[i];
      dfs(t, dis + 1);
      for (int j = min(p[now].v, k); j; j--)
        for (int a = 0; a <= min(j, p[t].v); a++)
          f[now][j] =
              max(f[now][j], f[now][j - a] + f[t][a] + (j - a) * dis * a);
    }
  for (int i = min(p[now].v, k); i; i--)
    for (int j = 1; j <= min(p[now].f, i); j++)
      f[now][i] =
          max(f[now][i], f[now][i - j] + dis * ((i - j) * j + j * (j - 1) / 2));
}
int main() {
  int tot = 1;
  cin >> n >> k;
  for (int i = 1; i <= n; i++) {
    int now = 1;
    cin >> a[i];
    for (int j = 0; j < a[i].size(); j++) {
      p[now].v++;
      if (!p[now].son[a[i][j] - 'a']) p[now].son[a[i][j] - 'a'] = ++tot;
      now = p[now].son[a[i][j] - 'a'];
    }
    p[now].v++;
    p[now].f++;
  }
  dfs(1, 0);
  cout << f[1][k] << endl;
  return 0;
}
