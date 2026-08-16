#include <bits/stdc++.h>
using namespace std;
const int maxn = 4111;
const int maxm = 257;
const int inf = 0x3f3f3f3f;
int f[maxn][maxn];
char A[maxn], B[maxn];
int pos[2][maxm];
int t[5];
int n, m;
bool get() {
  for (int i = 0; i < 4; ++i)
    if (1 != scanf("%d", t + i)) return 0;
  scanf("%s%s", A + 1, B + 1);
  return 1;
}
inline void update(int &a, int b) {
  if (b < a) a = b;
}
void work() {
  n = strlen(A + 1), m = strlen(B + 1);
  for (int i = 0; i <= n; ++i)
    for (int j = 0; j <= m; ++j) f[i][j] = inf;
  f[0][0] = 0;
  for (int i = 1; i <= n; ++i) f[i][0] = i * t[1];
  for (int i = 1; i <= m; ++i) f[0][i] = i * t[0];
  memset(pos, 0, sizeof pos);
  for (int i = 1; i <= n;
       pos[0][A[i]] = i, memset(pos[1], 0, sizeof pos[1]), ++i)
    for (int j = 1; j <= m; ++j) {
      update(f[i][j], f[i][j - 1] + t[0]);
      update(f[i][j], f[i - 1][j] + t[1]);
      update(f[i][j], f[i - 1][j - 1] + (A[i] != B[j]) * t[2]);
      int a, b;
      if ((b = pos[1][A[i]]) && (a = pos[0][B[j]])) {
        update(f[i][j], f[a - 1][b - 1] + t[3] + (i - a - 1) * t[1] +
                            (j - b - 1) * t[0]);
      }
      pos[1][B[j]] = j;
    }
  cout << f[n][m] << endl;
}
int main() {
  while (get()) work();
  return 0;
}
