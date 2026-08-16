#include <bits/stdc++.h>
using namespace std;
const int MOD = 51123987;
const int maxn = 152;
const int maxs = 5005;
const int maxa = 52;
string st;
int f[maxs][maxa][maxa];
int P[maxn][maxn];
int la[maxn], lb[maxn], lc[maxn];
int Q[maxs];
int n, ret, Qs = 0, Ps = 0;
inline void Add(int &x, int y) {
  x += y;
  if (x >= MOD) x -= MOD;
}
int N1, N0;
inline void Addit(int p, int &cur, pair<int, int> ab, int s) {
  int a = ab.first;
  if (a > N1 || a + p < N0) return;
  int b = ab.second;
  if (b > N1 || b + p < N0) return;
  int c = n - p - a - b;
  if (c > N1 || c + p < N0) return;
  if (cur == -1) {
    if (Qs)
      cur = Q[Qs--];
    else
      cur = Ps++;
  }
  Add(f[cur][a][b], s);
}
void Release(int x, int y) {
  memset(f[P[x][y]], 0, sizeof(f[P[x][y]]));
  Q[++Qs] = P[x][y];
}
void init() {
  scanf("%d", &n);
  cin >> st;
}
inline void Check(int x) {
  if (st[x] == 'a') la[x] = x;
  if (st[x] == 'b') lb[x] = x;
  if (st[x] == 'c') lc[x] = x;
}
inline void Swap(int &a, int &b) {
  int tmp = a;
  a = b;
  b = tmp;
}
inline bool legal(int a, int b, int c) {
  if (a < b) Swap(a, b);
  if (a < c) Swap(a, c);
  if (b < c) Swap(b, c);
  return a <= c + 1;
}
void work() {
  N0 = n / 3 - 1;
  N1 = n / 3 + 1;
  la[0] = lb[0] = lc[0] = -1;
  Check(0);
  for (int i = 1; i < n; i++) {
    la[i] = la[i - 1], lb[i] = lb[i - 1], lc[i] = lc[i - 1];
    Check(i);
  }
  ret = 0;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) P[i][j] = -1;
  for (int i = n - 1; i >= 0; i--) {
    if (la[n - 1] == i || lb[n - 1] == i || lc[n - 1] == i)
      Addit(n - 1, P[i][n - 1],
            make_pair(st[i] == 'a' ? 1 : 0, st[i] == 'b' ? 1 : 0), 1);
    for (int l = n - 1; l >= 0; l--) {
      int l1 = l - 1;
      if (P[i][l] == -1) continue;
      for (int sa = 0; sa <= n - l && sa <= 51; sa++)
        for (int sb = 0; sb + sa <= n - l && sb <= 51; sb++) {
          int s = f[P[i][l]][sa][sb];
          if (l == 0) {
            if (legal(sa, sb, n - sa - sb)) Add(ret, s);
            continue;
          }
          if (st[i] == 'a') Addit(l1, P[i][l1], make_pair(sa + 1, sb), s);
          if (st[i] == 'b') Addit(l1, P[i][l1], make_pair(sa, sb + 1), s);
          if (st[i] == 'c') Addit(l1, P[i][l1], make_pair(sa, sb), s);
          if (st[i] != 'a' && i && la[i - 1] != -1)
            Addit(l1, P[la[i - 1]][l1], make_pair(sa + 1, sb), s);
          if (st[i] != 'b' && i && lb[i - 1] != -1)
            Addit(l1, P[lb[i - 1]][l1], make_pair(sa, sb + 1), s);
          if (st[i] != 'c' && i && lc[i - 1] != -1)
            Addit(l1, P[lc[i - 1]][l1], make_pair(sa, sb), s);
        }
      if (P[i][l] != -1) Release(i, l);
    }
  }
}
void print() { printf("%d\n", ret); }
int main() {
  init();
  work();
  print();
  return 0;
}
