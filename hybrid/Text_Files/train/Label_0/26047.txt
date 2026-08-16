#include <bits/stdc++.h>
using namespace std;
const long long MOD = 999998727899999ll, MAXN = 300001;
long long c[MAXN];
vector<long long> g[MAXN];
set<long long> s[MAXN];
string t;
bool mark[MAXN];
long long base = 101;
long long diff[MAXN];
long long ans[MAXN];
long long n;
void dsu(long long a1, long long a2) {
  set<long long>::iterator it = s[a2].begin();
  while (it != s[a2].end()) {
    s[a1].insert(*it);
    it++;
  }
  s[a2].clear();
}
int dfs(long long v, long long h) {
  long long hash = ((h * base) + (t[v - 1] - 'a' + 1)) % MOD;
  mark[v] = 1;
  vector<int> child;
  for (int i = 0; i < g[v].size(); i++) {
    long long u = g[v][i];
    if (!mark[u]) {
      child.push_back(dfs(u, hash));
    }
  }
  if (child.size() == 0) {
    diff[v] = 1;
    s[v].insert(hash);
    return v;
  } else {
    int w = 0;
    for (int i = 1; i < child.size(); i++) {
      if (s[child[i]].size() > s[child[w]].size()) {
        w = i;
      }
    }
    for (int i = 0; i < child.size(); i++) {
      if (i != w) {
        dsu(child[w], child[i]);
      }
    }
    s[child[w]].insert(hash);
    diff[v] = s[child[w]].size();
    return child[w];
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> c[i];
    ans[i] = i;
  }
  cin >> t;
  for (int i = 1; i < n; i++) {
    int u, v;
    cin >> u >> v;
    g[v].push_back(u);
    g[u].push_back(v);
  }
  dfs(1, 0);
  long long mx = 0;
  for (int i = 1; i <= n; i++) {
    mx = max(diff[i] + c[i], mx);
  }
  long long cnt = 0;
  for (int i = 1; i <= n; i++) {
    if (diff[i] + c[i] == mx) {
      cnt++;
    }
  }
  cout << mx << endl;
  cout << cnt;
  return 0;
}
