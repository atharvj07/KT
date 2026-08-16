#include <bits/stdc++.h>
using namespace std;
int inline read() {
  int num = 0, neg = 1;
  char c = getchar();
  while (!isdigit(c)) {
    if (c == '-') neg = -1;
    c = getchar();
  }
  while (isdigit(c)) {
    num = (num << 3) + (num << 1) + c - '0';
    c = getchar();
  }
  return num * neg;
}
const int maxn = 100010, mod = 998244353;
int n, m;
vector<pair<int, int> > g[maxn];
int flg, vis[maxn], L[maxn], tot;
double ans[maxn], a[maxn], b[maxn];
void dfs(int x, int fa, int op) {
  if (flg) return;
  if (op) L[++tot] = x;
  for (int i = 0; i < g[x].size(); i++) {
    int v = g[x][i].first, w = g[x][i].second;
    if (v == fa) continue;
    double A = -a[x], B = w - b[x];
    if (vis[v]) {
      if (A == a[v] && B != b[v])
        flg = 1;
      else if (A * a[v] == -1) {
        b[v] = (B - b[v]) / (a[v] - A) * A + B;
        a[v] = 0;
      }
    } else {
      vis[v] = 1;
      a[v] = A;
      b[v] = B;
      dfs(v, x, op);
    }
  }
}
double A[maxn], B[maxn];
int cnt, id[maxn];
int main() {
  n = read();
  m = read();
  for (int i = 1; i <= m; i++) {
    int x = read(), y = read(), d = read();
    g[x].push_back(make_pair(y, d));
    g[y].push_back(make_pair(x, d));
  }
  for (int i = 1; i <= n; i++)
    if (!vis[i]) {
      a[i] = 1;
      b[i] = 0;
      vis[i] = 1;
      tot = 0;
      dfs(i, 0, 1);
      for (int j = 1; j <= tot; j++)
        if (!a[L[j]]) {
          for (int k = 1; k <= tot; k++) vis[L[k]] = 0;
          vis[L[j]] = 1;
          dfs(L[j], 0, 0);
          break;
        }
      if (flg) {
        cout << "NO";
        break;
      } else {
        cnt = 0;
        for (int j = 1; j <= tot; j++)
          if (abs(a[L[j]]) == 0)
            ans[L[j]] = b[L[j]];
          else
            A[++cnt] = a[L[j]], B[cnt] = b[L[j]], id[cnt] = L[j];
        for (int j = 1; j <= cnt; j++)
          if (A[j] == 1) B[j] = -B[j];
        sort(B + 1, B + cnt + 1);
        int x = B[cnt / 2 + 1];
        for (int j = 1; j <= tot; j++) ans[L[j]] = a[L[j]] * x + b[L[j]];
      }
    }
  if (!flg) {
    cout << "YES" << endl;
    for (int i = 1; i <= n; i++) printf("%.9lf ", ans[i]);
  }
  return 0;
}
