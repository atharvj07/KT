#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, pii> node;
const int maxn = 2e5 + 10;
int n, par[maxn]; ll k, a[maxn], f[maxn];
vector <node> e;

int find(int x) {
  return par[x] == x ? x : par[x] = find(par[x]);
}

void unite(int x, int y) {
  par[find(x)] = find(y);
}

void solve(int l, int r) {
  if (l == r) return;
  ll val = 1ll << 60;
  int mid = l + r >> 1, pl = 0, pr = 0;
  for (int i = l; i <= mid; i++) {
    f[i] = a[i] - k * i;
    if (val > f[i]) val = f[i], pl = i;
  }
  val = 1ll << 60;
  for (int i = mid + 1; i <= r; i++) {
    f[i] = a[i] + k * i;
    if (val > f[i]) val = f[i], pr = i;
  }
  for (int i = l; i <= mid; i++) {
    e.push_back(node(f[i] + f[pr], pii(i, pr)));
  }
  for (int i = mid + 1; i <= r; i++) {
    e.push_back(node(f[pl] + f[i], pii(i, pl)));
  }
  solve(l, mid), solve(mid + 1, r);
}

int main() {
  scanf("%d %lld", &n, &k);
  for (int i = 1; i <= n; i++) {
    scanf("%lld", a + i), par[i] = i;
  }
  solve(1, n), sort(e.begin(), e.end());
  ll ans = 0;
  for (node p : e) {
    int u = p.second.first, v = p.second.second;
    if (find(u) != find(v)) {
      ans += p.first, unite(u, v);
    }
  }
  printf("%lld", ans);
  return 0;
}