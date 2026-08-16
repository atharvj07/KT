#include <bits/stdc++.h>
using namespace std;
struct Edge {
  int x, y, v;
} E[200005];
bool Cmp(Edge a, Edge b) { return a.v > b.v; }
int Size[200005], Flag[200005];
int Fa[200005];
int GetRoot(int x) { return x == Fa[x] ? x : Fa[x] = GetRoot(Fa[x]); }
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= m; ++i) scanf("%d%d%d", &E[i].x, &E[i].y, &E[i].v);
  sort(E + 1, E + m + 1, Cmp);
  for (int i = 1; i <= n; ++i) Fa[i] = i, Size[i] = 1, Flag[i] = true;
  int Ans = 0;
  for (int i = 1; i <= m; ++i) {
    int Rx = GetRoot(E[i].x), Ry = GetRoot(E[i].y);
    if (Rx ^ Ry && (Flag[Rx] || Flag[Ry])) {
      if (Size[Rx] > Size[Ry]) swap(Rx, Ry);
      Fa[Rx] = Ry;
      Ans += E[i].v;
      Flag[Ry] &= Flag[Rx];
    } else if (Rx == Ry && Flag[Rx])
      Flag[Rx] = false, Ans += E[i].v;
  }
  printf("%d\n", Ans);
  return 0;
}
