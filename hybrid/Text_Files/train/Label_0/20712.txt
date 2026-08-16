#include <bits/stdc++.h>
using namespace std;
const long long inf = 1e18;
const double eps = 1e-9;
const double INF = inf;
const double EPS = eps;
int n, m;
int L[110], R[110];
vector<pair<int, int> > G[110000], GR[110000];
int Tp[110000];
long long D[110000];
int s1, s2, f;
set<pair<long long, int> > S;
int Res[110];
void relax(int v, long long d, int tp) {
  if (D[v] < d) return;
  if (D[v] > d)
    S.erase(make_pair(D[v], v)), D[v] = d, Tp[v] = 0,
                                 S.insert(make_pair(D[v], v));
  Tp[v] |= tp;
}
bool can(bool wn) {
  int i;
  for (i = 0; i < 110; i++) Res[i] = L[i];
  for (i = 0; i < n; i++) D[i] = inf, Tp[i] = 0;
  Tp[s1] = 1, Tp[s2] = 2;
  D[s1] = 0, D[s2] = 0;
  S.clear();
  S.insert(make_pair(D[s1], s1)), S.insert(make_pair(D[s2], s2));
  while (S.size()) {
    int v = S.begin()->second;
    S.erase(S.begin());
    int tp = Tp[v];
    assert(0 < tp && tp < 4);
    for (i = 0; i < (int)G[v].size(); i++)
      relax(G[v][i].first, D[v] + G[v][i].second, tp);
    for (i = 0; i < (int)GR[v].size(); i++) {
      int id = GR[v][i].second;
      int add = L[id];
      if (wn && (tp & 2) != 0) add = R[id], Res[id] = R[id];
      if ((!wn) && (tp & 1) == 0) add = R[id], Res[id] = R[id];
      relax(GR[v][i].first, D[v] + add, tp);
    }
  }
  int tp = Tp[f];
  assert(0 < tp && tp < 4);
  if (wn) return (tp == 1);
  return ((tp & 1) != 0);
}
int main() {
  int i, k, v1, v2, l;
  scanf("%d%d%d", &n, &m, &k);
  scanf("%d%d%d", &s1, &s2, &f), s1--, s2--, f--;
  for (i = 0; i < m; i++)
    scanf("%d%d%d", &v1, &v2, &l), v1--, v2--,
        G[v1].push_back(make_pair(v2, l));
  for (i = 0; i < k; i++)
    scanf("%d%d%d%d", &v1, &v2, &L[i], &R[i]), v1--, v2--,
        GR[v1].push_back(make_pair(v2, i));
  if (s1 == s2) {
    puts("DRAW");
    for (i = 0; i < k; i++) printf("%d ", L[i]);
    return 0;
  }
  if (can(1)) {
    puts("WIN");
    for (i = 0; i < k; i++) printf("%d ", Res[i]);
    return 0;
  }
  if (can(0)) {
    puts("DRAW");
    for (i = 0; i < k; i++) printf("%d ", Res[i]);
  } else
    puts("LOSE");
  ;
  return 0;
}
