#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using db = double;
using pii = pair<int, int>;
using vec = vector<int>;
int read() {
  int x = 0;
  bool f = 0;
  char ch = getchar();
  while (!isdigit(ch)) f |= ch == '-', ch = getchar();
  while (isdigit(ch)) x = (x << 1) + (x << 3) + (ch ^ 48), ch = getchar();
  return f ? -x : x;
}
const int N = 1e5 + 10;
const int mod = 1e9 + 7;
const int M = 58;
int n, K, x[N], y[N], z[N], fac[N], bx[M], by[M];
ll sf[M];
vector<pii> G[M];
map<ll, int> f[2][M];
void upd(int &x) { x = x + (x >> 31 & mod); }
int main() {
  n = read(), K = read();
  for (int i = (fac[0] = 1); i <= n; i++) fac[i] = (ll)fac[i - 1] * i % mod;
  for (int i = 1; i <= K; i++)
    x[i] = read(), y[i] = read(), z[i] = read() - 1, bx[i] = x[i], by[i] = y[i];
  sort(bx + 1, bx + K + 1);
  sort(by + 1, by + K + 1);
  int cx = unique(bx + 1, bx + K + 1) - bx - 1,
      cy = unique(by + 1, by + K + 1) - by - 1;
  for (int i = 1; i <= K; i++)
    x[i] = lower_bound(bx + 1, bx + cx + 1, x[i]) - bx,
    y[i] = lower_bound(by + 1, by + cy + 1, y[i]) - by,
    G[x[i]].push_back({y[i], z[i]});
  for (int i = cx; i > 0; i--) {
    sf[i] = sf[i + 1];
    for (auto d : G[i]) sf[i] |= 1ll << d.first - 1;
  }
  int o = 0;
  f[o][0][0] = 1;
  for (int i = 1; i <= cx; i++, o ^= 1) {
    for (int j = 0; j < i; j++) {
      for (auto d : f[o][j]) {
        upd(f[o ^ 1][j][d.first & sf[i + 1]] += d.second - mod);
        for (auto ed : G[i])
          if (!(d.first >> ed.first - 1 & 1ll))
            upd(f[o ^ 1][j + 1][(d.first | 1ll << ed.first - 1) & sf[i + 1]] +=
                (ll)d.second * ed.second % mod - mod);
      }
      map<ll, int> tmp;
      f[o][j].swap(tmp);
    }
  }
  int ans = 0;
  for (int i = 0; i <= cx; i++)
    for (auto d : f[o][i]) upd(ans += (ll)d.second * fac[n - i] % mod - mod);
  printf("%d\n", ans);
  return 0;
}
