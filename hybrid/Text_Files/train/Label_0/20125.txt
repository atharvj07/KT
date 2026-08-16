#include <bits/stdc++.h>
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
using namespace std;
const long long MOD = 1000000007LL, INF = 1e9, LINF = 1e18;
const long double PI = 3.141592653589793116, EPS = 1e-9,
                  GOLD = ((1 + sqrt(5)) / 2);
template <class T>
int getbit(T s, int i) {
  return (s >> 1) & 1;
}
template <class T>
T onbit(T s, int i) {
  return s | (T(1) << i);
}
template <class T>
T offbit(T s, int i) {
  return s & (~(T(1) << i));
}
template <class T>
int cntbit(T s) {
  return __builtin_popcount(s);
}
long long n, m, s, t, ans = 0;
vector<vector<long long> > adj;
vector<long long> dpS, dpT;
vector<bool> vis;
vector<vector<bool> > linked;
void VarInput() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cin >> n >> m >> s >> t;
  vis.resize(n, false);
  linked.resize(n, vector<bool>(n, false));
  adj.resize(n, vector<long long>(0));
  s--;
  t--;
  while (m--) {
    long long u, v;
    cin >> u >> v;
    u--;
    v--;
    adj[u].push_back(v);
    adj[v].push_back(u);
    linked[u][v] = true;
    linked[v][u] = true;
  }
}
void ProSolve() {
  dpS.resize(n, 0);
  dpT = dpS;
  queue<long long> QS;
  QS.push(s);
  vis[s] = true;
  while (!QS.empty()) {
    long long z = QS.front();
    QS.pop();
    for (long long i = 0; i < adj[z].size(); i++) {
      if (!vis[adj[z][i]]) {
        vis[adj[z][i]] = true;
        dpS[adj[z][i]] = dpS[z] + 1;
        QS.push(adj[z][i]);
      }
    }
  }
  for (long long i = 0; i < n; i++) vis[i] = false;
  queue<long long> QT;
  QT.push(t);
  vis[t] = true;
  while (!QT.empty()) {
    long long z = QT.front();
    QT.pop();
    for (long long i = 0; i < adj[z].size(); i++) {
      if (!vis[adj[z][i]]) {
        vis[adj[z][i]] = true;
        dpT[adj[z][i]] = dpT[z] + 1;
        QT.push(adj[z][i]);
      }
    }
  }
  long long dist = dpS[t];
  for (long long i = 0; i < n; i++) {
    for (long long j = i + 1; j < n; j++) {
      if (linked[i][j]) continue;
      if (min(dpS[i] + dpT[j], dpS[j] + dpT[i]) + 1 >= dist) {
        ans++;
      }
    }
  }
  cout << ans;
}
int main() {
  VarInput();
  ProSolve();
  return 0;
}
