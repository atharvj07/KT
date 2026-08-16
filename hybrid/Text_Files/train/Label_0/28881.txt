#include <bits/stdc++.h>
using namespace std;
long long mo(const long long input, const long long ceil) {
  return input >= ceil ? input % ceil : input;
}
const long long maxn = 5e5 + 10;
long long cnt, cnta, cntb;
long long vis[maxn];
vector<long long> e[maxn];
void dfs(long long k, long long t) {
  vis[k] = t;
  cnt++;
  for (auto i : e[k])
    if (vis[i] != t) dfs(i, t);
}
void solve(long long t) {
  long long n, m, a, b;
  cin >> n >> m >> a >> b;
  for (long long i = 1; i <= n; i++) e[i].clear();
  for (long long i = 1; i <= m; i++) {
    long long x, y;
    cin >> x >> y;
    e[x].push_back(y);
    e[y].push_back(x);
  }
  vis[a] = t * 2 - 1;
  cnt = 1;
  dfs(b, t * 2 - 1);
  cnta = n - cnt;
  vis[b] = t * 2;
  cnt = 1;
  dfs(a, t * 2);
  cntb = n - cnt;
  cout << cnta * cntb << "\n";
}
signed main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  long long tt = 1;
  cin >> tt;
  for (long long i = 1; i <= tt; i++) solve(i);
  cerr << "\n\n\nTime : "
       << 1000 * (long double)clock() / (long double)CLOCKS_PER_SEC << "ms\n";
  ;
  return 0;
}
