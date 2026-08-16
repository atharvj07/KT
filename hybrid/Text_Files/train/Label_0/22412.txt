#include <bits/stdc++.h>

using namespace std;

using int64 = long long;

int N, W[100000], Q;
vector< int > g[100000];
int dep[100000];
int64 sub[100000];
int64 heavy[3][100000];
const int LOG = 20;

int par[LOG][100000];
int64 sz[LOG][100000];

void predfs(int idx, int p, int d) {
  par[0][idx] = p;
  dep[idx] = d;
  sub[idx] += W[idx];
  for(auto &to : g[idx]) {
    if(to == p) continue;
    predfs(to, idx, d + 1);
    sub[idx] += sub[to];
    if(heavy[0][idx] < sub[to]) {
      heavy[2][idx] = heavy[1][idx];
      heavy[1][idx] = heavy[0][idx];
      heavy[0][idx] = sub[to];
    } else if(heavy[1][idx] < sub[to]) {
      heavy[2][idx] = heavy[1][idx];
      heavy[1][idx] = sub[to];
    } else if(heavy[2][idx] < sub[to]) {
      heavy[2][idx] = sub[to];
    }
  }
}

void dfs(int idx, int p) {
  for(auto &to : g[idx]) {
    if(to == p) continue;
    dfs(to, idx);
    sz[0][to] = heavy[heavy[0][idx] == sub[to]][idx];
  }
}

int lca(int x, int y) {
  if(dep[x] > dep[y]) swap(x, y);
  for(int i = LOG - 1; i >= 0; i--) {
    if((dep[y] - dep[x]) >> i & 1) y = par[i][y];
  }
  if(x == y) return x;
  for(int i = LOG - 1; i >= 0; i--) {
    if(par[i][x] != par[i][y]) {
      x = par[i][x];
      y = par[i][y];
    }
  }
  return par[0][x];
}

int main() {
  scanf("%d", &N);
  for(int i = 0; i < N; i++) {
    scanf("%d", &W[i]);
  }
  for(int i = 1; i < N; i++) {
    int x, y;
    scanf("%d %d", &x, &y);
    --x, --y;
    g[x].emplace_back(y);
    g[y].emplace_back(x);
  }
  predfs(0, -1, 0);
  dfs(0, -1);
  for(int i = 0; i + 1 < LOG; i++) {
    for(int j = 0; j < N; j++) {
      if(par[i][j] == -1) par[i + 1][j] = -1;
      else par[i + 1][j] = par[i][par[i][j]];
      if(par[i + 1][j] == -1) continue;
      sz[i + 1][j] = max(sz[i][j], sz[i][par[i][j]]);
    }
  }

  int64 all = accumulate(W, W + N, 0LL);

  scanf("%d", &Q);
  while(Q--) {
    int a, b;
    scanf("%d %d", &a, &b);
    --a, --b;
    if(dep[a] > dep[b]) swap(a, b);
    int p = lca(a, b);

    int64 ret = 0;
    if(p != a) {

      bool ng[3] = {};
      ret = max(ret, heavy[0][a]);
      ret = max(ret, heavy[0][b]);

      for(auto c : {a, b}) {
        int xx = dep[p] + 1;
        for(int i = LOG - 1; i >= 0; i--) {
          if(((dep[c] - xx) >> i) & 1) {
            ret = max(ret, sz[i][c]);
            c = par[i][c];
          }
        }
        for(int i = 0; i < 3; i++) {
          if(ng[i]) continue;
          if(sub[c] == heavy[i][p]) {
            ng[i] = true;
            break;
          }
        }
      }
      for(int i = 0; i < 3; i++) {
        if(ng[i]) continue;
        ret = max(ret, heavy[i][p]);
      }
    } else if(p != b) {
      ret = max(ret, heavy[0][b]);
      int c = b;
      int xx = dep[a] + 1;
      for(int i = LOG - 1; i >= 0; i--) {
        if(((dep[c] - xx) >> i) & 1) {
          ret = max(ret, sz[i][c]);
          c = par[i][c];
        }
      }
      ret = max(ret, sz[0][c]);
    } else {
      ret = max(ret, heavy[0][p]);
    }

    printf("%lld\n", max(ret, all - sub[p]));
  }
}


