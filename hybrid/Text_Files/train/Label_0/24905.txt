#include <bits/stdc++.h>
using namespace std;
template <class T>
inline void gmin(T &a, T b) {
  if (a > b) a = b;
}
template <class T>
inline void gmax(T &a, T b) {
  if (a < b) a = b;
}
inline int sign(const double &a) { return a > 1e-9 ? 1 : (a < -1e-9 ? -1 : 0); }
struct Initializer {
  Initializer() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
  }
  ~Initializer() {}
} initializer;
char st[10001000];
int col[10001000];
vector<int> a;
vector<vector<int> > to;
vector<int> sum(1), opt(1);
vector<int> u(1), v;
int ans = -1, n, c, r, l, p, q;
void dfs(int first) {
  sum.push_back(sum.back() + a[first]);
  int tmp = sum.back() - sum[max(0, int(sum.size()) - 1 - r)];
  if (ans < tmp && tmp > 0) {
    ans = tmp;
    p = max(0, int(sum.size()) - 1 - r) + 1;
    q = int(sum.size()) - 1;
  }
  for (int i = 0; i <= int(to[first].size()) - 1; i++) {
    dfs(to[first][i]);
  }
  sum.pop_back();
}
void prt(int first, int second) {
  string ss;
  for (int i = first; i <= l - 1; i++) {
    if (st[i] == ' ') continue;
    if (i > first) putchar(' ');
    int j = i;
    for (; j + 1 < l && st[j + 1] != ' '; j++)
      ;
    for (int k = i; k <= j; k++) putchar(st[k]);
    second--;
    if (second == 0) return;
    i = j;
  }
}
void dfs2(int first) {
  sum.push_back(sum.back() + a[first]);
  opt.push_back(first);
  int tmp = sum.back() - sum[max(0, int(sum.size()) - 1 - r)];
  if (ans == tmp) {
    for (int i = q; i >= p; i--) {
      prt(u[opt[i]], a[opt[i]]);
      putchar(10);
    }
    exit(0);
  }
  for (int i = 0; i <= int(to[first].size()) - 1; i++) {
    dfs2(to[first][i]);
  }
  sum.pop_back();
  opt.pop_back();
}
int main() {
  scanf("%d%d%d\n", &n, &r, &c);
  gets(st);
  l = strlen(st);
  st[l] = ' ';
  st[l + 1] = 0;
  l++;
  for (int i = 0; i <= l - 1; i++) {
    col[i] = int(u.size());
    if (st[i + 1] == ' ') {
      v.push_back(i);
      u.push_back(i + 2);
    }
  }
  if (int(u.size()) > int(v.size())) u.pop_back();
  for (int i = 0; i <= n - 1; i++) {
    if (u[i] + c <= l - 1)
      a.push_back(col[u[i] + c] - col[u[i]]);
    else
      a.push_back(n + 1 - col[u[i]]);
  }
  vector<int> din(n + 1);
  to.resize(n + 1);
  for (int i = 0; i <= n - 1; i++) {
    if (i + a[i] <= n - 1) {
      if (a[i] == 0 || a[i + a[i]] == 0) continue;
      to[i + a[i]].push_back(i);
      din[i]++;
    }
  }
  for (int i = 0; i <= n - 1; i++)
    if (din[i] == 0) dfs(i);
  for (int i = 0; i <= n - 1; i++)
    if (din[i] == 0) dfs2(i);
  return 0;
}
