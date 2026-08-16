#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5 + 5;
int head[maxn], deg[maxn], ans[maxn], tot = 1;
struct edge {
  int v, nex, id;
  bool f;
} e[maxn << 4];
void add(int u, int v, int id) {
  e[++tot] = {v, head[u], id, 0}, head[u] = tot;
  e[++tot] = {u, head[v], id, 0}, head[v] = tot;
}
struct Q {
  int l, r;
} q[maxn];
vector<int> a;
void euler(int u) {
  for (int &i = head[u]; i; i = e[i].nex) {
    if (e[i].f) continue;
    e[i].f = e[i ^ 1].f = 1;
    int v = e[i].v;
    ans[e[i].id] = (u < v);
    euler(v);
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> q[i].l >> q[i].r;
    q[i].r++;
    a.push_back(q[i].l);
    a.push_back(q[i].r);
  }
  sort(a.begin(), a.end());
  a.erase(unique(a.begin(), a.end()), a.end());
  for (int i = 0; i < n; i++) {
    q[i].l = lower_bound(a.begin(), a.end(), q[i].l) - a.begin();
    q[i].r = lower_bound(a.begin(), a.end(), q[i].r) - a.begin();
    deg[q[i].l]++, deg[q[i].r]++;
    add(q[i].l, q[i].r, i);
  }
  int len = a.size(), last = -1;
  for (int i = 0; i < len; i++) {
    if (deg[i] & 1) {
      if (last == -1)
        last = i;
      else
        add(last, i, n + 3), last = -1;
    }
  }
  for (int i = 0; i < len; i++)
    if (head[i]) euler(i);
  for (int i = 0; i < n; i++) cout << ans[i] << ' ';
  return 0;
}
