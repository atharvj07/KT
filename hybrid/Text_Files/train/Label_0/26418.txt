#include <bits/stdc++.h>
using namespace std;
const int maxn = 6e5 + 10, inf = 0x3f3f3f3f;
vector<int> v[maxn];
int fa[maxn];
long long cnt[maxn];
int n, k;
string s;
int find(int x) { return fa[x] == x ? x : fa[x] = find(fa[x]); }
void merge(int u, int v) {
  u = find(u), v = find(v);
  if (u == v) return;
  cnt[u] += cnt[v];
  fa[v] = u;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> k >> s;
  for (int i = 1, c, t; i <= k; i++) {
    cin >> c;
    while (c--) {
      cin >> t;
      v[t].push_back(i);
    }
  }
  for (int i = 1; i <= k; i++) {
    fa[i] = i, fa[i + k] = i + k;
    cnt[i + k] = 1;
  }
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    if (v[i].size() == 0) {
      printf("%d\n", ans);
      continue;
    } else if (v[i].size() == 1) {
      int x = v[i][0];
      ans -= min(cnt[find(x)], cnt[find(x + k)]);
      if (s[i - 1] == '0')
        cnt[find(x)] = inf;
      else
        cnt[find(x + k)] = inf;
      ans += min(cnt[find(x)], cnt[find(x + k)]);
      printf("%d\n", ans);
    } else {
      int x1 = v[i][0], x2 = v[i][1];
      if (find(x1) == find(x2) || find(x1) == find(x2 + k)) {
        printf("%d\n", ans);
        continue;
      }
      ans -= min(cnt[find(x1)], cnt[find(x1 + k)]);
      ans -= min(cnt[find(x2)], cnt[find(x2 + k)]);
      if (s[i - 1] == '0') {
        merge(x1, x2 + k);
        merge(x1 + k, x2);
      } else {
        merge(x1, x2);
        merge(x1 + k, x2 + k);
      }
      ans += min(cnt[find(x1)], cnt[find(x1 + k)]);
      printf("%d\n", ans);
    }
  }
}
