#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100000 + 86;
vector<int> e[MAXN];
vector<pair<int, int> > s[MAXN];
int l[MAXN], r[MAXN];
int t, c[MAXN];
int n, q;
struct seg_tree {
  int nz[MAXN << 2], x[MAXN << 2];
  void init() {
    memset(nz, 0, sizeof(nz));
    memset(x, 0, sizeof(x));
  }
  void update(int r, int L, int R) {
    if (x[r])
      nz[r] = R - L + 1;
    else if (L >= R)
      nz[r] = 0;
    else
      nz[r] = nz[((r) << 1)] + nz[(((r) << 1) ^ 1)];
  }
  void add(int r, int L, int R, const int a, const int b, const int off) {
    if (a <= L && R <= b) {
      x[r] += off;
      update(r, L, R);
      return;
    }
    int M = ((L) + (R)) >> 1;
    if (a <= M) add(((r) << 1), L, M, a, b, off);
    if (b > M) add((((r) << 1) ^ 1), M + 1, R, a, b, off);
    update(r, L, R);
  }
  int sum() { return max(0, nz[1] - 1); }
  void info(int r, int L, int R) {
    printf("%d [%d, %d] x: %d, nz: %d\n", r, L, R, x[r], nz[r]);
    if (L >= R) return;
    int M = ((L) + (R)) >> 1;
    info(((r) << 1), L, M);
    info((((r) << 1) ^ 1), M + 1, R);
  }
} T;
int dfs(int r, int p) {
  l[r] = ::r[r] = t;
  for (int i = 0; i < e[r].size(); ++i)
    if (e[r][i] != p) ++t, ::r[r] = max(::r[r], dfs(e[r][i], r));
  return ::r[r];
}
void gao(int r, int p) {
  for (int i = 0; i < s[r].size(); ++i)
    T.add(1, 0, n - 1, s[r][i].first, s[r][i].second, 1);
  c[r] = T.sum();
  for (int i = 0; i < e[r].size(); ++i)
    if (e[r][i] != p) gao(e[r][i], r);
  for (int i = 0; i < s[r].size(); ++i)
    T.add(1, 0, n - 1, s[r][i].first, s[r][i].second, -1);
}
int main() {
  scanf("%d%d", &n, &q);
  for (int i = 1, a, b; i < n; ++i) {
    scanf("%d%d", &a, &b), --a, --b;
    e[a].push_back(b), e[b].push_back(a);
  }
  dfs(0, -1);
  for (int a, b; q--;) {
    scanf("%d%d", &a, &b), --a, --b;
    s[a].push_back(make_pair((l[a]), (r[a]))),
        s[a].push_back(make_pair((l[b]), (r[b])));
    s[b].push_back(make_pair((l[a]), (r[a]))),
        s[b].push_back(make_pair((l[b]), (r[b])));
  }
  gao(0, -1);
  for (int i = 0; i < n; ++i) printf("%d%s", c[i], i == n - 1 ? "\n" : " ");
  return 0;
}
