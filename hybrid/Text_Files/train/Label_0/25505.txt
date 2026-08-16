#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
const long long infLL = 0x3f3f3f3f3f3f3f3fLL;
const int maxn = 2000 + 5;
int n, m, k;
char g[maxn][maxn];
int x[maxn], y[maxn];
int up[maxn][maxn], down[maxn][maxn];
int cur, ret[maxn];
void update(int c) {
  for (int i = 0; i < (n); ++i)
    up[i][c] = (g[i][c] == '.' ? (i ? up[i - 1][c] : 0) + 1 : 0);
  for (int i = n - 1; i >= 0; --i)
    down[i][c] = (g[i][c] == '.' ? (i < n - 1 ? down[i + 1][c] : 0) + 1 : 0);
}
void push(deque<int> &deq, int v) {
  while (!deq.empty() && deq.back() > v) deq.pop_back();
  deq.push_back(v);
}
void pop(deque<int> &deq, int v) {
  if (v == deq.front()) deq.pop_front();
}
bool check(int r, int d) {
  if (d > n || d > m) return false;
  deque<int> deq1, deq2;
  for (int j = 0; j < (m); ++j) {
    push(deq1, up[r][j]);
    push(deq2, down[r][j]);
    if (j >= d - 1) {
      if (deq1.front() + deq2.front() - 1 >= d) return true;
      pop(deq1, up[r][j - d + 1]);
      pop(deq2, down[r][j - d + 1]);
    }
  }
  return false;
}
int main() {
  scanf("%d%d%d", &n, &m, &k);
  for (int i = 0; i < (n); ++i) scanf("%s", g[i]);
  for (int i = 0; i < (k); ++i) {
    scanf("%d%d", &x[i], &y[i]);
    --x[i], --y[i];
    g[x[i]][y[i]] = 'X';
  }
  for (int j = 0; j < (m); ++j) update(j);
  for (int i = 0; i < (n); ++i)
    while (check(i, cur + 1)) ++cur;
  for (int i = k - 1; i >= 0; --i) {
    ret[i] = cur;
    g[x[i]][y[i]] = '.';
    update(y[i]);
    while (check(x[i], cur + 1)) ++cur;
  }
  for (int i = 0; i < (k); ++i) printf("%d\n", ret[i]);
  return 0;
}
