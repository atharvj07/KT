#include <bits/stdc++.h>
using namespace std;
const int maxn = 3e5 + 10;
int n, m, q;
int par[maxn], L[maxn];
int cnt[maxn];
void merge(int, int);
pair<int, int> root(int);
vector<int> adj[maxn];
void input() {
  scanf("%d%d%d", &n, &m, &q);
  int v, u;
  for (int i = 0; i < n; i++) par[i] = -1;
  for (int i = 0; i < m; i++) {
    scanf("%d%d", &u, &v);
    u--, v--;
    pair<int, int> Uinformation;
    adj[u].push_back(v);
    adj[v].push_back(u);
    merge(u, v);
  }
}
int dis[maxn];
bool mark[maxn];
int mx, ind;
void DFS_visit(int v) {
  mark[v] = 1;
  for (int i = 0; i < adj[v].size(); i++) {
    int nextV = adj[v][i];
    if (mark[nextV] == 0) {
      dis[nextV] = dis[v] + 1;
      if (mx < dis[nextV]) {
        mx = dis[nextV];
        ind = nextV;
      }
      mark[nextV] = 1;
      DFS_visit(nextV);
      dis[nextV] = 0;
      mark[nextV] = 0;
    }
  }
}
void DFS() {
  for (int i = 0; i < n; i++) {
    mx = 0;
    ind = -1;
    if (par[i] == -1) {
      DFS_visit(i);
      mx = 0;
      mark[i] = 0;
      dis[i] = 0;
      if (ind != -1) DFS_visit(ind);
      L[i] = mx;
    }
  }
}
pair<int, int> root(int v) {
  int now = v;
  int cnt = 0;
  while (par[now] != -1) {
    now = par[now];
    cnt++;
  }
  while (par[v] != -1) {
    int tmp = par[v];
    par[v] = now;
    v = tmp;
  }
  return make_pair(now, cnt);
}
void merge(int v, int u) {
  int parV = root(v).first, parU = root(u).first;
  if (parV == parU) return;
  if (cnt[parU] < cnt[parV]) {
    par[parU] = parV;
    cnt[parV] += cnt[parU];
    L[parV] = max(max(L[parV], L[parU]),
                  (int)ceil(L[parV] / 2.0) + (int)ceil(L[parU] / 2.0) + 1);
  } else {
    par[parV] = parU;
    cnt[parU] += cnt[parV];
    L[parU] = max(max(L[parV], L[parU]),
                  (int)ceil(L[parV] / 2.0) + (int)ceil(L[parU] / 2.0) + 1);
  }
}
int main() {
  input();
  DFS();
  int type, v, u;
  string s;
  for (int i = 0; i < q; i++) {
    scanf("%d", &type);
    if (type == 1) {
      scanf("%d", &v);
      cout << L[root(v - 1).first] << endl;
    } else {
      scanf("%d%d", &v, &u);
      merge(v - 1, u - 1);
    }
  }
}
