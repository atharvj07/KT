#include <bits/stdc++.h>
using namespace std;
const int q = 410;
int n, m, N, M;
char mp1[q][q], mp2[q][q];
bool ans[q][q], g[26][q][q];
bitset<q> b[26][q], h[q];
bitset<q> shift(const bitset<q> &c, int len, int s) {
  assert(0 <= s && s < len);
  return (c >> s) | (c << (len - s));
}
void solve() {
  scanf("%d%d", &N, &M);
  for (int i = 0; i < N; i++) scanf("%s", mp1[i]);
  for (int j = 0; j < N; j++)
    for (int k = 0; k < M; k++) {
      b[mp1[j][k] - 'a'][j][k] = 1;
    }
  for (int i = 0; i < N; i++) h[i] = ~h[i];
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; i++) scanf("%s", mp2[i]);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      int w = mp2[i][j];
      if (w == '?') continue;
      int shiftx = ((-i) % N + N) % N, shifty = (j % M + M) % M;
      for (int k = 0; k < N; k++) {
        int nx = (k + shiftx) % N;
        h[nx] &= shift(b[w - 'a'][k], M, shifty);
      }
    }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) printf("%d", h[i][j] ? 1 : 0);
    printf("\n");
  }
}
int main() {
  solve();
  return 0;
}
