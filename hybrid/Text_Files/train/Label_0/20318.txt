#include <bits/stdc++.h>
using namespace std;
const int N = 5050;
int n, m, q, last, dex, a[N], c[N], up[N], down[N];
bool mark[N];
vector<int> vec[N], nei[N];
void del(int dex) {
  auto it = &nei[c[dex]];
  for (int i = 0; i < (*it).size(); i++)
    if ((*it)[i] == a[dex]) {
      swap((*it)[i], (*it)[(*it).size() - 1]);
      (*it).pop_back();
      break;
    }
}
bool dfs(int v) {
  mark[v] = true;
  for (int u : nei[v])
    if (up[u] == -1 || (mark[up[u]] == false && dfs(up[u]))) {
      down[v] = u;
      up[u] = v;
      return true;
    }
  return false;
}
bool ok(int k) {
  fill(up, up + N, -1);
  fill(down, down + N, -1);
  int matching = 0;
  bool done = false;
  while (done == false) {
    done = true;
    memset(mark, false, sizeof mark);
    for (int v = 0; v < N; v++)
      if (mark[v] == false && down[v] == -1 && dfs(v)) matching++, done = false;
  }
  return matching >= k + 1;
}
int main() {
  ios::sync_with_stdio(false), cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    vec[a[i]].push_back(i);
  }
  for (int i = 0; i < n; i++) {
    cin >> c[i];
    nei[--c[i]].push_back(a[i]);
  }
  last = N - 1;
  cin >> q;
  while (q--) {
    cin >> dex;
    del(--dex);
    while (ok(last) == false) {
      for (int v : vec[last]) del(v);
      last--;
    }
    cout << last + 1 << '\n';
  }
  return 0;
}
