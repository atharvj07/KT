#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1 << 22 + 1;
int pai[MAXN];
char ranki[MAXN];
char tmp[MAXN];
bool pd[MAXN];
bool inp[MAXN];
class ConjDisj {
 public:
  int n;
  ConjDisj(int N) {
    for (int i = 0, n = N; i < n; i++) {
      pai[i] = i;
      ranki[i] = 0;
    }
  }
  int busca(int x) {
    if (x != pai[x]) pai[x] = busca(pai[x]);
    return pai[x];
  }
  void uniao(int a, int b) {
    if (!inp[a] || !inp[b]) return;
    int paiA = busca(a), paiB = busca(b);
    if (ranki[paiA] < ranki[paiB]) {
      pai[paiA] = paiB;
    } else {
      if (ranki[paiA] == ranki[paiB]) ranki[paiA]++;
      pai[paiB] = paiA;
    }
  }
};
ConjDisj cd(MAXN - 1);
bool solve(int mask, int W) {
  if (!pd[mask]) {
    for (int i = 1 << 21; i > 0; i >>= 1) {
      if (i & mask) {
        int nmask = mask ^ i;
        cd.uniao(W, nmask);
        solve(nmask, W);
      }
    }
    pd[mask] = true;
  }
  return pd[mask];
}
int main() {
  int n, m;
  scanf(" %d %d", &n, &m);
  memset(pd, 0, sizeof pd);
  for (int i = 0; i < m; i++) {
    int x;
    scanf(" %d", &x);
    inp[x] = true;
  }
  for (int i = 0; i < 1 << 22; i++) {
    if (!inp[i]) continue;
    int x = i;
    int w = ((1 << 22) - 1) ^ x;
    cd.uniao(x, w);
    solve(w, x);
  }
  for (int i = 0; i < 1 << 22; i++) {
    if (inp[i]) {
      tmp[cd.busca(i)] = 1;
    }
  }
  int ans = 0;
  for (int i = 0; i < 1 << 22; i++) {
    if (tmp[i]) ans++;
  }
  printf("%d\n", ans);
}
