#include <bits/stdc++.h>
using namespace std;
int n, m;
char S[555], ch[555][555];
int X[555], V[555];
int Head[400010], Next[400010], Go[400010], Fl[400010], Cost[400010], H[400010],
    Cnt = 1;
void addedge(int x, int y, int z, int w) {
  Go[++Cnt] = y;
  Next[Cnt] = Head[x];
  Head[x] = Cnt;
  Fl[Cnt] = z;
  Cost[Cnt] = w;
  Go[++Cnt] = x;
  Next[Cnt] = Head[y];
  Head[y] = Cnt;
  Fl[Cnt] = 0;
  Cost[Cnt] = -w;
}
void cmin(int &x, int y) {
  if (x > y) x = y;
}
void precalc() {
  static int Deg[400010];
  for (int i = 1; i <= n + 3; i++)
    for (int T = Head[i]; T; T = Next[T])
      if (Fl[T]) Deg[Go[T]]++;
  memset(H, 63, sizeof H);
  H[n + 2] = 0;
  vector<int> V(1, n + 2);
  for (int i = 0; i < V.size(); i++) {
    int x = V[i];
    for (int T = Head[x]; T; T = Next[T])
      if (Fl[T]) {
        cmin(H[Go[T]], H[x] + Cost[T]);
        if (!--Deg[Go[T]]) V.push_back(Go[T]);
      }
  }
}
int Dis[555], vis[555], FF[555], Pr[555];
void Dij() {
  memset(Dis, 63, sizeof Dis);
  memset(vis, 0, sizeof vis);
  memset(FF, 0, sizeof FF);
  Dis[n + 2] = 0;
  FF[n + 2] = 1000000000;
  for (int o = 1; o <= n + 3; o++) {
    int mn = 1e9, x;
    for (int i = 1; i <= n + 3; i++)
      if (!vis[i] && mn > Dis[i]) mn = Dis[i], x = i;
    vis[x] = 1;
    for (int T = Head[x]; T; T = Next[T])
      if (Fl[T]) {
        int v = Cost[T] + H[x] - H[Go[T]];
        if (Dis[Go[T]] > Dis[x] + v) {
          Dis[Go[T]] = Dis[x] + v;
          Pr[Go[T]] = T ^ 1;
          FF[Go[T]] = min(FF[x], Fl[T]);
        }
      }
  }
}
int inst[555];
int Flow() {
  precalc();
  int ans = 0;
  for (;;) {
    Dij();
    if (Dis[n + 3] >= 1000000000) return ans;
    ans += FF[n + 3] * (Dis[n + 3] + H[n + 3]);
    for (int i = n + 3; i != n + 2; i = Go[Pr[i]])
      Fl[Pr[i]] += FF[n + 3], Fl[Pr[i] ^ 1] -= FF[n + 3];
    for (int i = 1; i <= n + 3; i++) H[i] += Dis[i];
  }
}
int main() {
  scanf("%d", &n);
  scanf("%s", S + 1);
  scanf("%d", &m);
  for (int i = 1; i <= m; i++) {
    scanf("%s", ch[i] + 1);
    scanf("%d", &V[i]);
    int s = strlen(ch[i] + 1);
    for (int j = 1; j + s - 1 <= n; j++) {
      int flag = 1;
      for (int k = 1; k <= s; k++)
        if (S[j + k - 1] != ch[i][k]) {
          flag = 0;
          break;
        }
      if (flag == 1) {
        addedge(j, j + s, 1, -V[i]);
      }
    }
  }
  scanf("%d", &X[1]);
  for (int i = 2; i <= n; i++) X[i] = X[i - 1];
  for (int i = 1; i <= n + 1; i++)
    if (X[i] > X[i - 1])
      addedge(n + 2, i, X[i] - X[i - 1], 0);
    else if (X[i] < X[i - 1])
      addedge(i, n + 3, X[i - 1] - X[i], 0);
  for (int i = 1; i <= n; i++) addedge(i, i + 1, X[i], 0);
  printf("%d\n", -Flow());
  return 0;
}
