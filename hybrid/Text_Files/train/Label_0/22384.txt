#include <bits/stdc++.h>
using namespace std;
pair<int, int> a[100001];
short rs[100001 * 300];
map<int, int> M;
int pr[100001 * 300];
long long rrs[100001];
pair<pair<int, int>, short> v[2 * 100001];
void solve() {
  int n, k, i, j;
  scanf("%d", &n);
  scanf("%d", &k);
  for (i = 0; i < n; ++i) {
    scanf("%d", &a[i].first);
    scanf("%d", &a[i].second);
    M[a[i].second] = 1;
  }
  map<int, int>::iterator itr = M.begin();
  int prv = -2000000000;
  int cnt = 0;
  for (; itr != M.end(); ++itr) {
    itr->second = cnt + min((itr->first) - prv, 300);
    prv = itr->first;
    cnt = itr->second;
  }
  int x, y, ch;
  for (i = 0; i < n; ++i) {
    a[i].second = M[a[i].second];
  }
  M.clear();
  for (i = 0; i < n; ++i) {
    x = a[i].first - (k - 1);
    y = a[i].second;
    v[(i << 1)] = make_pair(make_pair(x, y), 1);
    v[(i << 1) ^ 1] = make_pair(make_pair(x + k, y), -1);
  }
  sort(v, v + (n << 1));
  for (i = 0; i < (n << 1); ++i) {
    x = v[i].first.first;
    ch = v[i].second;
    for (j = 0; j < k; ++j) {
      y = v[i].first.second - j;
      rrs[rs[y]] += (x - pr[y]);
      pr[y] = x;
      rs[y] += ch;
    }
  }
  for (i = 1; i <= n; ++i) printf("%lld ", rrs[i]);
}
int main() {
  int t = 1;
  while (t--) {
    solve();
  }
}
