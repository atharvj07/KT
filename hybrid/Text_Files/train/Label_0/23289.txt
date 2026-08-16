#include <bits/stdc++.h>
using namespace std;
const int amn = 1e5 + 5;
int n, ans, idx[amn], root;
vector<int> eg[amn];
struct node {
  int i, val;
} cnt[amn];
bool cmp(node a, node b) {
  if (a.val == b.val) return a.i < b.i;
  return a.val > b.val;
}
void dfs(int rt) {
  if (eg[rt].size() < 2) {
    ans = rt;
    return;
  }
  for (int i = 0; i < eg[rt].size(); i++) {
    int v = eg[rt][i];
    if (v == idx[rt] || v == rt) continue;
    idx[v] = rt;
    dfs(v);
  }
}
int main() {
  scanf("%d", &n);
  int x, y;
  for (int i = 1; i <= n - 1; i++) {
    scanf("%d%d", &x, &y);
    eg[x].push_back(y);
    eg[y].push_back(x);
  }
  for (int i = 1; i <= n; i++) {
    cnt[i].val = eg[i].size();
    cnt[i].i = i;
  }
  sort(cnt + 1, cnt + 1 + n, cmp);
  if (cnt[1].val > 2 && cnt[2].val > 2) {
    printf("No\n");
  } else {
    if (cnt[1].val > 2)
      root = cnt[1].i;
    else {
      for (int i = 1; i <= n; i++) {
        if (cnt[i].val < 2) {
          root = cnt[i].i;
          break;
        }
      }
    }
    memset(idx, 0, sizeof idx);
    printf("Yes\n%d\n", eg[root].size());
    int st;
    for (int i = n; i >= 1; i--) {
      if (cnt[i].val > 1) break;
      st = i;
    }
    for (int i = st; i <= n; i++) {
      if (cnt[i].i == root) continue;
      printf("%d ", root);
      printf("%d\n", cnt[i].i);
    }
  }
}
