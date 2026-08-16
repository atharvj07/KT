#include <bits/stdc++.h>
using namespace std;
const int fin = 0, maxn = 30;
int n, m;
int a[maxn];
vector<pair<int, int> > V;
void U(int p, int A, int B, int C) {
  if (p > n) return;
  U(p + 1, A, C, B);
  for (int i = 0; i < a[p]; ++i) V.push_back(pair<int, int>(A, B));
  U(p + 1, C, B, A);
}
void F(int p, int A, int B, int C) {
  int i;
  if (p == n) {
    for (i = 0; i < a[p] - 1; ++i) V.push_back(pair<int, int>(A, C));
    for (V.push_back(pair<int, int>(A, B)), i = 0; i < a[p] - 1; ++i)
      V.push_back(pair<int, int>(C, B));
  } else if (a[p] == 1)
    U(p, A, B, C);
  else {
    U(p + 1, A, B, C);
    for (i = 0; i < a[p]; ++i) V.push_back(pair<int, int>(A, C));
    U(p + 1, B, A, C);
    for (i = 0; i < a[p]; ++i) V.push_back(pair<int, int>(C, B));
    F(p + 1, A, B, C);
  }
}
int main() {
  if (fin) {
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);
  }
  int i, r, w = 0;
  scanf("%d", &m);
  for (i = 0; i < m; ++i, r = w)
    if (scanf("%d", &w), w == r)
      ++a[n];
    else
      a[++n] = 1;
  F(1, 1, 3, 2);
  printf("%d\n", V.size());
  for (i = 0; i < V.size(); ++i) printf("%d %d\n", V[i].first, V[i].second);
  return 0;
}
