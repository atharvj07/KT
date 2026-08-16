#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
const long long int INFLL = 1e18;
const double EPS = 1e-8;
const long long int MOD = 1000000007;
template <class T>
T &chmin(T &a, const T &b) {
  return a = min(a, b);
}
template <class T>
T &chmax(T &a, const T &b) {
  return a = max(a, b);
}
struct Mod {
  unsigned n;
  Mod() {}
  Mod(long long int x) {
    if (x < 0)
      n = x % MOD + MOD;
    else
      n = x % MOD;
  }
};
Mod operator+(Mod a, Mod b) { return Mod((a.n + b.n) % MOD); }
Mod operator+=(Mod &a, Mod b) { return a = a + b; }
Mod operator-(Mod a, Mod b) { return Mod((a.n + MOD - b.n) % MOD); }
Mod operator-=(Mod &a, Mod b) { return a = a - b; }
Mod operator*(Mod a, Mod b) { return Mod(((long long int)a.n * b.n) % MOD); }
Mod operator*=(Mod &a, Mod b) { return a = a * b; }
Mod modpow(Mod x, long long int k) {
  Mod res = 1;
  while (k) {
    if (k & 1) res *= x;
    k /= 2;
    x *= x;
  }
  return res;
}
Mod inv(Mod a) { return modpow(a, MOD - 2); }
Mod operator/(Mod a, Mod b) {
  return Mod(((long long int)a.n * inv(b).n) % MOD);
}
Mod operator/=(Mod &a, Mod b) { return a = a / b; }
struct Bit {
  vector<long long int> bit;
  int size;
  void init(int n) {
    n++;
    size = 1;
    while (size < n) size *= 2;
    bit = vector<long long int>(size, 0);
  }
  void add(int k, long long int x) {
    k++;
    while (k <= size) {
      bit[k] += x;
      k += k & -k;
    }
  }
  long long int sum(int k) {
    k++;
    long long int res = 0;
    while (k > 0) {
      res += bit[k];
      k -= k & -k;
    }
    return res;
  }
  long long int get(int k) { return sum(k) - sum(k - 1); }
  long long int update(int k, long long int x) { add(k, x - get(k)); }
};
struct Tree {
  vector<vector<pair<long long int, long long int> > > G;
  int n, logn, r;
  vector<int> nst, sst;
  vector<int> dep;
  vector<long long int> w;
  vector<int> par;
  vector<bool> used;
  vector<vector<int> > ps;
  vector<int> in, out;
  int etcnt;
  bool dfs_f, lca_f, et_f;
  Bit etbit;
  void init(int num, int root = 0) {
    n = num;
    r = root;
    G = vector<vector<pair<long long int, long long int> > >(n);
    par = vector<int>(n, -1);
    w = vector<long long int>(n, 1);
    dfs_f = lca_f = et_f = false;
  }
  Tree(int num, int root = 0) { init(num, root); }
  Tree() {}
  void set_weight(const vector<long long int> &weight) { w = weight; }
  void set_graph_dfs(
      const vector<vector<pair<long long int, long long int> > > &g, int x) {
    used[x] = true;
    for (auto &w : g[x]) {
      if (!used[w.first]) {
        G[x].push_back(w);
        set_graph_dfs(g, w.first);
      }
    }
  }
  void set_graph(const vector<vector<pair<long long int, long long int> > > &g,
                 int root = 0) {
    init(g.size(), root);
    used = vector<bool>(n, 0);
    G = vector<vector<pair<long long int, long long int> > >(n);
    set_graph_dfs(g, root);
  }
  void set_graph(int root = 0) {
    vector<vector<pair<long long int, long long int> > > tempg = G;
    set_graph(tempg, root);
  }
  void add_edge(int x, int p, long long int co = 1) {
    G[p].push_back(pair<long long int, long long int>(x, co));
  }
  void add_biedge(int a, int b, long long int co = 1) {
    G[a].push_back(pair<long long int, long long int>(b, co));
    G[b].push_back(pair<long long int, long long int>(a, co));
  }
  void dfs(int x, int p, int d) {
    used[x] = true;
    dep[x] = d;
    nst[x] = 1;
    sst[x] = w[x];
    par[x] = p;
    for (auto &w : G[x]) {
      if (p != x && !used[w.first]) {
        dfs(w.first, x, d + 1);
        nst[x] += nst[w.first];
        sst[x] += sst[w.first];
      }
    }
  }
  void dfs() {
    used = vector<bool>(n, false);
    nst = sst = vector<int>(n);
    dep = vector<int>(n);
    dfs(r, -1, 0);
    dfs_f = true;
  }
  void init_lca() {
    if (!dfs_f) dfs();
    logn = (int)log2(n) + 1;
    ps = vector<vector<int> >(logn, vector<int>(n, -1));
    ps[0] = par;
    for (int i = (1); i < (int)(logn); i++) {
      for (int j = (0); j < (int)(n); j++) {
        if (ps[i - 1][j] == -1)
          ps[i][j] = -1;
        else
          ps[i][j] = ps[i - 1][ps[i - 1][j]];
      }
    }
    lca_f = true;
  }
  int lca(int a, int b) {
    if (!lca_f) init_lca();
    if (dep[a] > dep[b]) swap(a, b);
    for (int i = logn; i >= 0; i--)
      if ((dep[b] - dep[a]) & (1 << i)) b = ps[i][b];
    if (a == b) return a;
    for (int i = logn - 1; i >= 0; i--) {
      if (ps[i][a] != ps[i][b]) {
        a = ps[i][a];
        b = ps[i][b];
      }
    }
    return ps[0][a];
  }
  void etdfs(int x) {
    in[x] = etcnt++;
    for (auto &w : G[x]) {
      etdfs(w.first);
      etbit.add(in[w.first], w.second);
      etbit.add(out[w.first], -w.second);
    }
    out[x] = etcnt++;
  }
  void etdfs() {
    if (!dfs_f) dfs();
    if (!lca_f) init_lca();
    etcnt = 0;
    in = vector<int>(n);
    out = vector<int>(n);
    etbit.init(2 * n);
    etdfs(r);
    et_f = true;
  }
  void etupdate(int x, long long int d) {
    if (!et_f) etdfs();
    etbit.update(in[x], d);
    etbit.update(out[x], -d);
  }
  long long int dist(int a, int b) {
    if (!et_f) etdfs();
    return etbit.sum(in[a]) + etbit.sum(in[b]) - etbit.sum(in[lca(a, b)]) * 2;
  }
  vector<Mod> ds, dss;
  void dsdfs(int x) {
    for (auto &w : G[x]) {
      dsdfs(w.first);
      Mod c = w.second;
      ds[x] += ds[w.first] + Mod(nst[w.first]) * c;
      dss[x] +=
          dss[w.first] + Mod(2) * c * ds[w.first] + c * c * Mod(nst[w.first]);
    }
  }
  void dsdfs() {
    ds = dss = vector<Mod>(n, 0);
    dsdfs(r);
  }
  vector<Mod> ss, sss;
  void qdfs(int x, Mod sum, Mod sums) {
    ss[x] = sum;
    sss[x] = sums;
    for (auto &w : G[x]) {
      int t = w.first;
      Mod c = w.second;
      qdfs(t, sum + Mod(n - 2 * nst[t]) * c,
           sums + c * c * Mod(n) - Mod(4) * (ds[t] + c * Mod(nst[t])) * c +
               Mod(2) * sum * c);
    }
  }
  void qdfs() {
    dsdfs();
    ss = sss = vector<Mod>(n);
    qdfs(r, ds[r], dss[r]);
  }
  Mod mdist(int u, int v) { return Mod(dist(u, v)); }
  Mod querya(int u, int v) {
    if (lca(u, v) == v) {
      return sss[u] -
             (sss[v] - dss[v] + mdist(u, v) * mdist(u, v) * Mod(n - nst[v]) +
              Mod(2) * mdist(u, v) * (ss[v] - ds[v]));
    } else {
      return dss[v] + mdist(u, v) * mdist(u, v) * Mod(nst[v]) +
             Mod(2) * mdist(u, v) * ds[v];
    }
  }
  Mod query(int u, int v) { return Mod(2) * querya(u, v) - sss[u]; }
};
Tree T;
int n, q;
int main() {
  cin >> n;
  T.init(n);
  for (int i = (0); i < (int)(n - 1); i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    T.add_biedge(a, b, c);
  }
  T.set_graph(0);
  T.dfs();
  T.init_lca();
  T.etdfs();
  T.qdfs();
  cin >> q;
  for (int i = (0); i < (int)(q); i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    cout << T.query(u, v).n << endl;
  }
  return 0;
}
